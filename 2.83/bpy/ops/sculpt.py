import sys
import typing
import bpy.types


def brush_stroke(stroke: typing.Union[
        typing.Dict[str, 'bpy.types.OperatorStrokeElement'], typing.
        List['bpy.types.OperatorStrokeElement'], 'bpy_prop_collection'] = None,
                 mode: typing.Union[str, int] = 'NORMAL',
                 ignore_background_click: bool = False):
    ''' Sculpt a stroke into the geometry

    :param stroke: Stroke
    :type stroke: typing.Union[typing.Dict[str, 'bpy.types.OperatorStrokeElement'], typing.List['bpy.types.OperatorStrokeElement'], 'bpy_prop_collection']
    :param mode: Stroke Mode, Action taken when a paint stroke is made * NORMAL Regular, Apply brush normally. * INVERT Invert, Invert action of brush for duration of stroke. * SMOOTH Smooth, Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Union[str, int]
    :param ignore_background_click: Ignore Background Click, Clicks on the background do not start the stroke
    :type ignore_background_click: bool
    '''

    pass


def detail_flood_fill():
    ''' Flood fill the mesh with the selected detail setting

    '''

    pass


def dirty_mask(dirty_only: bool = False):
    ''' Generates a mask based on the geometry cavity and pointiness

    :param dirty_only: Dirty Only, Don't calculate cleans for convex areas
    :type dirty_only: bool
    '''

    pass


def dynamic_topology_toggle():
    ''' Dynamic topology alters the mesh topology while sculpting

    '''

    pass


def face_set_change_visibility(mode: typing.Union[str, int] = 'TOGGLE'):
    ''' Change the visibility of the Face Sets of the sculpt

    :param mode: Mode * TOGGLE Toggle Visibility, Hide all Face Sets except for the active one. * SHOW_ACTIVE Show Active Face Set, Show Active Face Set. * HIDE_ACTIVE Hide Active Face Sets, Hide Active Face Sets. * INVERT Invert Face Set Visibility, Invert Face Set Visibility. * SHOW_ALL Show All Face Sets, Show All Face Sets.
    :type mode: typing.Union[str, int]
    '''

    pass


def face_sets_create(mode: typing.Union[str, int] = 'MASKED'):
    ''' Create a new Face Set

    :param mode: Mode * MASKED Face Set From Masked, Create a new Face Set from the masked faces. * VISIBLE Face Set From Visible, Create a new Face Set from the visible vertices. * ALL Face Set Full Mesh, Create an unique Face Set with all faces in the sculpt. * SELECTION Face Set From Edit Mode Selection, Create an Face Set corresponding to the Edit Mode face selection.
    :type mode: typing.Union[str, int]
    '''

    pass


def face_sets_init(mode: typing.Union[str, int] = 'LOOSE_PARTS',
                   threshold: float = 0.5):
    ''' Initializes all Face Sets in the mesh

    :param mode: Mode * LOOSE_PARTS Face Sets From Loose Parts, Create a Face Set per loose part in the mesh. * MATERIALS Face Sets From Material Slots, Create a Face Set per Material Slot. * NORMALS Face Sets From Mesh Normals, Create Face Sets for Faces that have similar normal. * UV_SEAMS Face Sets From UV Seams, Create Face Sets using UV Seams as boundaries. * CREASES Face Sets From Edge Creases, Create Face Sets using Edge Creases as boundaries. * BEVEL_WEIGHT Face Sets From Bevel Weight, Create Face Sets using Bevel Weights as boundaries. * SHARP_EDGES Face Sets From Sharp Edges, Create Face Sets using Sharp Edges as boundaries. * FACE_MAPS Face Sets From Face Maps, Create a Face Set per Face Map.
    :type mode: typing.Union[str, int]
    :param threshold: Threshold, Minimum value to consider a certain attribute a boundary when creating the Face Sets
    :type threshold: float
    '''

    pass


def face_sets_randomize_colors():
    ''' Generates a new set of random colors to render the Face Sets in the viewport

    '''

    pass


def mask_expand(invert: bool = True,
                use_cursor: bool = True,
                update_pivot: bool = True,
                smooth_iterations: int = 2,
                mask_speed: int = 5,
                use_normals: bool = True,
                keep_previous_mask: bool = False,
                edge_sensitivity: int = 300,
                create_face_set: bool = False):
    ''' Expands a mask from the initial active vertex under the cursor

    :param invert: Invert, Invert the new mask
    :type invert: bool
    :param use_cursor: Use Cursor, Expand the mask to the cursor position
    :type use_cursor: bool
    :param update_pivot: Update Pivot Position, Set the pivot position to the mask border after creating the mask
    :type update_pivot: bool
    :param smooth_iterations: Smooth iterations
    :type smooth_iterations: int
    :param mask_speed: Mask speed
    :type mask_speed: int
    :param use_normals: Use Normals, Generate the mask using the normals and curvature of the model
    :type use_normals: bool
    :param keep_previous_mask: Keep Previous Mask, Generate the new mask on top of the current one
    :type keep_previous_mask: bool
    :param edge_sensitivity: Edge Detection Sensitivity, Sensitivity for expanding the mask across sculpted sharp edges when using normals to generate the mask
    :type edge_sensitivity: int
    :param create_face_set: Expand Face Mask, Expand a new Face Mask instead of the sculpt mask
    :type create_face_set: bool
    '''

    pass


