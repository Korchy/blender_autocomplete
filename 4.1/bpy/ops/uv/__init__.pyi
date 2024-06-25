import typing
import collections.abc
import bpy.ops.transform
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def align(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    axis: str | None = "ALIGN_AUTO",
):
    """Aligns selected UV vertices on a line

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
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
        :type axis: str | None
    """

    ...

def align_rotation(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    method: str | None = "AUTO",
    axis: str | None = "X",
    correct_aspect: bool | typing.Any | None = False,
):
    """Align the UV island's rotation

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param method: Method, Method to calculate rotation angle

    AUTO
    Auto -- Align from all edges.

    EDGE
    Edge -- Only selected edges.

    GEOMETRY
    Geometry -- Align to Geometry axis.
        :type method: str | None
        :param axis: Axis, Axis to align to

    X
    X -- X axis.

    Y
    Y -- Y axis.

    Z
    Z -- Z axis.
        :type axis: str | None
        :param correct_aspect: Correct Aspect, Take image aspect ratio into account
        :type correct_aspect: bool | typing.Any | None
    """

    ...

def average_islands_scale(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    scale_uv: bool | typing.Any | None = False,
    shear: bool | typing.Any | None = False,
):
    """Average the size of separate UV islands, based on their area in 3D space

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param scale_uv: Non-Uniform, Scale U and V independently
    :type scale_uv: bool | typing.Any | None
    :param shear: Shear, Reduce shear within islands
    :type shear: bool | typing.Any | None
    """

    ...

def copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy selected UV vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def cube_project(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    cube_size: typing.Any | None = 1.0,
    correct_aspect: bool | typing.Any | None = True,
    clip_to_bounds: bool | typing.Any | None = False,
    scale_to_bounds: bool | typing.Any | None = False,
):
    """Project the UV vertices of the mesh over the six faces of a cube

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param cube_size: Cube Size, Size of the cube to project on
    :type cube_size: typing.Any | None
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: bool | typing.Any | None
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :type clip_to_bounds: bool | typing.Any | None
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: bool | typing.Any | None
    """

    ...

def cursor_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    location: typing.Any | None = (0.0, 0.0),
):
    """Set 2D cursor location

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Cursor location in normalized (0.0 to 1.0) coordinates
    :type location: typing.Any | None
    """

    ...

def cylinder_project(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: str | None = "VIEW_ON_EQUATOR",
    align: str | None = "POLAR_ZX",
    pole: str | None = "PINCH",
    seam: bool | typing.Any | None = False,
    radius: typing.Any | None = 1.0,
    correct_aspect: bool | typing.Any | None = True,
    clip_to_bounds: bool | typing.Any | None = False,
    scale_to_bounds: bool | typing.Any | None = False,
):
    """Project the UV vertices of the mesh over the curved wall of a cylinder

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param direction: Direction, Direction of the sphere or cylinder

    VIEW_ON_EQUATOR
    View on Equator -- 3D view is on the equator.

    VIEW_ON_POLES
    View on Poles -- 3D view is on the poles.

    ALIGN_TO_OBJECT
    Align to Object -- Align according to object transform.
        :type direction: str | None
        :param align: Align, How to determine rotation around the pole

    POLAR_ZX
    Polar ZX -- Polar 0 is X.

    POLAR_ZY
    Polar ZY -- Polar 0 is Y.
        :type align: str | None
        :param pole: Pole, How to handle faces at the poles

    PINCH
    Pinch -- UVs are pinched at the poles.

    FAN
    Fan -- UVs are fanned at the poles.
        :type pole: str | None
        :param seam: Preserve Seams, Separate projections by islands isolated by seams
        :type seam: bool | typing.Any | None
        :param radius: Radius, Radius of the sphere or cylinder
        :type radius: typing.Any | None
        :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        :type correct_aspect: bool | typing.Any | None
        :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
        :type clip_to_bounds: bool | typing.Any | None
        :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
        :type scale_to_bounds: bool | typing.Any | None
    """

    ...

