import sys
import typing
import bpy


def brush_stroke(stroke: typing.List['bpy.types.OperatorStrokeElement'] = None,
                 mode: typing.Union[str, int] = 'NORMAL',
                 ignore_background_click: bool = False):
    '''Sculpt a stroke into the geometry 

    :param stroke: Stroke 
    :type stroke: typing.List['bpy.types.OperatorStrokeElement']
    :param mode: Stroke Mode, Action taken when a paint stroke is madeNORMAL Regular, Apply brush normally.INVERT Invert, Invert action of brush for duration of stroke.SMOOTH Smooth, Switch brush to smooth mode for duration of stroke. 
    :type mode: typing.Union[str, int]
    :param ignore_background_click: Ignore Background Click, Clicks on the background do not start the stroke 
    :type ignore_background_click: bool
    '''

    pass


def detail_flood_fill():
    '''Flood fill the mesh with the selected detail setting 

    '''

    pass


def dirty_mask(dirty_only: bool = False):
    '''Generates a mask based on the geometry cavity and pointiness 

    :param dirty_only: Dirty Only, Don’t calculate cleans for convex areas 
    :type dirty_only: bool
    '''

    pass


def dynamic_topology_toggle():
    '''Dynamic topology alters the mesh topology while sculpting 

    '''

    pass


def mask_expand(invert: bool = True,
                use_cursor: bool = True,
                update_pivot: bool = True,
                smooth_iterations: int = 2,
                mask_speed: int = 5,
                use_normals: bool = True,
                keep_previous_mask: bool = False,
                edge_sensitivity: int = 300):
    '''Expands a mask from the initial active vertex under the cursor 

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
    '''

    pass


def mask_filter(filter_type: typing.Union[str, int] = 'SMOOTH',
                iterations: int = 1,
                auto_iteration_count: bool = False):
    '''Applies a filter to modify the current mask 

    :param filter_type: Type, Filter that is going to be applied to the maskSMOOTH Smooth Mask, Smooth mask.SHARPEN Sharpen Mask, Sharpen mask.GROW Grow Mask, Grow mask.SHRINK Shrink Mask, Shrink mask.CONTRAST_INCREASE Increase contrast, Increase the contrast of the paint mask.CONTRAST_DECREASE Decrease contrast, Decrease the contrast of the paint mask. 
    :type filter_type: typing.Union[str, int]
    :param iterations: Iterations, Number of times that the filter is going to be applied 
    :type iterations: int
    :param auto_iteration_count: Auto Iteration Count, Use a automatic number of iterations based on the number of vertices of the sculpt 
    :type auto_iteration_count: bool
    '''

    pass


def mesh_filter(
        type: typing.Union[str, int] = 'INFLATE',
        strength: float = 1.0,
        deform_axis: typing.Set[typing.Union[str, int]] = {'X', 'Y', 'Z'}):
    '''Applies a filter to modify the current mesh 

    :param type: Filter type, Operation that is going to be applied to the meshSMOOTH Smooth, Smooth mesh.SCALE Scale, Scale mesh.INFLATE Inflate, Inflate mesh.SPHERE Sphere, Morph into sphere.RANDOM Random, Randomize vertex positions.RELAX Relax, Relax mesh. 
    :type type: typing.Union[str, int]
    :param strength: Strength, Filter Strength 
    :type strength: float
    :param deform_axis: Deform axis, Apply the deformation in the selected axisX X, Deform in the X axis.Y Y, Deform in the Y axis.Z Z, Deform in the Z axis. 
    :type deform_axis: typing.Set[typing.Union[str, int]]
    '''

    pass


def optimize():
    '''Recalculate the sculpt BVH to improve performance 

    '''

    pass


def sample_detail_size(location: int = (0, 0),
                       mode: typing.Union[str, int] = 'DYNTOPO'):
    '''Sample the mesh detail on clicked point 

    :param location: Location, Screen Coordinates of sampling 
    :type location: int
    :param mode: Detail Mode, Target sculpting workflow that is going to use the sampled sizeDYNTOPO Dyntopo, Sample dyntopo detail.VOXEL Voxel, Sample mesh voxel size. 
    :type mode: typing.Union[str, int]
    '''

    pass


def sculptmode_toggle():
    '''Toggle sculpt mode in 3D view 

    '''

    pass


def set_detail_size():
    '''Set the mesh detail (either relative or constant one, depending on current dyntopo mode) 

    '''

    pass


def set_persistent_base():
    '''Reset the copy of the mesh that is being sculpted on 

    '''

    pass


def set_pivot_position(mode: typing.Union[str, int] = 'UNMASKED'):
    '''Sets the sculpt transform pivot position 

    :param mode: ModeORIGIN Origin, Sets the pivot to the origin of the sculpt.UNMASKED Unmasked, Sets the pivot position to the average position of the unmasked vertices.BORDER Mask border, Sets the pivot position to the center of the border of the mask.ACTIVE Active vertex, Sets the pivot position to the active vertex position.SURFACE Surface, Sets the pivot position to the surface under the cursor. 
    :type mode: typing.Union[str, int]
    '''

    pass


def symmetrize():
    '''Symmetrize the topology modifications 

    '''

    pass


def uv_sculpt_stroke(mode: typing.Union[str, int] = 'NORMAL'):
    '''Sculpt UVs using a brush 

    :param mode: Mode, Stroke ModeNORMAL Regular, Apply brush normally.INVERT Invert, Invert action of brush for duration of stroke.RELAX Relax, Switch brush to relax mode for duration of stroke. 
    :type mode: typing.Union[str, int]
    '''

    pass
