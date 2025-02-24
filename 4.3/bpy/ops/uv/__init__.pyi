import typing
import collections.abc
import typing_extensions
import bpy._typing.rna_enums
import bpy.ops.transform
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
):
    """Aligns selected UV vertices on a line

        :type execution_context: int | str | None
        :type undo: bool | None
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
        :type axis: typing.Literal['ALIGN_S','ALIGN_T','ALIGN_U','ALIGN_AUTO','ALIGN_X','ALIGN_Y'] | None
    """

def align_rotation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    method: typing.Literal["AUTO", "EDGE", "GEOMETRY"] | None = "AUTO",
    axis: typing.Literal["X", "Y", "Z"] | None = "X",
    correct_aspect: bool | None = False,
):
    """Align the UV island's rotation

        :type execution_context: int | str | None
        :type undo: bool | None
        :param method: Method, Method to calculate rotation angle

    AUTO
    Auto -- Align from all edges.

    EDGE
    Edge -- Only selected edges.

    GEOMETRY
    Geometry -- Align to Geometry axis.
        :type method: typing.Literal['AUTO','EDGE','GEOMETRY'] | None
        :param axis: Axis, Axis to align to

    X
    X -- X axis.

    Y
    Y -- Y axis.

    Z
    Z -- Z axis.
        :type axis: typing.Literal['X','Y','Z'] | None
        :param correct_aspect: Correct Aspect, Take image aspect ratio into account
        :type correct_aspect: bool | None
    """

def average_islands_scale(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    scale_uv: bool | None = False,
    shear: bool | None = False,
):
    """Average the size of separate UV islands, based on their area in 3D space

    :type execution_context: int | str | None
    :type undo: bool | None
    :param scale_uv: Non-Uniform, Scale U and V independently
    :type scale_uv: bool | None
    :param shear: Shear, Reduce shear within islands
    :type shear: bool | None
    """

def copy(execution_context: int | str | None = None, undo: bool | None = None):
    """Copy selected UV vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def cube_project(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    cube_size: float | None = 1.0,
    correct_aspect: bool | None = True,
    clip_to_bounds: bool | None = False,
    scale_to_bounds: bool | None = False,
):
    """Project the UV vertices of the mesh over the six faces of a cube

    :type execution_context: int | str | None
    :type undo: bool | None
    :param cube_size: Cube Size, Size of the cube to project on
    :type cube_size: float | None
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: bool | None
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :type clip_to_bounds: bool | None
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: bool | None
    """

def cursor_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Set 2D cursor location

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Cursor location in normalized (0.0 to 1.0) coordinates
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
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
):
    """Project the UV vertices of the mesh over the curved wall of a cylinder

        :type execution_context: int | str | None
        :type undo: bool | None
        :param direction: Direction, Direction of the sphere or cylinder

    VIEW_ON_EQUATOR
    View on Equator -- 3D view is on the equator.

    VIEW_ON_POLES
    View on Poles -- 3D view is on the poles.

    ALIGN_TO_OBJECT
    Align to Object -- Align according to object transform.
        :type direction: typing.Literal['VIEW_ON_EQUATOR','VIEW_ON_POLES','ALIGN_TO_OBJECT'] | None
        :param align: Align, How to determine rotation around the pole

    POLAR_ZX
    Polar ZX -- Polar 0 is X.

    POLAR_ZY
    Polar ZY -- Polar 0 is Y.
        :type align: typing.Literal['POLAR_ZX','POLAR_ZY'] | None
        :param pole: Pole, How to handle faces at the poles

    PINCH
    Pinch -- UVs are pinched at the poles.

    FAN
    Fan -- UVs are fanned at the poles.
        :type pole: typing.Literal['PINCH','FAN'] | None
        :param seam: Preserve Seams, Separate projections by islands isolated by seams
        :type seam: bool | None
        :param radius: Radius, Radius of the sphere or cylinder
        :type radius: float | None
        :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        :type correct_aspect: bool | None
        :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
        :type clip_to_bounds: bool | None
        :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
        :type scale_to_bounds: bool | None
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
):
    """Export UV layout to file

        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: filepath
        :type filepath: str
        :param export_all: All UVs, Export all UVs in this mesh (not just visible ones)
        :type export_all: bool | None
        :param export_tiles: Export Tiles, Choose whether to export only the [0, 1] range, or all UV tiles

    NONE
    None -- Export only UVs in the [0, 1] range.

    UDIM
    UDIM -- Export tiles in the UDIM numbering scheme: 1001 + u_tile + 10*v_tile.

    UV
    UVTILE -- Export tiles in the UVTILE numbering scheme: u(u_tile + 1)_v(v_tile + 1).
        :type export_tiles: typing.Literal['NONE','UDIM','UV'] | None
        :param modified: Modified, Exports UVs from the modified mesh
        :type modified: bool | None
        :param mode: Format, File format to export the UV layout to

    SVG
    Scalable Vector Graphic (.svg) -- Export the UV layout to a vector SVG file.

    EPS
    Encapsulated PostScript (.eps) -- Export the UV layout to a vector EPS file.

    PNG
    PNG Image (.png) -- Export the UV layout to a bitmap image.
        :type mode: typing.Literal['SVG','EPS','PNG'] | None
        :param size: Size, Dimensions of the exported file
        :type size: collections.abc.Iterable[int] | None
        :param opacity: Fill Opacity, Set amount of opacity for exported UV layout
        :type opacity: float | None
        :param check_existing: check_existing
        :type check_existing: bool | None
    """

