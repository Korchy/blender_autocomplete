import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

def align(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    axis: typing.Literal[
        "ALIGN_S", "ALIGN_T", "ALIGN_U", "ALIGN_AUTO", "ALIGN_X", "ALIGN_Y"
    ]
    | None = "ALIGN_AUTO",
) -> None:
    """Aligns selected UV vertices on a line

        :param axis: Axis, Axis to align UV locations on

    ALIGN_S
    Straighten -- Align UV vertices along the line defined by the endpoints.

    ALIGN_T
    Straighten X -- Align UV vertices, moving them horizontally to the line defined by the endpoints.

    ALIGN_U
    Straighten Y -- Align UV vertices, moving them vertically to the line defined by the endpoints.

    ALIGN_AUTO
    Align Auto -- Automatically choose the direction on which there is most alignment already.

    ALIGN_X
    Align Vertically -- Align UV vertices on a vertical line.

    ALIGN_Y
    Align Horizontally -- Align UV vertices on a horizontal line.
    """

def align_rotation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    method: typing.Literal["AUTO", "EDGE", "GEOMETRY"] | None = "AUTO",
    axis: typing.Literal["X", "Y", "Z"] | None = "X",
    correct_aspect: bool | None = False,
) -> None:
    """Align the UV islands rotation

        :param method: Method, Method to calculate rotation angle

    AUTO
    Auto -- Align from all edges.

    EDGE
    Edge -- Only selected edges.

    GEOMETRY
    Geometry -- Align to Geometry axis.
        :param axis: Axis, Axis to align to

    X
    X -- X axis.

    Y
    Y -- Y axis.

    Z
    Z -- Z axis.
        :param correct_aspect: Correct Aspect, Take image aspect ratio into account
    """

def average_islands_scale(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    scale_uv: bool | None = False,
    shear: bool | None = False,
) -> None:
    """Average the size of separate UV islands, based on their area in 3D space

    :param scale_uv: Non-Uniform, Scale U and V independently
    :param shear: Shear, Reduce shear within islands
    """

def copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy selected UV vertices"""

def cube_project(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    cube_size: float | None = 1.0,
    correct_aspect: bool | None = True,
    clip_to_bounds: bool | None = False,
    scale_to_bounds: bool | None = False,
) -> None:
    """Project the UV vertices of the mesh over the six faces of a cube

    :param cube_size: Cube Size, Size of the cube to project on
    :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    """

def cursor_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Set 2D cursor location

    :param location: Location, Cursor location in normalized (0.0 to 1.0) coordinates
    """

def cylinder_project(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["VIEW_ON_EQUATOR", "VIEW_ON_POLES", "ALIGN_TO_OBJECT"]
    | None = "VIEW_ON_EQUATOR",
    align: typing.Literal["POLAR_ZX", "POLAR_ZY"] | None = "POLAR_ZX",
    pole: typing.Literal["PINCH", "FAN"] | None = "PINCH",
    seam: bool | None = False,
    radius: float | None = 1.0,
    correct_aspect: bool | None = True,
    clip_to_bounds: bool | None = False,
    scale_to_bounds: bool | None = False,
) -> None:
    """Project the UV vertices of the mesh over the curved wall of a cylinder

        :param direction: Direction, Direction of the sphere or cylinder

    VIEW_ON_EQUATOR
    View on Equator -- 3D view is on the equator.

    VIEW_ON_POLES
    View on Poles -- 3D view is on the poles.

    ALIGN_TO_OBJECT
    Align to Object -- Align according to object transform.
        :param align: Align, How to determine rotation around the pole

    POLAR_ZX
    Polar ZX -- Polar 0 is X.

    POLAR_ZY
    Polar ZY -- Polar 0 is Y.
        :param pole: Pole, How to handle faces at the poles

    PINCH
    Pinch -- UVs are pinched at the poles.

    FAN
    Fan -- UVs are fanned at the poles.
        :param seam: Preserve Seams, Separate projections by islands isolated by seams
        :param radius: Radius, Radius of the sphere or cylinder
        :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account
        :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
        :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    """