def export_layout(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    export_all: bool | typing.Any | None = False,
    export_tiles: str | None = "NONE",
    modified: bool | typing.Any | None = False,
    mode: str | None = "PNG",
    size: typing.Any | None = (1024, 1024),
    opacity: typing.Any | None = 0.25,
    check_existing: bool | typing.Any | None = True,
):
    """Export UV layout to file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: filepath
        :type filepath: str | typing.Any
        :param export_all: All UVs, Export all UVs in this mesh (not just visible ones)
        :type export_all: bool | typing.Any | None
        :param export_tiles: Export Tiles, Choose whether to export only the [0, 1] range, or all UV tiles

    NONE
    None -- Export only UVs in the [0, 1] range.

    UDIM
    UDIM -- Export tiles in the UDIM numbering scheme: 1001 + u_tile + 10*v_tile.

    UV
    UVTILE -- Export tiles in the UVTILE numbering scheme: u(u_tile + 1)_v(v_tile + 1).
        :type export_tiles: str | None
        :param modified: Modified, Exports UVs from the modified mesh
        :type modified: bool | typing.Any | None
        :param mode: Format, File format to export the UV layout to

    SVG
    Scalable Vector Graphic (.svg) -- Export the UV layout to a vector SVG file.

    EPS
    Encapsulated PostScript (.eps) -- Export the UV layout to a vector EPS file.

    PNG
    PNG Image (.png) -- Export the UV layout to a bitmap image.
        :type mode: str | None
        :param size: Size, Dimensions of the exported file
        :type size: typing.Any | None
        :param opacity: Fill Opacity, Set amount of opacity for exported UV layout
        :type opacity: typing.Any | None
        :param check_existing: check_existing
        :type check_existing: bool | typing.Any | None
    """

    ...

def follow_active_quads(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "LENGTH_AVERAGE",
):
    """Follow UVs from active quads along continuous face loops

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Edge Length Mode, Method to space UV edge loops

    EVEN
    Even -- Space all UVs evenly.

    LENGTH
    Length -- Average space UVs edge length of each loop.

    LENGTH_AVERAGE
    Length Average -- Average space UVs edge length of each loop.
        :type mode: str | None
    """

    ...

def hide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | typing.Any | None = False,
):
    """Hide (un)selected UV vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: bool | typing.Any | None
    """

    ...

def lightmap_pack(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    PREF_CONTEXT: str | None = "SEL_FACES",
    PREF_PACK_IN_ONE: bool | typing.Any | None = True,
    PREF_NEW_UVLAYER: bool | typing.Any | None = False,
    PREF_BOX_DIV: typing.Any | None = 12,
    PREF_MARGIN_DIV: typing.Any | None = 0.1,
):
    """Pack each face's UVs into the UV bounds

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param PREF_CONTEXT: Selection

    SEL_FACES
    Selected Faces -- Space all UVs evenly.

    ALL_FACES
    All Faces -- Average space UVs edge length of each loop.
        :type PREF_CONTEXT: str | None
        :param PREF_PACK_IN_ONE: Share Texture Space, Objects share texture space, map all objects into a single UV map
        :type PREF_PACK_IN_ONE: bool | typing.Any | None
        :param PREF_NEW_UVLAYER: New UV Map, Create a new UV map for every mesh packed
        :type PREF_NEW_UVLAYER: bool | typing.Any | None
        :param PREF_BOX_DIV: Pack Quality, Quality of the packing. Higher values will be slower but waste less space
        :type PREF_BOX_DIV: typing.Any | None
        :param PREF_MARGIN_DIV: Margin, Size of the margin as a division of the UV
        :type PREF_MARGIN_DIV: typing.Any | None
    """

    ...

def mark_seam(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    clear: bool | typing.Any | None = False,
):
    """Mark selected UV edges as seams

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear Seams, Clear instead of marking seams
    :type clear: bool | typing.Any | None
    """

    ...

def minimize_stretch(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    fill_holes: bool | typing.Any | None = True,
    blend: typing.Any | None = 0.0,
    iterations: typing.Any | None = 0,
):
    """Reduce UV stretching by relaxing angles

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param fill_holes: Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
    :type fill_holes: bool | typing.Any | None
    :param blend: Blend, Blend factor between stretch minimized and original
    :type blend: typing.Any | None
    :param iterations: Iterations, Number of iterations to run, 0 is unlimited when run interactively
    :type iterations: typing.Any | None
    """

    ...