def follow_active_quads(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["EVEN", "LENGTH", "LENGTH_AVERAGE"] | None = "LENGTH_AVERAGE",
):
    """Follow UVs from active quads along continuous face loops

        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Edge Length Mode, Method to space UV edge loops

    EVEN
    Even -- Space all UVs evenly.

    LENGTH
    Length -- Average space UVs edge length of each loop.

    LENGTH_AVERAGE
    Length Average -- Average space UVs edge length of each loop.
        :type mode: typing.Literal['EVEN','LENGTH','LENGTH_AVERAGE'] | None
    """

def hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
):
    """Hide (un)selected UV vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: bool | None
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
):
    """Pack each face's UVs into the UV bounds

        :type execution_context: int | str | None
        :type undo: bool | None
        :param PREF_CONTEXT: Selection

    SEL_FACES
    Selected Faces -- Space all UVs evenly.

    ALL_FACES
    All Faces -- Average space UVs edge length of each loop.
        :type PREF_CONTEXT: typing.Literal['SEL_FACES','ALL_FACES'] | None
        :param PREF_PACK_IN_ONE: Share Texture Space, Objects share texture space, map all objects into a single UV map
        :type PREF_PACK_IN_ONE: bool | None
        :param PREF_NEW_UVLAYER: New UV Map, Create a new UV map for every mesh packed
        :type PREF_NEW_UVLAYER: bool | None
        :param PREF_BOX_DIV: Pack Quality, Quality of the packing. Higher values will be slower but waste less space
        :type PREF_BOX_DIV: int | None
        :param PREF_MARGIN_DIV: Margin, Size of the margin as a division of the UV
        :type PREF_MARGIN_DIV: float | None
    """

def mark_seam(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
):
    """Mark selected UV edges as seams

    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear Seams, Clear instead of marking seams
    :type clear: bool | None
    """

def minimize_stretch(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    fill_holes: bool | None = True,
    blend: float | None = 0.0,
    iterations: int | None = 0,
):
    """Reduce UV stretching by relaxing angles

    :type execution_context: int | str | None
    :type undo: bool | None
    :param fill_holes: Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
    :type fill_holes: bool | None
    :param blend: Blend, Blend factor between stretch minimized and original
    :type blend: float | None
    :param iterations: Iterations, Number of iterations to run, 0 is unlimited when run interactively
    :type iterations: int | None
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
):
    """Transform all islands so that they fill up the UV/UDIM space as much as possible

        :type execution_context: int | str | None
        :type undo: bool | None
        :param udim_source: Pack to

    CLOSEST_UDIM
    Closest UDIM -- Pack islands to closest UDIM.

    ACTIVE_UDIM
    Active UDIM -- Pack islands to active UDIM image tile or UDIM grid tile where 2D cursor is located.

    ORIGINAL_AABB
    Original bounding box -- Pack to starting bounding box of islands.
        :type udim_source: typing.Literal['CLOSEST_UDIM','ACTIVE_UDIM','ORIGINAL_AABB'] | None
        :param rotate: Rotate, Rotate islands to improve layout
        :type rotate: bool | None
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
        :type rotate_method: typing.Literal['ANY','CARDINAL','AXIS_ALIGNED','AXIS_ALIGNED_X','AXIS_ALIGNED_Y'] | None
        :param scale: Scale, Scale islands to fill unit square
        :type scale: bool | None
        :param merge_overlap: Merge Overlapping, Overlapping islands stick together
        :type merge_overlap: bool | None
        :param margin_method: Margin Method

    SCALED
    Scaled -- Use scale of existing UVs to multiply margin.

    ADD
    Add -- Just add the margin, ignoring any UV scale.

    FRACTION
    Fraction -- Specify a precise fraction of final UV output.
        :type margin_method: typing.Literal['SCALED','ADD','FRACTION'] | None
        :param margin: Margin, Space between islands
        :type margin: float | None
        :param pin: Lock Pinned Islands, Constrain islands containing any pinned UV's
        :type pin: bool | None
        :param pin_method: Pin Method

    SCALE
    Scale -- Pinned islands won't rescale.

    ROTATION
    Rotation -- Pinned islands won't rotate.

    ROTATION_SCALE
    Rotation and Scale -- Pinned islands will translate only.

    LOCKED
    All -- Pinned islands are locked in place.
        :type pin_method: typing.Literal['SCALE','ROTATION','ROTATION_SCALE','LOCKED'] | None
        :param shape_method: Shape Method

    CONCAVE
    Exact Shape (Concave) -- Uses exact geometry.

    CONVEX
    Boundary Shape (Convex) -- Uses convex hull.

    AABB
    Bounding Box -- Uses bounding boxes.
        :type shape_method: typing.Literal['CONCAVE','CONVEX','AABB'] | None
    """