def export_layout(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    export_all: bool | None = False,
    export_tiles: typing.Literal["NONE", "UDIM", "UV"] | None = "NONE",
    modified: bool | None = False,
    mode: typing.Literal["SVG", "EPS", "PNG"] | None = "PNG",
    size: collections.abc.Iterable[int] | None = (1024, 1024),
    opacity: float | None = 0.25,
    check_existing: bool | None = True,
) -> None:
    """Export UV layout to file

        :param filepath: filepath
        :param export_all: All UVs, Export all UVs in this mesh (not just visible ones)
        :param export_tiles: Export Tiles, Choose whether to export only the [0, 1] range, or all UV tiles

    NONE
    None -- Export only UVs in the [0, 1] range.

    UDIM
    UDIM -- Export tiles in the UDIM numbering scheme: 1001 + u_tile + 10*v_tile.

    UV
    UVTILE -- Export tiles in the UVTILE numbering scheme: u(u_tile + 1)_v(v_tile + 1).
        :param modified: Modified, Exports UVs from the modified mesh
        :param mode: Format, File format to export the UV layout to

    SVG
    Scalable Vector Graphic (.svg) -- Export the UV layout to a vector SVG file.

    EPS
    Encapsulated PostScript (.eps) -- Export the UV layout to a vector EPS file.

    PNG
    PNG Image (.png) -- Export the UV layout to a bitmap image.
        :param size: Size, Dimensions of the exported file
        :param opacity: Fill Opacity, Set amount of opacity for exported UV layout
        :param check_existing: check_existing
    """

def follow_active_quads(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["EVEN", "LENGTH", "LENGTH_AVERAGE"] | None = "LENGTH_AVERAGE",
) -> None:
    """Follow UVs from active quads along continuous face loops

        :param mode: Edge Length Mode, Method to space UV edge loops

    EVEN
    Even -- Space all UVs evenly.

    LENGTH
    Length -- Average space UVs edge length of each loop.

    LENGTH_AVERAGE
    Length Average -- Average space UVs edge length of each loop.
    """

def hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Hide (un)selected UV vertices

    :param unselected: Unselected, Hide unselected rather than selected
    """

def lightmap_pack(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    PREF_CONTEXT: typing.Literal["SEL_FACES", "ALL_FACES"] | None = "SEL_FACES",
    PREF_PACK_IN_ONE: bool | None = True,
    PREF_NEW_UVLAYER: bool | None = False,
    PREF_BOX_DIV: int | None = 12,
    PREF_MARGIN_DIV: float | None = 0.1,
) -> None:
    """Pack each faces UVs into the UV bounds

        :param PREF_CONTEXT: Selection

    SEL_FACES
    Selected Faces -- Space all UVs evenly.

    ALL_FACES
    All Faces -- Average space UVs edge length of each loop.
        :param PREF_PACK_IN_ONE: Share Texture Space, Objects share texture space, map all objects into a single UV map
        :param PREF_NEW_UVLAYER: New UV Map, Create a new UV map for every mesh packed
        :param PREF_BOX_DIV: Pack Quality, Quality of the packing. Higher values will be slower but waste less space
        :param PREF_MARGIN_DIV: Margin, Size of the margin as a division of the UV
    """

def mark_seam(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
) -> None:
    """Mark selected UV edges as seams

    :param clear: Clear Seams, Clear instead of marking seams
    """

def minimize_stretch(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    fill_holes: bool | None = True,
    blend: float | None = 0.0,
    iterations: int | None = 0,
) -> None:
    """Reduce UV stretching by relaxing angles

    :param fill_holes: Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
    :param blend: Blend, Blend factor between stretch minimized and original
    :param iterations: Iterations, Number of iterations to run, 0 is unlimited when run interactively
    """

def pack_islands(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    udim_source: typing.Literal["CLOSEST_UDIM", "ACTIVE_UDIM", "ORIGINAL_AABB"]
    | None = "CLOSEST_UDIM",
    rotate: bool | None = True,
    rotate_method: typing.Literal[
        "ANY", "CARDINAL", "AXIS_ALIGNED", "AXIS_ALIGNED_X", "AXIS_ALIGNED_Y"
    ]
    | None = "ANY",
    scale: bool | None = True,
    merge_overlap: bool | None = False,
    margin_method: typing.Literal["SCALED", "ADD", "FRACTION"] | None = "SCALED",
    margin: float | None = 0.001,
    pin: bool | None = False,
    pin_method: typing.Literal["SCALE", "ROTATION", "ROTATION_SCALE", "LOCKED"]
    | None = "LOCKED",
    shape_method: typing.Literal["CONCAVE", "CONVEX", "AABB"] | None = "CONCAVE",
) -> None:
    """Transform all islands so that they fill up the UV/UDIM space as much as possible

        :param udim_source: Pack to

    CLOSEST_UDIM
    Closest UDIM -- Pack islands to closest UDIM.

    ACTIVE_UDIM
    Active UDIM -- Pack islands to active UDIM image tile or UDIM grid tile where 2D cursor is located.

    ORIGINAL_AABB
    Original bounding box -- Pack to starting bounding box of islands.
        :param rotate: Rotate, Rotate islands to improve layout
        :param rotate_method: Rotation Method

    ANY
    Any -- Any angle is allowed for rotation.

    CARDINAL
    Cardinal -- Only 90 degree rotations are allowed.

    AXIS_ALIGNED
    Axis-aligned -- Rotated to a minimal rectangle, either vertical or horizontal.

    AXIS_ALIGNED_X
    Axis-aligned (Horizontal) -- Rotate islands to be aligned horizontally.

    AXIS_ALIGNED_Y
    Axis-aligned (Vertical) -- Rotate islands to be aligned vertically.
        :param scale: Scale, Scale islands to fill unit square
        :param merge_overlap: Merge Overlapping, Overlapping islands stick together
        :param margin_method: Margin Method

    SCALED
    Scaled -- Use scale of existing UVs to multiply margin.

    ADD
    Add -- Just add the margin, ignoring any UV scale.

    FRACTION
    Fraction -- Specify a precise fraction of final UV output.
        :param margin: Margin, Space between islands
        :param pin: Lock Pinned Islands, Constrain islands containing any pinned UVs
        :param pin_method: Pin Method

    SCALE
    Scale -- Pinned islands wont rescale.

    ROTATION
    Rotation -- Pinned islands wont rotate.

    ROTATION_SCALE
    Rotation and Scale -- Pinned islands will translate only.

    LOCKED
    All -- Pinned islands are locked in place.
        :param shape_method: Shape Method

    CONCAVE
    Exact Shape (Concave) -- Uses exact geometry.

    CONVEX
    Boundary Shape (Convex) -- Uses convex hull.

    AABB
    Bounding Box -- Uses bounding boxes.
    """

def paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Paste selected UV vertices"""

def pin(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
    invert: bool | None = False,
) -> None:
    """Set/clear selected UV vertices as anchored between multiple unwrap operations

    :param clear: Clear, Clear pinning for the selection instead of setting it
    :param invert: Invert, Invert pinning for the selection instead of setting it
    """

def project_from_view(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    orthographic: bool | None = False,
    camera_bounds: bool | None = True,
    correct_aspect: bool | None = True,
    clip_to_bounds: bool | None = False,
    scale_to_bounds: bool | None = False,
) -> None:
    """Project the UV vertices of the mesh as seen in current 3D view

    :param orthographic: Orthographic, Use orthographic projection
    :param camera_bounds: Camera Bounds, Map UVs to the camera region taking resolution and aspect into account
    :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    """