def pack_islands(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    udim_source: str | None = "CLOSEST_UDIM",
    rotate: bool | typing.Any | None = True,
    rotate_method: str | None = "ANY",
    scale: bool | typing.Any | None = True,
    merge_overlap: bool | typing.Any | None = False,
    margin_method: str | None = "SCALED",
    margin: typing.Any | None = 0.001,
    pin: bool | typing.Any | None = False,
    pin_method: str | None = "LOCKED",
    shape_method: str | None = "CONCAVE",
):
    """Transform all islands so that they fill up the UV/UDIM space as much as possible

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param udim_source: Pack to

    CLOSEST_UDIM
    Closest UDIM -- Pack islands to closest UDIM.

    ACTIVE_UDIM
    Active UDIM -- Pack islands to active UDIM image tile or UDIM grid tile where 2D cursor is located.

    ORIGINAL_AABB
    Original bounding box -- Pack to starting bounding box of islands.
        :type udim_source: str | None
        :param rotate: Rotate, Rotate islands to improve layout
        :type rotate: bool | typing.Any | None
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
        :type rotate_method: str | None
        :param scale: Scale, Scale islands to fill unit square
        :type scale: bool | typing.Any | None
        :param merge_overlap: Merge Overlapping, Overlapping islands stick together
        :type merge_overlap: bool | typing.Any | None
        :param margin_method: Margin Method

    SCALED
    Scaled -- Use scale of existing UVs to multiply margin.

    ADD
    Add -- Just add the margin, ignoring any UV scale.

    FRACTION
    Fraction -- Specify a precise fraction of final UV output.
        :type margin_method: str | None
        :param margin: Margin, Space between islands
        :type margin: typing.Any | None
        :param pin: Lock Pinned Islands, Constrain islands containing any pinned UV's
        :type pin: bool | typing.Any | None
        :param pin_method: Pin Method

    SCALE
    Scale -- Pinned islands won't rescale.

    ROTATION
    Rotation -- Pinned islands won't rotate.

    ROTATION_SCALE
    Rotation and Scale -- Pinned islands will translate only.

    LOCKED
    All -- Pinned islands are locked in place.
        :type pin_method: str | None
        :param shape_method: Shape Method

    CONCAVE
    Exact Shape (Concave) -- Uses exact geometry.

    CONVEX
    Boundary Shape (Convex) -- Uses convex hull.

    AABB
    Bounding Box -- Uses bounding boxes.
        :type shape_method: str | None
    """

    ...

def paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Paste selected UV vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def pin(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    clear: bool | typing.Any | None = False,
    invert: bool | typing.Any | None = False,
):
    """Set/clear selected UV vertices as anchored between multiple unwrap operations

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear, Clear pinning for the selection instead of setting it
    :type clear: bool | typing.Any | None
    :param invert: Invert, Invert pinning for the selection instead of setting it
    :type invert: bool | typing.Any | None
    """

    ...

def project_from_view(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    orthographic: bool | typing.Any | None = False,
    camera_bounds: bool | typing.Any | None = True,
    correct_aspect: bool | typing.Any | None = True,
    clip_to_bounds: bool | typing.Any | None = False,
    scale_to_bounds: bool | typing.Any | None = False,
):
    """Project the UV vertices of the mesh as seen in current 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param orthographic: Orthographic, Use orthographic projection
    :type orthographic: bool | typing.Any | None
    :param camera_bounds: Camera Bounds, Map UVs to the camera region taking resolution and aspect into account
    :type camera_bounds: bool | typing.Any | None
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: bool | typing.Any | None
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :type clip_to_bounds: bool | typing.Any | None
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: bool | typing.Any | None
    """

    ...