def paste(execution_context: int | str | None = None, undo: bool | None = None):
    """Paste selected UV vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def pin(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
    invert: bool | None = False,
):
    """Set/clear selected UV vertices as anchored between multiple unwrap operations

    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear, Clear pinning for the selection instead of setting it
    :type clear: bool | None
    :param invert: Invert, Invert pinning for the selection instead of setting it
    :type invert: bool | None
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
):
    """Project the UV vertices of the mesh as seen in current 3D view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param orthographic: Orthographic, Use orthographic projection
    :type orthographic: bool | None
    :param camera_bounds: Camera Bounds, Map UVs to the camera region taking resolution and aspect into account
    :type camera_bounds: bool | None
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: bool | None
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :type clip_to_bounds: bool | None
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: bool | None
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
):
    """Randomize the UV island's location, rotation, and scale

    :type execution_context: int | str | None
    :type undo: bool | None
    :param random_seed: Random Seed, Seed value for the random generator
    :type random_seed: int | None
    :param use_loc: Randomize Location, Randomize the location values
    :type use_loc: bool | None
    :param loc: Location, Maximum distance the objects can spread over each axis
    :type loc: collections.abc.Sequence[float] | mathutils.Vector | None
    :param use_rot: Randomize Rotation, Randomize the rotation value
    :type use_rot: bool | None
    :param rot: Rotation, Maximum rotation
    :type rot: float | None
    :param use_scale: Randomize Scale, Randomize the scale values
    :type use_scale: bool | None
    :param scale_even: Scale Even, Use the same scale value for both axes
    :type scale_even: bool | None
    :param scale: Scale, Maximum scale randomization over each axis
    :type scale: collections.abc.Iterable[float] | None
    """

def remove_doubles(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.02,
    use_unselected: bool | None = False,
    use_shared_vertex: bool | None = False,
):
    """Selected UV vertices that are within a radius of each other are welded together

    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Merge Distance, Maximum distance between welded vertices
    :type threshold: float | None
    :param use_unselected: Unselected, Merge selected to other unselected vertices
    :type use_unselected: bool | None
    :param use_shared_vertex: Shared Vertex, Weld UVs based on shared vertices
    :type use_shared_vertex: bool | None
    """

def reset(execution_context: int | str | None = None, undo: bool | None = None):
    """Reset UV projection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def reveal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
):
    """Reveal all hidden UV vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | None
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
):
    """Rip selected vertices or a selected region

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | None
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def rip_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    UV_OT_rip: rip | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Unstitch UVs and move the result

    :type execution_context: int | str | None
    :type undo: bool | None
    :param UV_OT_rip: UV Rip, Rip selected vertices or a selected region
    :type UV_OT_rip: rip | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def seams_from_islands(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mark_seams: bool | None = True,
    mark_sharp: bool | None = False,
):
    """Set mesh seams according to island setup in the UV editor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mark_seams: Mark Seams, Mark boundary edges as seams
    :type mark_seams: bool | None
    :param mark_sharp: Mark Sharp, Mark boundary edges as sharp
    :type mark_sharp: bool | None
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
):
    """Select UV vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
    :param deselect: Deselect, Remove from selection
    :type deselect: bool | None
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: bool | None
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool | None
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: bool | None
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Change selection of all UV vertices

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
):
    """Select UV vertices using box selection

        :type execution_context: int | str | None
        :type undo: bool | None
        :param pinned: Pinned, Border select pinned UVs only
        :type pinned: bool | None
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
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
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
):
    """Select UV vertices using circle selection

        :type execution_context: int | str | None
        :type undo: bool | None
        :param x: X
        :type x: int | None
        :param y: Y
        :type y: int | None
        :param radius: Radius
        :type radius: int | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
    """

def select_edge_ring(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Select an edge ring of connected UV vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | None
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
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
):
    """Select UVs using lasso selection

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
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
    """

def select_less(execution_context: int | str | None = None, undo: bool | None = None):
    """Deselect UV vertices at the boundary of each selection region

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked(execution_context: int | str | None = None, undo: bool | None = None):
    """Select all UV vertices linked to the active UV map

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Select all UV vertices linked under the mouse

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | None
    :param deselect: Deselect, Deselect linked UV vertices rather than selecting them
    :type deselect: bool | None
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def select_loop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
):
    """Select a loop of connected UV vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | None
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def select_mode(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy._typing.rna_enums.MeshSelectModeUvItems | None = "VERTEX",
):
    """Change UV selection mode

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy._typing.rna_enums.MeshSelectModeUvItems | None
    """