def randomize_uv_transform(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    random_seed: int | None = 0,
    use_loc: bool | None = True,
    loc: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
    use_rot: bool | None = True,
    rot: float | None = 0.0,
    use_scale: bool | None = True,
    scale_even: bool | None = False,
    scale: collections.abc.Iterable[float] | None = (1.0, 1.0),
) -> None:
    """Randomize the UV islands location, rotation, and scale

    :param random_seed: Random Seed, Seed value for the random generator
    :param use_loc: Randomize Location, Randomize the location values
    :param loc: Location, Maximum distance the objects can spread over each axis
    :param use_rot: Randomize Rotation, Randomize the rotation value
    :param rot: Rotation, Maximum rotation
    :param use_scale: Randomize Scale, Randomize the scale values
    :param scale_even: Scale Even, Use the same scale value for both axes
    :param scale: Scale, Maximum scale randomization over each axis
    """

def remove_doubles(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.02,
    use_unselected: bool | None = False,
    use_shared_vertex: bool | None = False,
) -> None:
    """Selected UV vertices that are within a radius of each other are welded together

    :param threshold: Merge Distance, Maximum distance between welded vertices
    :param use_unselected: Unselected, Merge selected to other unselected vertices
    :param use_shared_vertex: Shared Vertex, Weld UVs based on shared vertices
    """

def reset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset UV projection"""

def reveal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
) -> None:
    """Reveal all hidden UV vertices

    :param select: Select
    """

def rip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Rip selected vertices or a selected region

    :param mirror: Mirror Editing
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :param use_accurate: Accurate, Use accurate transformation
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    """

def rip_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    UV_OT_rip: rip | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Unstitch UVs and move the result

    :param UV_OT_rip: UV Rip, Rip selected vertices or a selected region
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def seams_from_islands(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mark_seams: bool | None = True,
    mark_sharp: bool | None = False,
) -> None:
    """Set mesh seams according to island setup in the UV editor

    :param mark_seams: Mark Seams, Mark boundary edges as seams
    :param mark_sharp: Mark Sharp, Mark boundary edges as sharp
    """

def select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
    deselect_all: bool | None = False,
    select_passthrough: bool | None = False,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Select UV vertices

    :param extend: Extend, Extend selection instead of deselecting everything first
    :param deselect: Deselect, Remove from selection
    :param toggle: Toggle Selection, Toggle the selection
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Change selection of all UV vertices

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

def select_box(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pinned: bool | None = False,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
) -> None:
    """Select UV vertices using box selection

        :param pinned: Pinned, Border select pinned UVs only
        :param xmin: X Min
        :param xmax: X Max
        :param ymin: Y Min
        :param ymax: Y Max
        :param wait_for_input: Wait for Input
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
    """

def select_circle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    x: int | None = 0,
    y: int | None = 0,
    radius: int | None = 25,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
) -> None:
    """Select UV vertices using circle selection

        :param x: X
        :param y: Y
        :param radius: Radius
        :param wait_for_input: Wait for Input
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
    """

def select_edge_ring(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Select an edge ring of connected UV vertices

    :param extend: Extend, Extend selection rather than clearing the existing selection
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    """

def select_lasso(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_smooth_stroke: bool | None = False,
    smooth_stroke_factor: float | None = 0.75,
    smooth_stroke_radius: int | None = 35,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
) -> None:
    """Select UVs using lasso selection

        :param path: Path
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
    """

def select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Deselect UV vertices at the boundary of each selection region"""

def select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all UV vertices linked to the active UV map"""

def select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Select all UV vertices linked under the mouse

    :param extend: Extend, Extend selection rather than clearing the existing selection
    :param deselect: Deselect, Deselect linked UV vertices rather than selecting them
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    """

def select_loop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Select a loop of connected UV vertices

    :param extend: Extend, Extend selection rather than clearing the existing selection
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    """

def select_mode(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.MeshSelectModeUvItems | None = "VERTEX",
) -> None:
    """Change UV selection mode

    :param type: Type
    """

def select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select more UV vertices connected to initial selection"""

def select_overlap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Select all UV faces which overlap each other

    :param extend: Extend, Extend selection rather than clearing the existing selection
    """

def select_pinned(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all pinned UV vertices"""

def select_similar(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "PIN",
        "LENGTH",
        "LENGTH_3D",
        "AREA",
        "AREA_3D",
        "MATERIAL",
        "OBJECT",
        "SIDES",
        "WINDING",
        "FACE",
    ]
    | None = "PIN",
    compare: typing.Literal["EQUAL", "GREATER", "LESS"] | None = "EQUAL",
    threshold: float | None = 0.0,
) -> None:
    """Select similar UVs by property types

    :param type: Type
    :param compare: Compare
    :param threshold: Threshold
    """

