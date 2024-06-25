import typing
import collections.abc
import bpy.ops.transform
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def active_frame_delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete the active frame for the active Grease Pencil Layer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def active_frames_delete_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete the active frame(s) of all editable Grease Pencil layers

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def annotate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "DRAW",
    arrowstyle_start: str | None = "NONE",
    arrowstyle_end: str | None = "NONE",
    use_stabilizer: bool | typing.Any | None = False,
    stabilizer_factor: typing.Any | None = 0.75,
    stabilizer_radius: typing.Any | None = 35,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    wait_for_input: bool | typing.Any | None = True,
):
    """Make annotations on the active data

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode, Way to interpret mouse movements

    DRAW
    Draw Freehand -- Draw freehand stroke(s).

    DRAW_STRAIGHT
    Draw Straight Lines -- Draw straight line segment(s).

    DRAW_POLY
    Draw Poly Line -- Click to place endpoints of straight line segments (connected).

    ERASER
    Eraser -- Erase Annotation strokes.
        :type mode: str | None
        :param arrowstyle_start: Start Arrow Style, Stroke start style

    NONE
    None -- Don't use any arrow/style in corner.

    ARROW
    Arrow -- Use closed arrow style.

    ARROW_OPEN
    Open Arrow -- Use open arrow style.

    ARROW_OPEN_INVERTED
    Segment -- Use perpendicular segment style.

    DIAMOND
    Square -- Use square style.
        :type arrowstyle_start: str | None
        :param arrowstyle_end: End Arrow Style, Stroke end style

    NONE
    None -- Don't use any arrow/style in corner.

    ARROW
    Arrow -- Use closed arrow style.

    ARROW_OPEN
    Open Arrow -- Use open arrow style.

    ARROW_OPEN_INVERTED
    Segment -- Use perpendicular segment style.

    DIAMOND
    Square -- Use square style.
        :type arrowstyle_end: str | None
        :param use_stabilizer: Stabilize Stroke, Helper to draw smooth and clean lines. Press Shift for an invert effect (even if this option is not active)
        :type use_stabilizer: bool | typing.Any | None
        :param stabilizer_factor: Stabilizer Stroke Factor, Higher values gives a smoother stroke
        :type stabilizer_factor: typing.Any | None
        :param stabilizer_radius: Stabilizer Stroke Radius, Minimum distance from last point before stroke continues
        :type stabilizer_radius: typing.Any | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately
        :type wait_for_input: bool | typing.Any | None
    """

    ...

def annotation_active_frame_delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete the active frame for the active Annotation Layer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def annotation_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add new Annotation data-block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def bake_grease_pencil_animation(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame_start: typing.Any | None = 1,
    frame_end: typing.Any | None = 250,
    step: typing.Any | None = 1,
    only_selected: bool | typing.Any | None = False,
    frame_target: typing.Any | None = 1,
    project_type: str | None = "KEEP",
):
    """Bake grease pencil object transform to grease pencil keyframes

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param frame_start: Start Frame, The start frame
        :type frame_start: typing.Any | None
        :param frame_end: End Frame, The end frame of animation
        :type frame_end: typing.Any | None
        :param step: Step, Step between generated frames
        :type step: typing.Any | None
        :param only_selected: Only Selected Keyframes, Convert only selected keyframes
        :type only_selected: bool | typing.Any | None
        :param frame_target: Target Frame, Destination frame
        :type frame_target: typing.Any | None
        :param project_type: Projection Type

    KEEP
    No Reproject.

    FRONT
    Front -- Reproject the strokes using the X-Z plane.

    SIDE
    Side -- Reproject the strokes using the Y-Z plane.

    TOP
    Top -- Reproject the strokes using the X-Y plane.

    VIEW
    View -- Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using 'Cursor' Stroke Placement.

    CURSOR
    Cursor -- Reproject the strokes using the orientation of 3D cursor.
        :type project_type: str | None
    """

    ...

def bake_mesh_animation(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    target: str | None = "NEW",
    frame_start: typing.Any | None = 1,
    frame_end: typing.Any | None = 250,
    step: typing.Any | None = 1,
    thickness: typing.Any | None = 1,
    angle: typing.Any | None = 1.22173,
    offset: typing.Any | None = 0.001,
    seams: bool | typing.Any | None = False,
    faces: bool | typing.Any | None = True,
    only_selected: bool | typing.Any | None = False,
    frame_target: typing.Any | None = 1,
    project_type: str | None = "VIEW",
):
    """Bake mesh animation to grease pencil strokes

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param target: Target Object, Target grease pencil
        :type target: str | None
        :param frame_start: Start Frame, The start frame
        :type frame_start: typing.Any | None
        :param frame_end: End Frame, The end frame of animation
        :type frame_end: typing.Any | None
        :param step: Step, Step between generated frames
        :type step: typing.Any | None
        :param thickness: Thickness
        :type thickness: typing.Any | None
        :param angle: Threshold Angle, Threshold to determine ends of the strokes
        :type angle: typing.Any | None
        :param offset: Stroke Offset, Offset strokes from fill
        :type offset: typing.Any | None
        :param seams: Only Seam Edges, Convert only seam edges
        :type seams: bool | typing.Any | None
        :param faces: Export Faces, Export faces as filled strokes
        :type faces: bool | typing.Any | None
        :param only_selected: Only Selected Keyframes, Convert only selected keyframes
        :type only_selected: bool | typing.Any | None
        :param frame_target: Target Frame, Destination frame
        :type frame_target: typing.Any | None
        :param project_type: Projection Type

    KEEP
    No Reproject.

    FRONT
    Front -- Reproject the strokes using the X-Z plane.

    SIDE
    Side -- Reproject the strokes using the Y-Z plane.

    TOP
    Top -- Reproject the strokes using the X-Y plane.

    VIEW
    View -- Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using 'Cursor' Stroke Placement.

    CURSOR
    Cursor -- Reproject the strokes using the orientation of 3D cursor.
        :type project_type: str | None
    """

    ...

def blank_frame_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    all_layers: bool | typing.Any | None = False,
):
    """Insert a blank frame on the current frame (all subsequently existing frames, if any, are shifted right by one frame)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param all_layers: All Layers, Create blank frame in all layers, not only active
    :type all_layers: bool | typing.Any | None
    """

    ...