def select_more(execution_context: int | str | None = None, undo: bool | None = None):
    """Select more UV vertices connected to initial selection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_overlap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
):
    """Select all UV faces which overlap each other

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | None
    """

def select_pinned(execution_context: int | str | None = None, undo: bool | None = None):
    """Select all pinned UV vertices

    :type execution_context: int | str | None
    :type undo: bool | None
    """

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
):
    """Select similar UVs by property types

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['PIN','LENGTH','LENGTH_3D','AREA','AREA_3D','MATERIAL','OBJECT','SIDES','WINDING','FACE'] | None
    :param compare: Compare
    :type compare: typing.Literal['EQUAL','GREATER','LESS'] | None
    :param threshold: Threshold
    :type threshold: float | None
    """

def select_split(execution_context: int | str | None = None, undo: bool | None = None):
    """Select only entirely selected faces

    :type execution_context: int | str | None
    :type undo: bool | None
    """

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
):
    """Select shortest path between two selections

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: bool | None
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: bool | None
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: bool | None
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: int | None
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: int | None
    :param offset: Offset, Offset from the starting point
    :type offset: int | None
    :type object_index: int | None
    :type index: int | None
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
):
    """Selected shortest path between two vertices/edges/faces

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: bool | None
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: bool | None
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: bool | None
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: int | None
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: int | None
    :param offset: Offset, Offset from the starting point
    :type offset: int | None
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
):
    """Projection unwraps the selected faces of mesh objects

        :type execution_context: int | str | None
        :type undo: bool | None
        :param angle_limit: Angle Limit, Lower for more projection groups, higher for less distortion
        :type angle_limit: float | None
        :param margin_method: Margin Method

    SCALED
    Scaled -- Use scale of existing UVs to multiply margin.

    ADD
    Add -- Just add the margin, ignoring any UV scale.

    FRACTION
    Fraction -- Specify a precise fraction of final UV output.
        :type margin_method: typing.Literal['SCALED','ADD','FRACTION'] | None
        :param rotate_method: Rotation Method

    AXIS_ALIGNED
    Axis-aligned -- Rotated to a minimal rectangle, either vertical or horizontal.

    AXIS_ALIGNED_X
    Axis-aligned (Horizontal) -- Rotate islands to be aligned horizontally.

    AXIS_ALIGNED_Y
    Axis-aligned (Vertical) -- Rotate islands to be aligned vertically.
        :type rotate_method: typing.Literal['AXIS_ALIGNED','AXIS_ALIGNED_X','AXIS_ALIGNED_Y'] | None
        :param island_margin: Island Margin, Margin to reduce bleed from adjacent islands
        :type island_margin: float | None
        :param area_weight: Area Weight, Weight projection's vector by faces with larger areas
        :type area_weight: float | None
        :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        :type correct_aspect: bool | None
        :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
        :type scale_to_bounds: bool | None
    """

def snap_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    target: typing.Literal["PIXELS", "SELECTED", "ORIGIN"] | None = "PIXELS",
):
    """Snap cursor to target type

    :type execution_context: int | str | None
    :type undo: bool | None
    :param target: Target, Target to snap the selected UVs to
    :type target: typing.Literal['PIXELS','SELECTED','ORIGIN'] | None
    """

def snap_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    target: typing.Literal["PIXELS", "CURSOR", "CURSOR_OFFSET", "ADJACENT_UNSELECTED"]
    | None = "PIXELS",
):
    """Snap selected UV vertices to target type

    :type execution_context: int | str | None
    :type undo: bool | None
    :param target: Target, Target to snap the selected UVs to
    :type target: typing.Literal['PIXELS','CURSOR','CURSOR_OFFSET','ADJACENT_UNSELECTED'] | None
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
):
    """Project the UV vertices of the mesh over the curved surface of a sphere

        :type execution_context: int | str | None
        :type undo: bool | None
        :param direction: Direction, Direction of the sphere or cylinder

    VIEW_ON_EQUATOR
    View on Equator -- 3D view is on the equator.

    VIEW_ON_POLES
    View on Poles -- 3D view is on the poles.

    ALIGN_TO_OBJECT
    Align to Object -- Align according to object transform.
        :type direction: typing.Literal['VIEW_ON_EQUATOR','VIEW_ON_POLES','ALIGN_TO_OBJECT'] | None
        :param align: Align, How to determine rotation around the pole

    POLAR_ZX
    Polar ZX -- Polar 0 is X.

    POLAR_ZY
    Polar ZY -- Polar 0 is Y.
        :type align: typing.Literal['POLAR_ZX','POLAR_ZY'] | None
        :param pole: Pole, How to handle faces at the poles

    PINCH
    Pinch -- UVs are pinched at the poles.

    FAN
    Fan -- UVs are fanned at the poles.
        :type pole: typing.Literal['PINCH','FAN'] | None
        :param seam: Preserve Seams, Separate projections by islands isolated by seams
        :type seam: bool | None
        :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        :type correct_aspect: bool | None
        :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
        :type clip_to_bounds: bool | None
        :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
        :type scale_to_bounds: bool | None
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
):
    """Stitch selected UV vertices by proximity

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_limit: Use Limit, Stitch UVs within a specified limit distance
    :type use_limit: bool | None
    :param snap_islands: Snap Islands, Snap islands together (on edge stitch mode, rotates the islands too)
    :type snap_islands: bool | None
    :param limit: Limit, Limit distance in normalized coordinates
    :type limit: float | None
    :param static_island: Static Island, Island that stays in place when stitching islands
    :type static_island: int | None
    :param active_object_index: Active Object, Index of the active object
    :type active_object_index: int | None
    :param midpoint_snap: Snap at Midpoint, UVs are stitched at midpoint instead of at static island
    :type midpoint_snap: bool | None
    :param clear_seams: Clear Seams, Clear seams of stitched edges
    :type clear_seams: bool | None
    :param mode: Operation Mode, Use vertex or edge stitching
    :type mode: typing.Literal['VERTEX','EDGE'] | None
    :param stored_mode: Stored Operation Mode, Use vertex or edge stitching
    :type stored_mode: typing.Literal['VERTEX','EDGE'] | None
    :param selection: Selection
    :type selection: bpy.types.bpy_prop_collection[bpy.types.SelectedUvElement] | None
    :param objects_selection_count: Objects Selection Count
    :type objects_selection_count: collections.abc.Iterable[int] | None
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
):
    """Unwrap the mesh of the object being edited

        :type execution_context: int | str | None
        :type undo: bool | None
        :param method: Method, Unwrapping method (Angle Based usually gives better results than Conformal, while being somewhat slower)
        :type method: typing.Literal['ANGLE_BASED','CONFORMAL','MINIMUM_STRETCH'] | None
        :param fill_holes: Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
        :type fill_holes: bool | None
        :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        :type correct_aspect: bool | None
        :param use_subsurf_data: Use Subdivision Surface, Map UVs taking vertex position after Subdivision Surface modifier has been applied
        :type use_subsurf_data: bool | None
        :param margin_method: Margin Method

    SCALED
    Scaled -- Use scale of existing UVs to multiply margin.

    ADD
    Add -- Just add the margin, ignoring any UV scale.

    FRACTION
    Fraction -- Specify a precise fraction of final UV output.
        :type margin_method: typing.Literal['SCALED','ADD','FRACTION'] | None
        :param margin: Margin, Space between islands
        :type margin: float | None
        :param no_flip: No Flip, Prevent flipping UV's, flipping may lower distortion depending on the position of pins
        :type no_flip: bool | None
        :param iterations: Iterations, Number of iterations when "Minimum Stretch" method is used
        :type iterations: int | None
        :param use_weights: Importance Weights, Whether to take into account per-vertex importance weights
        :type use_weights: bool | None
        :param weight_group: Weight Group, Vertex group name for importance weights (modulating the deform)
        :type weight_group: str
        :param weight_factor: Weight Factor, How much influence the weightmap has for weighted parameterization, 0 being no influence
        :type weight_factor: float | None
    """

def weld(execution_context: int | str | None = None, undo: bool | None = None):
    """Weld selected UV vertices together

    :type execution_context: int | str | None
    :type undo: bool | None
    """