def mask_filter(filter_type: typing.Union[str, int] = 'SMOOTH',
                iterations: int = 1,
                auto_iteration_count: bool = False):
    ''' Applies a filter to modify the current mask

    :param filter_type: Type, Filter that is going to be applied to the mask * SMOOTH Smooth Mask, Smooth mask. * SHARPEN Sharpen Mask, Sharpen mask. * GROW Grow Mask, Grow mask. * SHRINK Shrink Mask, Shrink mask. * CONTRAST_INCREASE Increase contrast, Increase the contrast of the paint mask. * CONTRAST_DECREASE Decrease contrast, Decrease the contrast of the paint mask.
    :type filter_type: typing.Union[str, int]
    :param iterations: Iterations, Number of times that the filter is going to be applied
    :type iterations: int
    :param auto_iteration_count: Auto Iteration Count, Use a automatic number of iterations based on the number of vertices of the sculpt
    :type auto_iteration_count: bool
    '''

    pass


def mesh_filter(type: typing.Union[str, int] = 'INFLATE',
                strength: float = 1.0,
                deform_axis: typing.Union[typing.Set[str], typing.Set[int]] = {
                    'X', 'Y', 'Z'
                },
                use_face_sets: bool = False,
                surface_smooth_shape_preservation: float = 0.5,
                surface_smooth_current_vertex: float = 0.5,
                sharpen_smooth_ratio: float = 0.35):
    ''' Applies a filter to modify the current mesh

    :param type: Filter type, Operation that is going to be applied to the mesh * SMOOTH Smooth, Smooth mesh. * SCALE Scale, Scale mesh. * INFLATE Inflate, Inflate mesh. * SPHERE Sphere, Morph into sphere. * RANDOM Random, Randomize vertex positions. * RELAX Relax, Relax mesh. * RELAX_FACE_SETS Relax Face Sets, Smooth the edges of all the Face Sets. * SURFACE_SMOOTH Surface Smooth, Smooth the surface of the mesh, preserving the volume. * SHARPEN Sharpen, Sharpen the cavities of the mesh.
    :type type: typing.Union[str, int]
    :param strength: Strength, Filter Strength
    :type strength: float
    :param deform_axis: Deform axis, Apply the deformation in the selected axis * X X, Deform in the X axis. * Y Y, Deform in the Y axis. * Z Z, Deform in the Z axis.
    :type deform_axis: typing.Union[typing.Set[str], typing.Set[int]]
    :param use_face_sets: Use Face Sets, Apply the filter only to the Face Mask under the cursor
    :type use_face_sets: bool
    :param surface_smooth_shape_preservation: Shape Preservation, How much of the original shape is preserved when smoothing
    :type surface_smooth_shape_preservation: float
    :param surface_smooth_current_vertex: Per Vertex Displacement, How much the position of each individual vertex influences the final result
    :type surface_smooth_current_vertex: float
    :param sharpen_smooth_ratio: Smooth Ratio, How much smoothing is applied to polished surfaces
    :type sharpen_smooth_ratio: float
    '''

    pass


def optimize():
    ''' Recalculate the sculpt BVH to improve performance

    '''

    pass


def sample_detail_size(location: typing.List[int] = (0, 0),
                       mode: typing.Union[str, int] = 'DYNTOPO'):
    ''' Sample the mesh detail on clicked point

    :param location: Location, Screen Coordinates of sampling
    :type location: typing.List[int]
    :param mode: Detail Mode, Target sculpting workflow that is going to use the sampled size * DYNTOPO Dyntopo, Sample dyntopo detail. * VOXEL Voxel, Sample mesh voxel size.
    :type mode: typing.Union[str, int]
    '''

    pass


def sculptmode_toggle():
    ''' Toggle sculpt mode in 3D view

    '''

    pass


def set_detail_size():
    ''' Set the mesh detail (either relative or constant one, depending on current dyntopo mode)

    '''

    pass


def set_persistent_base():
    ''' Reset the copy of the mesh that is being sculpted on

    '''

    pass


def set_pivot_position(mode: typing.Union[str, int] = 'UNMASKED',
                       mouse_x: float = 0.0,
                       mouse_y: float = 0.0):
    ''' Sets the sculpt transform pivot position

    :param mode: Mode * ORIGIN Origin, Sets the pivot to the origin of the sculpt. * UNMASKED Unmasked, Sets the pivot position to the average position of the unmasked vertices. * BORDER Mask border, Sets the pivot position to the center of the border of the mask. * ACTIVE Active vertex, Sets the pivot position to the active vertex position. * SURFACE Surface, Sets the pivot position to the surface under the cursor.
    :type mode: typing.Union[str, int]
    :param mouse_x: Mouse Position X, Position of the mouse used for "Surface" mode
    :type mouse_x: float
    :param mouse_y: Mouse Position Y, Position of the mouse used for "Surface" mode
    :type mouse_y: float
    '''

    pass


def symmetrize(merge_tolerance: float = 0.001):
    ''' Symmetrize the topology modifications

    :param merge_tolerance: Merge Limit, Distance within which symmetrical vertices are merged
    :type merge_tolerance: float
    '''

    pass


def uv_sculpt_stroke(mode: typing.Union[str, int] = 'NORMAL'):
    ''' Sculpt UVs using a brush

    :param mode: Mode, Stroke Mode * NORMAL Regular, Apply brush normally. * INVERT Invert, Invert action of brush for duration of stroke. * RELAX Relax, Switch brush to relax mode for duration of stroke.
    :type mode: typing.Union[str, int]
    '''

    pass