def randomize_uv_transform(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    random_seed: typing.Any | None = 0,
    use_loc: bool | typing.Any | None = True,
    loc: typing.Any | None = (0.0, 0.0),
    use_rot: bool | typing.Any | None = True,
    rot: typing.Any | None = 0.0,
    use_scale: bool | typing.Any | None = True,
    scale_even: bool | typing.Any | None = False,
    scale: typing.Any | None = (1.0, 1.0),
):
    """Randomize the UV island's location, rotation, and scale

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param random_seed: Random Seed, Seed value for the random generator
    :type random_seed: typing.Any | None
    :param use_loc: Randomize Location, Randomize the location values
    :type use_loc: bool | typing.Any | None
    :param loc: Location, Maximum distance the objects can spread over each axis
    :type loc: typing.Any | None
    :param use_rot: Randomize Rotation, Randomize the rotation value
    :type use_rot: bool | typing.Any | None
    :param rot: Rotation, Maximum rotation
    :type rot: typing.Any | None
    :param use_scale: Randomize Scale, Randomize the scale values
    :type use_scale: bool | typing.Any | None
    :param scale_even: Scale Even, Use the same scale value for both axes
    :type scale_even: bool | typing.Any | None
    :param scale: Scale, Maximum scale randomization over each axis
    :type scale: typing.Any | None
    """

    ...

def remove_doubles(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    threshold: typing.Any | None = 0.02,
    use_unselected: bool | typing.Any | None = False,
):
    """Selected UV vertices that are within a radius of each other are welded together

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Merge Distance, Maximum distance between welded vertices
    :type threshold: typing.Any | None
    :param use_unselected: Unselected, Merge selected to other unselected vertices
    :type use_unselected: bool | typing.Any | None
    """

    ...

def reset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset UV projection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select: bool | typing.Any | None = True,
):
    """Reveal all hidden UV vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | typing.Any | None
    """

    ...

def rip(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mirror: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
    use_accurate: bool | typing.Any | None = False,
    location: typing.Any | None = (0.0, 0.0),
):
    """Rip selected vertices or a selected region

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | typing.Any | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | typing.Any | None
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool | typing.Any | None
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: typing.Any | None
    """

    ...

def rip_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    UV_OT_rip: rip | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Unstitch UVs and move the result

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param UV_OT_rip: UV Rip, Rip selected vertices or a selected region
    :type UV_OT_rip: rip | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def seams_from_islands(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mark_seams: bool | typing.Any | None = True,
    mark_sharp: bool | typing.Any | None = False,
):
    """Set mesh seams according to island setup in the UV editor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mark_seams: Mark Seams, Mark boundary edges as seams
    :type mark_seams: bool | typing.Any | None
    :param mark_sharp: Mark Sharp, Mark boundary edges as sharp
    :type mark_sharp: bool | typing.Any | None
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
    location: typing.Any | None = (0.0, 0.0),
):
    """Select UV vertices

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
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: typing.Any | None
    """

    ...

def select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "TOGGLE",
):
    """Change selection of all UV vertices

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

def select_box(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    pinned: bool | typing.Any | None = False,
    xmin: typing.Any | None = 0,
    xmax: typing.Any | None = 0,
    ymin: typing.Any | None = 0,
    ymax: typing.Any | None = 0,
    wait_for_input: bool | typing.Any | None = True,
    mode: str | None = "SET",
):
    """Select UV vertices using box selection

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param pinned: Pinned, Border select pinned UVs only
        :type pinned: bool | typing.Any | None
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
    """Select UV vertices using circle selection

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

def select_edge_ring(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
    location: typing.Any | None = (0.0, 0.0),
):
    """Select an edge ring of connected UV vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | typing.Any | None
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: typing.Any | None
    """

    ...

def select_lasso(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    mode: str | None = "SET",
):
    """Select UVs using lasso selection

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: Path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
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

def select_less(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Deselect UV vertices at the boundary of each selection region

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
    """Select all UV vertices linked to the active UV map

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_linked_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
    deselect: bool | typing.Any | None = False,
    location: typing.Any | None = (0.0, 0.0),
):
    """Select all UV vertices linked under the mouse

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | typing.Any | None
    :param deselect: Deselect, Deselect linked UV vertices rather than selecting them
    :type deselect: bool | typing.Any | None
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: typing.Any | None
    """

    ...

def select_loop(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
    location: typing.Any | None = (0.0, 0.0),
):
    """Select a loop of connected UV vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | typing.Any | None
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: typing.Any | None
    """

    ...