def brush_reset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset brush to default parameters

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def brush_reset_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete all mode brushes and recreate a default set

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def convert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "PATH",
    bevel_depth: typing.Any | None = 0.0,
    bevel_resolution: typing.Any | None = 0,
    use_normalize_weights: bool | typing.Any | None = True,
    radius_multiplier: typing.Any | None = 1.0,
    use_link_strokes: bool | typing.Any | None = False,
    timing_mode: str | None = "FULL",
    frame_range: typing.Any | None = 100,
    start_frame: typing.Any | None = 1,
    use_realtime: bool | typing.Any | None = False,
    end_frame: typing.Any | None = 250,
    gap_duration: typing.Any | None = 0.0,
    gap_randomness: typing.Any | None = 0.0,
    seed: typing.Any | None = 0,
    use_timing_data: bool | typing.Any | None = False,
):
    """Convert the active Grease Pencil layer to a new Curve Object

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Which type of curve to convert to

    PATH
    Path -- Animation path.

    CURVE
    Bézier Curve -- Smooth Bézier curve.

    POLY
    Polygon Curve -- Bézier curve with straight-line segments (vector handles).
        :type type: str | None
        :param bevel_depth: Bevel Depth
        :type bevel_depth: typing.Any | None
        :param bevel_resolution: Bevel Resolution, Bevel resolution when depth is non-zero
        :type bevel_resolution: typing.Any | None
        :param use_normalize_weights: Normalize Weight, Normalize weight (set from stroke width)
        :type use_normalize_weights: bool | typing.Any | None
        :param radius_multiplier: Radius Factor, Multiplier for the points' radii (set from stroke width)
        :type radius_multiplier: typing.Any | None
        :param use_link_strokes: Link Strokes, Whether to link strokes with zero-radius sections of curves
        :type use_link_strokes: bool | typing.Any | None
        :param timing_mode: Timing Mode, How to use timing data stored in strokes

    NONE
    No Timing -- Ignore timing.

    LINEAR
    Linear -- Simple linear timing.

    FULL
    Original -- Use the original timing, gaps included.

    CUSTOMGAP
    Custom Gaps -- Use the original timing, but with custom gap lengths (in frames).
        :type timing_mode: str | None
        :param frame_range: Frame Range, The duration of evaluation of the path control curve
        :type frame_range: typing.Any | None
        :param start_frame: Start Frame, The start frame of the path control curve
        :type start_frame: typing.Any | None
        :param use_realtime: Realtime, Whether the path control curve reproduces the drawing in realtime, starting from Start Frame
        :type use_realtime: bool | typing.Any | None
        :param end_frame: End Frame, The end frame of the path control curve (if Realtime is not set)
        :type end_frame: typing.Any | None
        :param gap_duration: Gap Duration, Custom Gap mode: (Average) length of gaps, in frames (Note: Realtime value, will be scaled if Realtime is not set)
        :type gap_duration: typing.Any | None
        :param gap_randomness: Gap Randomness, Custom Gap mode: Number of frames that gap lengths can vary
        :type gap_randomness: typing.Any | None
        :param seed: Random Seed, Custom Gap mode: Random generator seed
        :type seed: typing.Any | None
        :param use_timing_data: Has Valid Timing, Whether the converted Grease Pencil layer has valid timing data (internal use)
        :type use_timing_data: bool | typing.Any | None
    """

    ...

def convert_old_files(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    annotation: bool | typing.Any | None = False,
):
    """Convert 2.7x grease pencil files to 2.80

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param annotation: Annotation, Convert to Annotations
    :type annotation: bool | typing.Any | None
    """

    ...

def copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy selected Grease Pencil points and strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def data_unlink(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Unlink active Annotation data-block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "POINTS",
):
    """Delete selected Grease Pencil strokes, vertices, or frames

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Method used for deleting Grease Pencil data

    POINTS
    Points -- Delete selected points and split strokes into segments.

    STROKES
    Strokes -- Delete selected strokes.

    FRAME
    Frame -- Delete active frame.
        :type type: str | None
    """

    ...

def dissolve(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "POINTS",
):
    """Delete selected points without splitting strokes

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Method used for dissolving stroke points

    POINTS
    Dissolve -- Dissolve selected points.

    BETWEEN
    Dissolve Between -- Dissolve points between selected points.

    UNSELECT
    Dissolve Unselect -- Dissolve all unselected points.
        :type type: str | None
    """

    ...

def draw(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "DRAW",
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    wait_for_input: bool | typing.Any | None = True,
    disable_straight: bool | typing.Any | None = False,
    disable_fill: bool | typing.Any | None = False,
    disable_stabilizer: bool | typing.Any | None = False,
    guide_last_angle: typing.Any | None = 0.0,
):
    """Draw a new stroke in the active Grease Pencil object

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode, Way to interpret mouse movements

    DRAW
    Draw Freehand -- Draw freehand stroke(s).

    DRAW_STRAIGHT
    Draw Straight Lines -- Draw straight line segment(s).

    ERASER
    Eraser -- Erase Grease Pencil strokes.
        :type mode: str | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately
        :type wait_for_input: bool | typing.Any | None
        :param disable_straight: No Straight lines, Disable key for straight lines
        :type disable_straight: bool | typing.Any | None
        :param disable_fill: No Fill Areas, Disable fill to use stroke as fill boundary
        :type disable_fill: bool | typing.Any | None
        :param disable_stabilizer: No Stabilizer
        :type disable_stabilizer: bool | typing.Any | None
        :param guide_last_angle: Angle, Speed guide angle
        :type guide_last_angle: typing.Any | None
    """

    ...

def duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Duplicate the selected Grease Pencil strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def duplicate_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    GPENCIL_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Make copies of the selected Grease Pencil strokes and move them

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param GPENCIL_OT_duplicate: Duplicate Strokes, Duplicate the selected Grease Pencil strokes
    :type GPENCIL_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def editmode_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    back: bool | typing.Any | None = False,
):
    """Enter/Exit edit mode for Grease Pencil strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param back: Return to Previous Mode, Return to previous mode
    :type back: bool | typing.Any | None
    """

    ...

def extract_palette_vertex(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    selected: bool | typing.Any | None = False,
    threshold: typing.Any | None = 1,
):
    """Extract all colors used in Grease Pencil Vertex and create a Palette

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param selected: Only Selected, Convert only selected strokes
    :type selected: bool | typing.Any | None
    :param threshold: Threshold
    :type threshold: typing.Any | None
    """

    ...