def select_split(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select only entirely selected faces"""

def shortest_path_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_step: bool | None = False,
    use_topology_distance: bool | None = False,
    use_fill: bool | None = False,
    skip: int | None = 0,
    nth: int | None = 1,
    offset: int | None = 0,
    object_index: int | None = -1,
    index: int | None = -1,
) -> None:
    """Select shortest path between two selections

    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :param offset: Offset, Offset from the starting point
    """

def shortest_path_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_step: bool | None = False,
    use_topology_distance: bool | None = False,
    use_fill: bool | None = False,
    skip: int | None = 0,
    nth: int | None = 1,
    offset: int | None = 0,
) -> None:
    """Selected shortest path between two vertices/edges/faces

    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :param offset: Offset, Offset from the starting point
    """

def smart_project(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle_limit: float | None = 1.15192,
    margin_method: typing.Literal["SCALED", "ADD", "FRACTION"] | None = "SCALED",
    rotate_method: typing.Literal["AXIS_ALIGNED", "AXIS_ALIGNED_X", "AXIS_ALIGNED_Y"]
    | None = "AXIS_ALIGNED_Y",
    island_margin: float | None = 0.0,
    area_weight: float | None = 0.0,
    correct_aspect: bool | None = True,
    scale_to_bounds: bool | None = False,
) -> None:
    """Projection unwraps the selected faces of mesh objects

        :param angle_limit: Angle Limit, Lower for more projection groups, higher for less distortion
        :param margin_method: Margin Method

    SCALED
    Scaled -- Use scale of existing UVs to multiply margin.

    ADD
    Add -- Just add the margin, ignoring any UV scale.

    FRACTION
    Fraction -- Specify a precise fraction of final UV output.
        :param rotate_method: Rotation Method

    AXIS_ALIGNED
    Axis-aligned -- Rotated to a minimal rectangle, either vertical or horizontal.

    AXIS_ALIGNED_X
    Axis-aligned (Horizontal) -- Rotate islands to be aligned horizontally.

    AXIS_ALIGNED_Y
    Axis-aligned (Vertical) -- Rotate islands to be aligned vertically.
        :param island_margin: Island Margin, Margin to reduce bleed from adjacent islands
        :param area_weight: Area Weight, Weight projections vector by faces with larger areas
        :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account
        :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    """

def snap_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    target: typing.Literal["PIXELS", "SELECTED", "ORIGIN"] | None = "PIXELS",
) -> None:
    """Snap cursor to target type

    :param target: Target, Target to snap the selected UVs to
    """

def snap_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    target: typing.Literal["PIXELS", "CURSOR", "CURSOR_OFFSET", "ADJACENT_UNSELECTED"]
    | None = "PIXELS",
) -> None:
    """Snap selected UV vertices to target type

    :param target: Target, Target to snap the selected UVs to
    """

def sphere_project(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["VIEW_ON_EQUATOR", "VIEW_ON_POLES", "ALIGN_TO_OBJECT"]
    | None = "VIEW_ON_EQUATOR",
    align: typing.Literal["POLAR_ZX", "POLAR_ZY"] | None = "POLAR_ZX",
    pole: typing.Literal["PINCH", "FAN"] | None = "PINCH",
    seam: bool | None = False,
    correct_aspect: bool | None = True,
    clip_to_bounds: bool | None = False,
    scale_to_bounds: bool | None = False,
) -> None:
    """Project the UV vertices of the mesh over the curved surface of a sphere

        :param direction: Direction, Direction of the sphere or cylinder

    VIEW_ON_EQUATOR
    View on Equator -- 3D view is on the equator.

    VIEW_ON_POLES
    View on Poles -- 3D view is on the poles.

    ALIGN_TO_OBJECT
    Align to Object -- Align according to object transform.
        :param align: Align, How to determine rotation around the pole

    POLAR_ZX
    Polar ZX -- Polar 0 is X.

    POLAR_ZY
    Polar ZY -- Polar 0 is Y.
        :param pole: Pole, How to handle faces at the poles

    PINCH
    Pinch -- UVs are pinched at the poles.

    FAN
    Fan -- UVs are fanned at the poles.
        :param seam: Preserve Seams, Separate projections by islands isolated by seams
        :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account
        :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
        :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    """

def stitch(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_limit: bool | None = False,
    snap_islands: bool | None = True,
    limit: float | None = 0.01,
    static_island: int | None = 0,
    active_object_index: int | None = 0,
    midpoint_snap: bool | None = False,
    clear_seams: bool | None = True,
    mode: typing.Literal["VERTEX", "EDGE"] | None = "VERTEX",
    stored_mode: typing.Literal["VERTEX", "EDGE"] | None = "VERTEX",
    selection: bpy.types.bpy_prop_collection[bpy.types.SelectedUvElement] | None = None,
    objects_selection_count: collections.abc.Iterable[int] | None = (0, 0, 0, 0, 0, 0),
) -> None:
    """Stitch selected UV vertices by proximity

    :param use_limit: Use Limit, Stitch UVs within a specified limit distance
    :param snap_islands: Snap Islands, Snap islands together (on edge stitch mode, rotates the islands too)
    :param limit: Limit, Limit distance in normalized coordinates
    :param static_island: Static Island, Island that stays in place when stitching islands
    :param active_object_index: Active Object, Index of the active object
    :param midpoint_snap: Snap at Midpoint, UVs are stitched at midpoint instead of at static island
    :param clear_seams: Clear Seams, Clear seams of stitched edges
    :param mode: Operation Mode, Use vertex or edge stitching
    :param stored_mode: Stored Operation Mode, Use vertex or edge stitching
    :param selection: Selection
    :param objects_selection_count: Objects Selection Count
    """

def unwrap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    method: typing.Literal["ANGLE_BASED", "CONFORMAL", "MINIMUM_STRETCH"]
    | None = "CONFORMAL",
    fill_holes: bool | None = False,
    correct_aspect: bool | None = True,
    use_subsurf_data: bool | None = False,
    margin_method: typing.Literal["SCALED", "ADD", "FRACTION"] | None = "SCALED",
    margin: float | None = 0.001,
    no_flip: bool | None = False,
    iterations: int | None = 10,
    use_weights: bool | None = False,
    weight_group: str = "uv_importance",
    weight_factor: float | None = 1.0,
) -> None:
    """Unwrap the mesh of the object being edited

        :param method: Method, Unwrapping method (Angle Based usually gives better results than Conformal, while being somewhat slower)
        :param fill_holes: Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
        :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account
        :param use_subsurf_data: Use Subdivision Surface, Map UVs taking vertex position after Subdivision Surface modifier has been applied
        :param margin_method: Margin Method

    SCALED
    Scaled -- Use scale of existing UVs to multiply margin.

    ADD
    Add -- Just add the margin, ignoring any UV scale.

    FRACTION
    Fraction -- Specify a precise fraction of final UV output.
        :param margin: Margin, Space between islands
        :param no_flip: No Flip, Prevent flipping UVs, flipping may lower distortion depending on the position of pins
        :param iterations: Iterations, Number of iterations when "Minimum Stretch" method is used
        :param use_weights: Importance Weights, Whether to take into account per-vertex importance weights
        :param weight_group: Weight Group, Vertex group name for importance weights (modulating the deform)
        :param weight_factor: Weight Factor, How much influence the weightmap has for weighted parameterization, 0 being no influence
    """

def weld(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Weld selected UV vertices together"""