def select_mode(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "VERTEX",
):
    """Change UV selection mode

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def select_more(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select more UV vertices connected to initial selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_overlap(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
):
    """Select all UV faces which overlap each other

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | typing.Any | None
    """

    ...

def select_pinned(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select all pinned UV vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_similar(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "PIN",
    compare: str | None = "EQUAL",
    threshold: typing.Any | None = 0.0,
):
    """Select similar UVs by property types

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    :param compare: Compare
    :type compare: str | None
    :param threshold: Threshold
    :type threshold: typing.Any | None
    """

    ...

def select_split(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select only entirely selected faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def shortest_path_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_face_step: bool | typing.Any | None = False,
    use_topology_distance: bool | typing.Any | None = False,
    use_fill: bool | typing.Any | None = False,
    skip: typing.Any | None = 0,
    nth: typing.Any | None = 1,
    offset: typing.Any | None = 0,
    object_index: typing.Any | None = -1,
    index: typing.Any | None = -1,
):
    """Select shortest path between two selections

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: bool | typing.Any | None
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: bool | typing.Any | None
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: bool | typing.Any | None
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: typing.Any | None
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: typing.Any | None
    :param offset: Offset, Offset from the starting point
    :type offset: typing.Any | None
    :type object_index: typing.Any | None
    :type index: typing.Any | None
    """

    ...

def shortest_path_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_face_step: bool | typing.Any | None = False,
    use_topology_distance: bool | typing.Any | None = False,
    use_fill: bool | typing.Any | None = False,
    skip: typing.Any | None = 0,
    nth: typing.Any | None = 1,
    offset: typing.Any | None = 0,
):
    """Selected shortest path between two vertices/edges/faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: bool | typing.Any | None
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: bool | typing.Any | None
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: bool | typing.Any | None
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: typing.Any | None
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: typing.Any | None
    :param offset: Offset, Offset from the starting point
    :type offset: typing.Any | None
    """

    ...

def smart_project(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    angle_limit: typing.Any | None = 1.15192,
    margin_method: str | None = "SCALED",
    rotate_method: str | None = "AXIS_ALIGNED_Y",
    island_margin: typing.Any | None = 0.0,
    area_weight: typing.Any | None = 0.0,
    correct_aspect: bool | typing.Any | None = True,
    scale_to_bounds: bool | typing.Any | None = False,
):
    """Projection unwraps the selected faces of mesh objects

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param angle_limit: Angle Limit, Lower for more projection groups, higher for less distortion
        :type angle_limit: typing.Any | None
        :param margin_method: Margin Method

    SCALED
    Scaled -- Use scale of existing UVs to multiply margin.

    ADD
    Add -- Just add the margin, ignoring any UV scale.

    FRACTION
    Fraction -- Specify a precise fraction of final UV output.
        :type margin_method: str | None
        :param rotate_method: Rotation Method

    AXIS_ALIGNED
    Axis-aligned -- Rotated to a minimal rectangle, either vertical or horizontal.

    AXIS_ALIGNED_X
    Axis-aligned (Horizontal) -- Rotate islands to be aligned horizontally.

    AXIS_ALIGNED_Y
    Axis-aligned (Vertical) -- Rotate islands to be aligned vertically.
        :type rotate_method: str | None
        :param island_margin: Island Margin, Margin to reduce bleed from adjacent islands
        :type island_margin: typing.Any | None
        :param area_weight: Area Weight, Weight projection's vector by faces with larger areas
        :type area_weight: typing.Any | None
        :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        :type correct_aspect: bool | typing.Any | None
        :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
        :type scale_to_bounds: bool | typing.Any | None
    """

    ...

def snap_cursor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    target: str | None = "PIXELS",
):
    """Snap cursor to target type

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param target: Target, Target to snap the selected UVs to
    :type target: str | None
    """

    ...

def snap_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    target: str | None = "PIXELS",
):
    """Snap selected UV vertices to target type

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param target: Target, Target to snap the selected UVs to
    :type target: str | None
    """

    ...

def sphere_project(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: str | None = "VIEW_ON_EQUATOR",
    align: str | None = "POLAR_ZX",
    pole: str | None = "PINCH",
    seam: bool | typing.Any | None = False,
    correct_aspect: bool | typing.Any | None = True,
    clip_to_bounds: bool | typing.Any | None = False,
    scale_to_bounds: bool | typing.Any | None = False,
):
    """Project the UV vertices of the mesh over the curved surface of a sphere

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param direction: Direction, Direction of the sphere or cylinder

    VIEW_ON_EQUATOR
    View on Equator -- 3D view is on the equator.

    VIEW_ON_POLES
    View on Poles -- 3D view is on the poles.

    ALIGN_TO_OBJECT
    Align to Object -- Align according to object transform.
        :type direction: str | None
        :param align: Align, How to determine rotation around the pole

    POLAR_ZX
    Polar ZX -- Polar 0 is X.

    POLAR_ZY
    Polar ZY -- Polar 0 is Y.
        :type align: str | None
        :param pole: Pole, How to handle faces at the poles

    PINCH
    Pinch -- UVs are pinched at the poles.

    FAN
    Fan -- UVs are fanned at the poles.
        :type pole: str | None
        :param seam: Preserve Seams, Separate projections by islands isolated by seams
        :type seam: bool | typing.Any | None
        :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        :type correct_aspect: bool | typing.Any | None
        :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
        :type clip_to_bounds: bool | typing.Any | None
        :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
        :type scale_to_bounds: bool | typing.Any | None
    """

    ...

def stitch(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_limit: bool | typing.Any | None = False,
    snap_islands: bool | typing.Any | None = True,
    limit: typing.Any | None = 0.01,
    static_island: typing.Any | None = 0,
    active_object_index: typing.Any | None = 0,
    midpoint_snap: bool | typing.Any | None = False,
    clear_seams: bool | typing.Any | None = True,
    mode: str | None = "VERTEX",
    stored_mode: str | None = "VERTEX",
    selection: bpy.types.bpy_prop_collection[bpy.types.SelectedUvElement] | None = None,
    objects_selection_count: typing.Any | None = (0, 0, 0, 0, 0, 0),
):
    """Stitch selected UV vertices by proximity

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_limit: Use Limit, Stitch UVs within a specified limit distance
    :type use_limit: bool | typing.Any | None
    :param snap_islands: Snap Islands, Snap islands together (on edge stitch mode, rotates the islands too)
    :type snap_islands: bool | typing.Any | None
    :param limit: Limit, Limit distance in normalized coordinates
    :type limit: typing.Any | None
    :param static_island: Static Island, Island that stays in place when stitching islands
    :type static_island: typing.Any | None
    :param active_object_index: Active Object, Index of the active object
    :type active_object_index: typing.Any | None
    :param midpoint_snap: Snap at Midpoint, UVs are stitched at midpoint instead of at static island
    :type midpoint_snap: bool | typing.Any | None
    :param clear_seams: Clear Seams, Clear seams of stitched edges
    :type clear_seams: bool | typing.Any | None
    :param mode: Operation Mode, Use vertex or edge stitching
    :type mode: str | None
    :param stored_mode: Stored Operation Mode, Use vertex or edge stitching
    :type stored_mode: str | None
    :param selection: Selection
    :type selection: bpy.types.bpy_prop_collection[bpy.types.SelectedUvElement] | None
    :param objects_selection_count: Objects Selection Count
    :type objects_selection_count: typing.Any | None
    """

    ...

def unwrap(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    method: str | None = "ANGLE_BASED",
    fill_holes: bool | typing.Any | None = True,
    correct_aspect: bool | typing.Any | None = True,
    use_subsurf_data: bool | typing.Any | None = False,
    margin_method: str | None = "SCALED",
    margin: typing.Any | None = 0.001,
):
    """Unwrap the mesh of the object being edited

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param method: Method, Unwrapping method (Angle Based usually gives better results than Conformal, while being somewhat slower)
        :type method: str | None
        :param fill_holes: Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
        :type fill_holes: bool | typing.Any | None
        :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        :type correct_aspect: bool | typing.Any | None
        :param use_subsurf_data: Use Subdivision Surface, Map UVs taking vertex position after Subdivision Surface modifier has been applied
        :type use_subsurf_data: bool | typing.Any | None
        :param margin_method: Margin Method

    SCALED
    Scaled -- Use scale of existing UVs to multiply margin.

    ADD
    Add -- Just add the margin, ignoring any UV scale.

    FRACTION
    Fraction -- Specify a precise fraction of final UV output.
        :type margin_method: str | None
        :param margin: Margin, Space between islands
        :type margin: typing.Any | None
    """

    ...

def weld(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Weld selected UV vertices together

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...