def extrude(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Extrude the selected Grease Pencil points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def extrude_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    GPENCIL_OT_extrude: extrude | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Extrude selected points and move them

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param GPENCIL_OT_extrude: Extrude Stroke Points, Extrude the selected Grease Pencil points
    :type GPENCIL_OT_extrude: extrude | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def fill(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    on_back: bool | typing.Any | None = False,
):
    """Fill with color the shape formed by strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param on_back: Draw on Back, Send new stroke to back
    :type on_back: bool | typing.Any | None
    """

    ...

def frame_clean_duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "ALL",
):
    """Remove duplicate keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def frame_clean_fill(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "ACTIVE",
):
    """Remove 'no fill' boundary strokes

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    ACTIVE
    Active Frame Only -- Clean active frame only.

    ALL
    All Frames -- Clean all frames in all layers.
        :type mode: str | None
    """

    ...

def frame_clean_loose(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    limit: typing.Any | None = 1,
):
    """Remove loose points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param limit: Limit, Number of points to consider stroke as loose
    :type limit: typing.Any | None
    """

    ...

def frame_duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "ACTIVE",
):
    """Make a copy of the active Grease Pencil Frame

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    ACTIVE
    Active -- Duplicate frame in active layer only.

    ALL
    All -- Duplicate active frames in all layers.
        :type mode: str | None
    """

    ...

def generate_weights(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "NAME",
    armature: str | None = "DEFAULT",
    ratio: typing.Any | None = 0.1,
    decay: typing.Any | None = 0.8,
):
    """Generate automatic weights for armatures (requires armature modifier)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
    :param armature: Armature, Armature to use
    :type armature: str | None
    :param ratio: Ratio, Ratio between bone length and influence radius
    :type ratio: typing.Any | None
    :param decay: Decay, Factor to reduce influence depending of distance to bone axis
    :type decay: typing.Any | None
    """

    ...

def guide_rotate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    increment: bool | typing.Any | None = True,
    angle: typing.Any | None = 0.0,
):
    """Rotate guide angle

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param increment: Increment, Increment angle
    :type increment: bool | typing.Any | None
    :param angle: Angle, Guide angle
    :type angle: typing.Any | None
    """

    ...

def hide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | typing.Any | None = False,
):
    """Hide selected/unselected Grease Pencil layers

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected layers
    :type unselected: bool | typing.Any | None
    """

    ...

def image_to_grease_pencil(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    size: typing.Any | None = 0.005,
    mask: bool | typing.Any | None = False,
):
    """Generate a Grease Pencil Object using Image as source

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param size: Point Size, Size used for grease pencil points
    :type size: typing.Any | None
    :param mask: Generate Mask, Create an inverted image for masking using alpha channel
    :type mask: bool | typing.Any | None
    """

    ...

def interpolate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    shift: typing.Any | None = 0.0,
    layers: str | None = "ACTIVE",
    interpolate_selected_only: bool | typing.Any | None = False,
    exclude_breakdowns: bool | typing.Any | None = False,
    flip: str | None = "AUTO",
    smooth_steps: typing.Any | None = 1,
    smooth_factor: typing.Any | None = 0.0,
    release_confirm: bool | typing.Any | None = False,
):
    """Interpolate grease pencil strokes between frames

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param shift: Shift, Bias factor for which frame has more influence on the interpolated strokes
    :type shift: typing.Any | None
    :param layers: Layer, Layers included in the interpolation
    :type layers: str | None
    :param interpolate_selected_only: Only Selected, Interpolate only selected strokes
    :type interpolate_selected_only: bool | typing.Any | None
    :param exclude_breakdowns: Exclude Breakdowns, Exclude existing Breakdowns keyframes as interpolation extremes
    :type exclude_breakdowns: bool | typing.Any | None
    :param flip: Flip Mode, Invert destination stroke to match start and end with source stroke
    :type flip: str | None
    :param smooth_steps: Iterations, Number of times to smooth newly created strokes
    :type smooth_steps: typing.Any | None
    :param smooth_factor: Smooth, Amount of smoothing to apply to interpolated strokes, to reduce jitter/noise
    :type smooth_factor: typing.Any | None
    :param release_confirm: Confirm on Release
    :type release_confirm: bool | typing.Any | None
    """

    ...

def interpolate_reverse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove breakdown frames generated by interpolating between two Grease Pencil frames

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def interpolate_sequence(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    step: typing.Any | None = 1,
    layers: str | None = "ACTIVE",
    interpolate_selected_only: bool | typing.Any | None = False,
    exclude_breakdowns: bool | typing.Any | None = False,
    flip: str | None = "AUTO",
    smooth_steps: typing.Any | None = 1,
    smooth_factor: typing.Any | None = 0.0,
    type: str | None = "LINEAR",
    easing: str | None = "AUTO",
    back: typing.Any | None = 1.702,
    amplitude: typing.Any | None = 0.15,
    period: typing.Any | None = 0.15,
):
    """Generate 'in-betweens' to smoothly interpolate between Grease Pencil frames

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param step: Step, Number of frames between generated interpolated frames
        :type step: typing.Any | None
        :param layers: Layer, Layers included in the interpolation
        :type layers: str | None
        :param interpolate_selected_only: Only Selected, Interpolate only selected strokes
        :type interpolate_selected_only: bool | typing.Any | None
        :param exclude_breakdowns: Exclude Breakdowns, Exclude existing Breakdowns keyframes as interpolation extremes
        :type exclude_breakdowns: bool | typing.Any | None
        :param flip: Flip Mode, Invert destination stroke to match start and end with source stroke
        :type flip: str | None
        :param smooth_steps: Iterations, Number of times to smooth newly created strokes
        :type smooth_steps: typing.Any | None
        :param smooth_factor: Smooth, Amount of smoothing to apply to interpolated strokes, to reduce jitter/noise
        :type smooth_factor: typing.Any | None
        :param type: Type, Interpolation method to use the next time 'Interpolate Sequence' is run

    LINEAR
    Linear -- Straight-line interpolation between A and B (i.e. no ease in/out).

    CUSTOM
    Custom -- Custom interpolation defined using a curve map.

    SINE
    Sinusoidal -- Sinusoidal easing (weakest, almost linear but with a slight curvature).

    QUAD
    Quadratic -- Quadratic easing.

    CUBIC
    Cubic -- Cubic easing.

    QUART
    Quartic -- Quartic easing.

    QUINT
    Quintic -- Quintic easing.

    EXPO
    Exponential -- Exponential easing (dramatic).

    CIRC
    Circular -- Circular easing (strongest and most dynamic).

    BACK
    Back -- Cubic easing with overshoot and settle.

    BOUNCE
    Bounce -- Exponentially decaying parabolic bounce, like when objects collide.

    ELASTIC
    Elastic -- Exponentially decaying sine wave, like an elastic band.
        :type type: str | None
        :param easing: Easing, Which ends of the segment between the preceding and following grease pencil frames easing interpolation is applied to

    AUTO
    Automatic Easing -- Easing type is chosen automatically based on what the type of interpolation used (e.g. 'Ease In' for transitional types, and 'Ease Out' for dynamic effects).

    EASE_IN
    Ease In -- Only on the end closest to the next keyframe.

    EASE_OUT
    Ease Out -- Only on the end closest to the first keyframe.

    EASE_IN_OUT
    Ease In and Out -- Segment between both keyframes.
        :type easing: str | None
        :param back: Back, Amount of overshoot for 'back' easing
        :type back: typing.Any | None
        :param amplitude: Amplitude, Amount to boost elastic bounces for 'elastic' easing
        :type amplitude: typing.Any | None
        :param period: Period, Time between bounces for elastic easing
        :type period: typing.Any | None
    """

    ...

def layer_active(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    layer: typing.Any | None = 0,
):
    """Active Grease Pencil layer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param layer: Grease Pencil Layer
    :type layer: typing.Any | None
    """

    ...

def layer_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    layer: typing.Any | None = 0,
    new_layer_name: str | typing.Any = "",
):
    """Add new layer or note for the active data-block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param layer: Grease Pencil Layer
    :type layer: typing.Any | None
    :param new_layer_name: Name, Name of the newly added layer
    :type new_layer_name: str | typing.Any
    """

    ...

def layer_annotation_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add new Annotation layer or note for the active data-block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def layer_annotation_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "UP",
):
    """Move the active Annotation layer up/down in the list

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def layer_annotation_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove active Annotation layer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def layer_change(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    layer: str | None = "DEFAULT",
):
    """Change active Grease Pencil layer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param layer: Grease Pencil Layer
    :type layer: str | None
    """

    ...

def layer_duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "ALL",
):
    """Make a copy of the active Grease Pencil layer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
    """

    ...

def layer_duplicate_object(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "ALL",
    only_active: bool | typing.Any | None = True,
):
    """Make a copy of the active Grease Pencil layer to selected object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
    :param only_active: Only Active, Copy only active Layer, uncheck to append all layers
    :type only_active: bool | typing.Any | None
    """

    ...

def layer_isolate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    affect_visibility: bool | typing.Any | None = False,
):
    """Toggle whether the active layer is the only one that can be edited and/or visible

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility
    :type affect_visibility: bool | typing.Any | None
    """

    ...

def layer_mask_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
):
    """Add new layer as masking

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Layer, Name of the layer
    :type name: str | typing.Any
    """

    ...

def layer_mask_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "UP",
):
    """Move the active Grease Pencil mask layer up/down in the list

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def layer_mask_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove Layer Mask

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def layer_merge(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "ACTIVE",
):
    """Combine Layers

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    ACTIVE
    Active -- Combine active layer into the layer below.

    ALL
    All -- Combine all layers into the active layer.
        :type mode: str | None
    """

    ...

def layer_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "UP",
):
    """Move the active Grease Pencil layer up/down in the list

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def layer_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove active Grease Pencil layer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def lock_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Lock all Grease Pencil layers to prevent them from being accidentally modified

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def lock_layer(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Lock and hide any color not used in any layer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def material_hide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | typing.Any | None = False,
):
    """Hide selected/unselected Grease Pencil materials

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected colors
    :type unselected: bool | typing.Any | None
    """

    ...

def material_isolate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    affect_visibility: bool | typing.Any | None = False,
):
    """Toggle whether the active material is the only one that is editable and/or visible

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility
    :type affect_visibility: bool | typing.Any | None
    """

    ...

def material_lock_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Lock all Grease Pencil materials to prevent them from being accidentally modified

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def material_lock_unused(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Lock any material not used in any selected stroke

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def material_reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Unhide all hidden Grease Pencil materials

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def material_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    deselect: bool | typing.Any | None = False,
):
    """Select/Deselect all Grease Pencil strokes using current material

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param deselect: Deselect, Unselect strokes
    :type deselect: bool | typing.Any | None
    """

    ...

def material_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    slot: str | None = "DEFAULT",
):
    """Set active material

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param slot: Material Slot
    :type slot: str | None
    """

    ...

def material_to_vertex_color(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    remove: bool | typing.Any | None = True,
    palette: bool | typing.Any | None = True,
    selected: bool | typing.Any | None = False,
    threshold: typing.Any | None = 3,
):
    """Replace materials in strokes with Vertex Color

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param remove: Remove Unused Materials, Remove any unused material after the conversion
    :type remove: bool | typing.Any | None
    :param palette: Create Palette, Create a new palette with colors
    :type palette: bool | typing.Any | None
    :param selected: Only Selected, Convert only selected strokes
    :type selected: bool | typing.Any | None
    :param threshold: Threshold
    :type threshold: typing.Any | None
    """

    ...

def material_unlock_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Unlock all Grease Pencil materials so that they can be edited

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def materials_copy_to_object(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    only_active: bool | typing.Any | None = True,
):
    """Append Materials of the active Grease Pencil to other object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_active: Only Active, Append only active material, uncheck to append all materials
    :type only_active: bool | typing.Any | None
    """

    ...

def move_to_layer(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    layer: typing.Any | None = 0,
    new_layer_name: str | typing.Any = "",
):
    """Move selected strokes to another layer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param layer: Grease Pencil Layer
    :type layer: typing.Any | None
    :param new_layer_name: Name, Name of the newly added layer
    :type new_layer_name: str | typing.Any
    """

    ...

def paintmode_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    back: bool | typing.Any | None = False,
):
    """Enter/Exit paint mode for Grease Pencil strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param back: Return to Previous Mode, Return to previous mode
    :type back: bool | typing.Any | None
    """

    ...

def paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "ACTIVE",
    paste_back: bool | typing.Any | None = False,
):
    """Paste previously copied strokes to active layer or to original layer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    :param paste_back: Paste on Back, Add pasted strokes behind all strokes
    :type paste_back: bool | typing.Any | None
    """

    ...

def primitive_box(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    subdivision: typing.Any | None = 3,
    edges: typing.Any | None = 1,
    type: str | None = "BOX",
    wait_for_input: bool | typing.Any | None = True,
):
    """Create predefined grease pencil stroke box shapes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param subdivision: Subdivisions, Number of subdivisions per segment
    :type subdivision: typing.Any | None
    :param edges: Edges, Number of points per segment
    :type edges: typing.Any | None
    :param type: Type, Type of shape
    :type type: str | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | typing.Any | None
    """

    ...

def primitive_circle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    subdivision: typing.Any | None = 94,
    edges: typing.Any | None = 1,
    type: str | None = "CIRCLE",
    wait_for_input: bool | typing.Any | None = True,
):
    """Create predefined grease pencil stroke circle shapes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param subdivision: Subdivisions, Number of subdivisions per segment
    :type subdivision: typing.Any | None
    :param edges: Edges, Number of points per segment
    :type edges: typing.Any | None
    :param type: Type, Type of shape
    :type type: str | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | typing.Any | None
    """

    ...

def primitive_curve(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    subdivision: typing.Any | None = 62,
    edges: typing.Any | None = 1,
    type: str | None = "CURVE",
    wait_for_input: bool | typing.Any | None = True,
):
    """Create predefined grease pencil stroke curve shapes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param subdivision: Subdivisions, Number of subdivisions per segment
    :type subdivision: typing.Any | None
    :param edges: Edges, Number of points per segment
    :type edges: typing.Any | None
    :param type: Type, Type of shape
    :type type: str | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | typing.Any | None
    """

    ...

def primitive_line(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    subdivision: typing.Any | None = 6,
    edges: typing.Any | None = 1,
    type: str | None = "LINE",
    wait_for_input: bool | typing.Any | None = True,
):
    """Create predefined grease pencil stroke lines

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param subdivision: Subdivisions, Number of subdivisions per segment
    :type subdivision: typing.Any | None
    :param edges: Edges, Number of points per segment
    :type edges: typing.Any | None
    :param type: Type, Type of shape
    :type type: str | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | typing.Any | None
    """

    ...

def primitive_polyline(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    subdivision: typing.Any | None = 6,
    edges: typing.Any | None = 1,
    type: str | None = "POLYLINE",
    wait_for_input: bool | typing.Any | None = True,
):
    """Create predefined grease pencil stroke polylines

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param subdivision: Subdivisions, Number of subdivisions per segment
    :type subdivision: typing.Any | None
    :param edges: Edges, Number of points per segment
    :type edges: typing.Any | None
    :param type: Type, Type of shape
    :type type: str | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | typing.Any | None
    """

    ...

def recalc_geometry(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Update all internal geometry data

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def reproject(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "VIEW",
    keep_original: bool | typing.Any | None = False,
    offset: typing.Any | None = 0.0,
):
    """Reproject the selected strokes from the current viewpoint as if they had been newly drawn (e.g. to fix problems from accidental 3D cursor movement or accidental viewport changes, or for matching deforming geometry)

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Projection Type

    FRONT
    Front -- Reproject the strokes using the X-Z plane.

    SIDE
    Side -- Reproject the strokes using the Y-Z plane.

    TOP
    Top -- Reproject the strokes using the X-Y plane.

    VIEW
    View -- Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using 'Cursor' Stroke Placement.

    SURFACE
    Surface -- Reproject the strokes on to the scene geometry, as if drawn using 'Surface' placement.

    CURSOR
    Cursor -- Reproject the strokes using the orientation of 3D cursor.
        :type type: str | None
        :param keep_original: Keep Original, Keep original strokes and create a copy before reprojecting
        :type keep_original: bool | typing.Any | None
        :param offset: Surface Offset
        :type offset: typing.Any | None
    """

    ...

def reset_transform_fill(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "ALL",
):
    """Reset any UV transformation and back to default values

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
    """

    ...

def reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select: bool | typing.Any | None = True,
):
    """Show all Grease Pencil layers

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | typing.Any | None
    """

    ...

def sculpt_paint(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    wait_for_input: bool | typing.Any | None = True,
):
    """Apply tweaks to strokes by painting over the strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
    :param wait_for_input: Wait for Input, Enter a mini 'sculpt-mode' if enabled, otherwise, exit after drawing a single stroke
    :type wait_for_input: bool | typing.Any | None
    """

    ...

def sculptmode_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    back: bool | typing.Any | None = False,
):
    """Enter/Exit sculpt mode for Grease Pencil strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param back: Return to Previous Mode, Return to previous mode
    :type back: bool | typing.Any | None
    """

    ...

def segment_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Add a segment to the dash modifier

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def segment_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
    type: str | None = "UP",
):
    """Move the active dash segment up or down

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    :param type: Type
    :type type: str | None
    """

    ...

def segment_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
    index: typing.Any | None = 0,
):
    """Remove the active segment from the dash modifier

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    :param index: Index, Index of the segment to remove
    :type index: typing.Any | None
    """

    ...

def select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
    deselect: bool | typing.Any | None = False,
    toggle: bool | typing.Any | None = False,
    deselect_all: bool | typing.Any | None = False,
    select_passthrough: bool | typing.Any | None = False,
    entire_strokes: bool | typing.Any | None = False,
    location: typing.Any | None = (0, 0),
    use_shift_extend: bool | typing.Any | None = False,
):
    """Select Grease Pencil strokes and/or stroke points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | typing.Any | None
    :param deselect: Deselect, Remove from selection
    :type deselect: bool | typing.Any | None
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: bool | typing.Any | None
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool | typing.Any | None
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: bool | typing.Any | None
    :param entire_strokes: Entire Strokes, Select entire strokes instead of just the nearest stroke vertex
    :type entire_strokes: bool | typing.Any | None
    :param location: Location, Mouse location
    :type location: typing.Any | None
    :param use_shift_extend: Extend
    :type use_shift_extend: bool | typing.Any | None
    """

    ...

def select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "TOGGLE",
):
    """Change selection of all Grease Pencil strokes currently visible

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

def select_alternate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselect_ends: bool | typing.Any | None = False,
):
    """Select alternative points in same strokes as already selected points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselect_ends: Unselect Ends, Do not select the first and last point of the stroke
    :type unselect_ends: bool | typing.Any | None
    """

    ...

def select_box(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xmin: typing.Any | None = 0,
    xmax: typing.Any | None = 0,
    ymin: typing.Any | None = 0,
    ymax: typing.Any | None = 0,
    wait_for_input: bool | typing.Any | None = True,
    mode: str | None = "SET",
):
    """Select Grease Pencil strokes within a rectangular region

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
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.

    XOR
    Difference -- Invert existing selection.

    AND
    Intersect -- Intersect existing selection.
        :type mode: str | None
    """

    ...

def select_circle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    x: typing.Any | None = 0,
    y: typing.Any | None = 0,
    radius: typing.Any | None = 25,
    wait_for_input: bool | typing.Any | None = True,
    mode: str | None = "SET",
):
    """Select Grease Pencil strokes using brush selection

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param x: X
        :type x: typing.Any | None
        :param y: Y
        :type y: typing.Any | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | typing.Any | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: str | None
    """

    ...

def select_first(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    only_selected_strokes: bool | typing.Any | None = False,
    extend: bool | typing.Any | None = False,
):
    """Select first point in Grease Pencil strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_selected_strokes: Selected Strokes Only, Only select the first point of strokes that already have points selected
    :type only_selected_strokes: bool | typing.Any | None
    :param extend: Extend, Extend selection instead of deselecting all other selected points
    :type extend: bool | typing.Any | None
    """

    ...

def select_grouped(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "LAYER",
):
    """Select all strokes with similar characteristics

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    LAYER
    Layer -- Shared layers.

    MATERIAL
    Material -- Shared materials.
        :type type: str | None
    """

    ...

def select_lasso(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "SET",
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
):
    """Select Grease Pencil strokes using lasso selection

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.

    XOR
    Difference -- Invert existing selection.

    AND
    Intersect -- Intersect existing selection.
        :type mode: str | None
        :param path: Path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
    """

    ...

def select_last(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    only_selected_strokes: bool | typing.Any | None = False,
    extend: bool | typing.Any | None = False,
):
    """Select last point in Grease Pencil strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_selected_strokes: Selected Strokes Only, Only select the last point of strokes that already have points selected
    :type only_selected_strokes: bool | typing.Any | None
    :param extend: Extend, Extend selection instead of deselecting all other selected points
    :type extend: bool | typing.Any | None
    """

    ...

def select_less(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Shrink sets of selected Grease Pencil points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select all points in same strokes as already selected points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_more(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Grow sets of selected Grease Pencil points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_random(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    ratio: typing.Any | None = 0.5,
    seed: typing.Any | None = 0,
    action: str | None = "SELECT",
    unselect_ends: bool | typing.Any | None = False,
):
    """Select random points for non selected strokes

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param ratio: Ratio, Portion of items to select randomly
        :type ratio: typing.Any | None
        :param seed: Random Seed, Seed for the random number generator
        :type seed: typing.Any | None
        :param action: Action, Selection action to execute

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.
        :type action: str | None
        :param unselect_ends: Unselect Ends, Do not select the first and last point of the stroke
        :type unselect_ends: bool | typing.Any | None
    """

    ...

def select_vertex_color(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    threshold: typing.Any | None = 0,
):
    """Select all points with similar vertex color of current selected

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Threshold, Tolerance of the selection. Higher values select a wider range of similar colors
    :type threshold: typing.Any | None
    """

    ...

def selection_opacity_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Hide/Unhide selected points for Grease Pencil strokes setting alpha factor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def selectmode_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Any | None = 0,
):
    """Set selection mode for Grease Pencil strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Select Mode, Select mode
    :type mode: typing.Any | None
    """

    ...

def set_active_material(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set the selected stroke material as the active material

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def snap_cursor_to_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Snap cursor to center of selected points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def snap_to_cursor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_offset: bool | typing.Any | None = True,
):
    """Snap selected points/strokes to the cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_offset: With Offset, Offset the entire stroke instead of selected points only
    :type use_offset: bool | typing.Any | None
    """

    ...

def snap_to_grid(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Snap selected points to the nearest grid points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def stroke_apply_thickness(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Apply the thickness change of the layer to its strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def stroke_arrange(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: str | None = "UP",
):
    """Arrange selected strokes up/down in the display order of the active layer

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction
    :type direction: str | None
    """

    ...

def stroke_caps_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "TOGGLE",
):
    """Change stroke caps mode (rounded or flat)

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    TOGGLE
    Both.

    START
    Start.

    END
    End.

    DEFAULT
    Default -- Set as default rounded.
        :type type: str | None
    """

    ...

def stroke_change_color(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    material: str | typing.Any = "",
):
    """Move selected strokes to active material

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param material: Material, Name of the material
    :type material: str | typing.Any
    """

    ...

def stroke_cutter(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    flat_caps: bool | typing.Any | None = False,
):
    """Select section and cut

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param path: Path
    :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
    :param flat_caps: Flat Caps
    :type flat_caps: bool | typing.Any | None
    """

    ...

def stroke_cyclical_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "TOGGLE",
    geometry: bool | typing.Any | None = False,
):
    """Close or open the selected stroke adding a segment from last to first point

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    :param geometry: Create Geometry, Create new geometry for closing stroke
    :type geometry: bool | typing.Any | None
    """

    ...

def stroke_editcurve_set_handle_type(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "AUTOMATIC",
):
    """Set the type of an edit curve handle

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Spline type
    :type type: str | None
    """

    ...

def stroke_enter_editcurve_mode(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    error_threshold: typing.Any | None = 0.1,
):
    """Called to transform a stroke into a curve

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param error_threshold: Error Threshold, Threshold on the maximum deviation from the actual stroke
    :type error_threshold: typing.Any | None
    """

    ...

def stroke_flip(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Change direction of the points of the selected strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def stroke_join(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "JOIN",
    leave_gaps: bool | typing.Any | None = False,
):
    """Join selected strokes (optionally as new stroke)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    :param leave_gaps: Leave Gaps, Leave gaps between joined strokes instead of linking them
    :type leave_gaps: bool | typing.Any | None
    """

    ...

def stroke_merge(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "STROKE",
    back: bool | typing.Any | None = False,
    additive: bool | typing.Any | None = False,
    cyclic: bool | typing.Any | None = False,
    clear_point: bool | typing.Any | None = False,
    clear_stroke: bool | typing.Any | None = False,
):
    """Create a new stroke with the selected stroke points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
    :param back: Draw on Back, Draw new stroke below all previous strokes
    :type back: bool | typing.Any | None
    :param additive: Additive Drawing, Add to previous drawing
    :type additive: bool | typing.Any | None
    :param cyclic: Cyclic, Close new stroke
    :type cyclic: bool | typing.Any | None
    :param clear_point: Dissolve Points, Dissolve old selected points
    :type clear_point: bool | typing.Any | None
    :param clear_stroke: Delete Strokes, Delete old selected strokes
    :type clear_stroke: bool | typing.Any | None
    """

    ...

def stroke_merge_by_distance(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    threshold: typing.Any | None = 0.001,
    use_unselected: bool | typing.Any | None = False,
):
    """Merge points by distance

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Threshold
    :type threshold: typing.Any | None
    :param use_unselected: Unselected, Use whole stroke, not only selected points
    :type use_unselected: bool | typing.Any | None
    """

    ...

def stroke_merge_material(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    hue_threshold: typing.Any | None = 0.001,
    sat_threshold: typing.Any | None = 0.001,
    val_threshold: typing.Any | None = 0.001,
):
    """Replace materials in strokes merging similar

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param hue_threshold: Hue Threshold
    :type hue_threshold: typing.Any | None
    :param sat_threshold: Saturation Threshold
    :type sat_threshold: typing.Any | None
    :param val_threshold: Value Threshold
    :type val_threshold: typing.Any | None
    """

    ...

def stroke_normalize(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "THICKNESS",
    factor: typing.Any | None = 1.0,
    value: typing.Any | None = 10,
):
    """Normalize stroke attributes

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode, Attribute to be normalized

    THICKNESS
    Thickness -- Normalizes the stroke thickness by making all points use the same thickness value.

    OPACITY
    Opacity -- Normalizes the stroke opacity by making all points use the same opacity value.
        :type mode: str | None
        :param factor: Factor
        :type factor: typing.Any | None
        :param value: Value, Value
        :type value: typing.Any | None
    """

    ...

def stroke_outline(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    view_mode: str | None = "VIEW",
    material_mode: str | None = "ACTIVE",
    thickness: typing.Any | None = 1,
    keep: bool | typing.Any | None = True,
    subdivisions: typing.Any | None = 3,
    length: typing.Any | None = 0.0,
):
    """Convert stroke to perimeter

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param view_mode: View
        :type view_mode: str | None
        :param material_mode: Material Mode

    ACTIVE
    Active Material.

    KEEP
    Keep Material -- Keep current stroke material.

    NEW
    New Material.
        :type material_mode: str | None
        :param thickness: Thickness, Thickness of the stroke perimeter
        :type thickness: typing.Any | None
        :param keep: Keep Shape, Try to keep global shape when the stroke thickness change
        :type keep: bool | typing.Any | None
        :param subdivisions: Subdivisions
        :type subdivisions: typing.Any | None
        :param length: Sample Length
        :type length: typing.Any | None
    """

    ...

def stroke_reset_vertex_color(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "BOTH",
):
    """Reset vertex color for all or selected strokes

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    STROKE
    Stroke -- Reset Vertex Color to Stroke only.

    FILL
    Fill -- Reset Vertex Color to Fill only.

    BOTH
    Stroke & Fill -- Reset Vertex Color to Stroke and Fill.
        :type mode: str | None
    """

    ...

def stroke_sample(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    length: typing.Any | None = 0.1,
    sharp_threshold: typing.Any | None = 0.1,
):
    """Sample stroke points to predefined segment length

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param length: Length
    :type length: typing.Any | None
    :param sharp_threshold: Sharp Threshold
    :type sharp_threshold: typing.Any | None
    """

    ...

def stroke_separate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "POINT",
):
    """Separate the selected strokes or layer in a new grease pencil object

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    POINT
    Selected Points -- Separate the selected points.

    STROKE
    Selected Strokes -- Separate the selected strokes.

    LAYER
    Active Layer -- Separate the strokes of the current layer.
        :type mode: str | None
    """

    ...

def stroke_simplify(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.0,
):
    """Simplify selected strokes, reducing number of points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor
    :type factor: typing.Any | None
    """

    ...

def stroke_simplify_fixed(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    step: typing.Any | None = 1,
):
    """Simplify selected strokes, reducing number of points using fixed algorithm

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param step: Steps, Number of simplify steps
    :type step: typing.Any | None
    """

    ...

def stroke_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    repeat: typing.Any | None = 2,
    factor: typing.Any | None = 1.0,
    only_selected: bool | typing.Any | None = True,
    smooth_position: bool | typing.Any | None = True,
    smooth_thickness: bool | typing.Any | None = True,
    smooth_strength: bool | typing.Any | None = False,
    smooth_uv: bool | typing.Any | None = False,
):
    """Smooth selected strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param repeat: Repeat
    :type repeat: typing.Any | None
    :param factor: Factor
    :type factor: typing.Any | None
    :param only_selected: Selected Points, Smooth only selected points in the stroke
    :type only_selected: bool | typing.Any | None
    :param smooth_position: Position
    :type smooth_position: bool | typing.Any | None
    :param smooth_thickness: Thickness
    :type smooth_thickness: bool | typing.Any | None
    :param smooth_strength: Strength
    :type smooth_strength: bool | typing.Any | None
    :param smooth_uv: UV
    :type smooth_uv: bool | typing.Any | None
    """

    ...

def stroke_split(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Split selected points as new stroke on same frame

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def stroke_start_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set start point for cyclic strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def stroke_subdivide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    number_cuts: typing.Any | None = 1,
    factor: typing.Any | None = 0.0,
    repeat: typing.Any | None = 1,
    only_selected: bool | typing.Any | None = True,
    smooth_position: bool | typing.Any | None = True,
    smooth_thickness: bool | typing.Any | None = True,
    smooth_strength: bool | typing.Any | None = False,
    smooth_uv: bool | typing.Any | None = False,
):
    """Subdivide between continuous selected points of the stroke adding a point half way between them

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param number_cuts: Number of Cuts
    :type number_cuts: typing.Any | None
    :param factor: Smooth
    :type factor: typing.Any | None
    :param repeat: Repeat
    :type repeat: typing.Any | None
    :param only_selected: Selected Points, Smooth only selected points in the stroke
    :type only_selected: bool | typing.Any | None
    :param smooth_position: Position
    :type smooth_position: bool | typing.Any | None
    :param smooth_thickness: Thickness
    :type smooth_thickness: bool | typing.Any | None
    :param smooth_strength: Strength
    :type smooth_strength: bool | typing.Any | None
    :param smooth_uv: UV
    :type smooth_uv: bool | typing.Any | None
    """

    ...

def stroke_trim(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Trim selected stroke to first loop or intersection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def time_segment_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Add a segment to the time modifier

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def time_segment_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
    type: str | None = "UP",
):
    """Move the active time segment up or down

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    :param type: Type
    :type type: str | None
    """

    ...

def time_segment_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
    index: typing.Any | None = 0,
):
    """Remove the active segment from the time modifier

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    :param index: Index, Index of the segment to remove
    :type index: typing.Any | None
    """

    ...

def tint_flip(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Switch tint colors

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def trace_image(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    target: str | None = "NEW",
    thickness: typing.Any | None = 10,
    resolution: typing.Any | None = 5,
    scale: typing.Any | None = 1.0,
    sample: typing.Any | None = 0.0,
    threshold: typing.Any | None = 0.5,
    turnpolicy: str | None = "MINORITY",
    mode: str | None = "SINGLE",
    use_current_frame: bool | typing.Any | None = True,
    frame_number: typing.Any | None = 0,
):
    """Extract Grease Pencil strokes from image

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param target: Target Object, Target grease pencil
        :type target: str | None
        :param thickness: Thickness
        :type thickness: typing.Any | None
        :param resolution: Resolution, Resolution of the generated curves
        :type resolution: typing.Any | None
        :param scale: Scale, Scale of the final stroke
        :type scale: typing.Any | None
        :param sample: Sample, Distance to sample points, zero to disable
        :type sample: typing.Any | None
        :param threshold: Color Threshold, Determine the lightness threshold above which strokes are generated
        :type threshold: typing.Any | None
        :param turnpolicy: Turn Policy, Determines how to resolve ambiguities during decomposition of bitmaps into paths

    BLACK
    Black -- Prefers to connect black (foreground) components.

    WHITE
    White -- Prefers to connect white (background) components.

    LEFT
    Left -- Always take a left turn.

    RIGHT
    Right -- Always take a right turn.

    MINORITY
    Minority -- Prefers to connect the color (black or white) that occurs least frequently in the local neighborhood of the current position.

    MAJORITY
    Majority -- Prefers to connect the color (black or white) that occurs most frequently in the local neighborhood of the current position.

    RANDOM
    Random -- Choose pseudo-randomly.
        :type turnpolicy: str | None
        :param mode: Mode, Determines if trace simple image or full sequence

    SINGLE
    Single -- Trace the current frame of the image.

    SEQUENCE
    Sequence -- Trace full sequence.
        :type mode: str | None
        :param use_current_frame: Start At Current Frame, Trace Image starting in current image frame
        :type use_current_frame: bool | typing.Any | None
        :param frame_number: Trace Frame, Used to trace only one frame of the image sequence, set to zero to trace all
        :type frame_number: typing.Any | None
    """

    ...

def transform_fill(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "ROTATE",
    location: typing.Any | None = (0.0, 0.0),
    rotation: typing.Any | None = 0.0,
    scale: typing.Any | None = 0.0,
    release_confirm: bool | typing.Any | None = False,
):
    """Transform grease pencil stroke fill

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
    :param location: Location
    :type location: typing.Any | None
    :param rotation: Rotation
    :type rotation: typing.Any | None
    :param scale: Scale
    :type scale: typing.Any | None
    :param release_confirm: Confirm on Release
    :type release_confirm: bool | typing.Any | None
    """

    ...

def unlock_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Unlock all Grease Pencil layers so that they can be edited

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_color_brightness_contrast(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "BOTH",
    brightness: typing.Any | None = 0.0,
    contrast: typing.Any | None = 0.0,
):
    """Adjust vertex color brightness/contrast

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
    :param brightness: Brightness
    :type brightness: typing.Any | None
    :param contrast: Contrast
    :type contrast: typing.Any | None
    """

    ...

def vertex_color_hsv(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "BOTH",
    h: typing.Any | None = 0.5,
    s: typing.Any | None = 1.0,
    v: typing.Any | None = 1.0,
):
    """Adjust vertex color HSV values

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
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
    *,
    mode: str | None = "BOTH",
):
    """Invert RGB values

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
    """

    ...

def vertex_color_levels(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "BOTH",
    offset: typing.Any | None = 0.0,
    gain: typing.Any | None = 1.0,
):
    """Adjust levels of vertex colors

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
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
    mode: str | None = "BOTH",
    factor: typing.Any | None = 1.0,
):
    """Set active color to all selected vertex

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
    :param factor: Factor, Mix Factor
    :type factor: typing.Any | None
    """

    ...

def vertex_group_assign(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Assign the selected vertices to the active vertex group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_deselect(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Deselect all selected vertices assigned to the active vertex group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_invert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Invert weights to the active vertex group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_normalize(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Normalize weights to the active vertex group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_normalize_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    lock_active: bool | typing.Any | None = True,
):
    """Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param lock_active: Lock Active, Keep the values of the active group while normalizing others
    :type lock_active: bool | typing.Any | None
    """

    ...

def vertex_group_remove_from(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the selected vertices from active or all vertex group(s)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select all the vertices assigned to the active vertex group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.5,
    repeat: typing.Any | None = 1,
):
    """Smooth weights to the active vertex group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor
    :type factor: typing.Any | None
    :param repeat: Iterations
    :type repeat: typing.Any | None
    """

    ...

def vertex_paint(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    wait_for_input: bool | typing.Any | None = True,
):
    """Paint stroke points with a color

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | typing.Any | None
    """

    ...

def vertexmode_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    back: bool | typing.Any | None = False,
):
    """Enter/Exit vertex paint mode for Grease Pencil strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param back: Return to Previous Mode, Return to previous mode
    :type back: bool | typing.Any | None
    """

    ...

def weight_paint(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    wait_for_input: bool | typing.Any | None = True,
):
    """Draw weight on stroke points

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param stroke: Stroke
    :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | typing.Any | None
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

def weight_toggle_direction(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle Add/Subtract for the weight paint draw tool

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def weightmode_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    back: bool | typing.Any | None = False,
):
    """Enter/Exit weight paint mode for Grease Pencil strokes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param back: Return to Previous Mode, Return to previous mode
    :type back: bool | typing.Any | None
    """

    ...
