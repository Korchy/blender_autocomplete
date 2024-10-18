import typing
import collections.abc
import typing_extensions
import bpy.types
import mathutils

def location_3d_to_region_2d(
    region: bpy.types.Region,
    rv3d: bpy.types.RegionView3D,
    coord: collections.abc.Sequence[float] | mathutils.Vector,
    *,
    default=None,
) -> mathutils.Vector:
    """Return the region relative 2d location of a 3d position.

        :param region: region of the 3D viewport, typically bpy.context.region.
        :type region: bpy.types.Region
        :param rv3d: 3D region data, typically bpy.context.space_data.region_3d.
        :type rv3d: bpy.types.RegionView3D
        :param coord: 3d world-space location.
        :type coord: collections.abc.Sequence[float] | mathutils.Vector
        :param default: Return this value if coord
    is behind the origin of a perspective view.
        :return: 2d location
        :rtype: mathutils.Vector
    """

def region_2d_to_location_3d(
    region: bpy.types.Region,
    rv3d: bpy.types.RegionView3D,
    coord: collections.abc.Sequence[float] | mathutils.Vector,
    depth_location: collections.abc.Sequence[float] | mathutils.Vector,
) -> mathutils.Vector:
    """Return a 3d location from the region relative 2d coords, aligned with
    depth_location.

        :param region: region of the 3D viewport, typically bpy.context.region.
        :type region: bpy.types.Region
        :param rv3d: 3D region data, typically bpy.context.space_data.region_3d.
        :type rv3d: bpy.types.RegionView3D
        :param coord: 2d coordinates relative to the region;
    (event.mouse_region_x, event.mouse_region_y) for example.
        :type coord: collections.abc.Sequence[float] | mathutils.Vector
        :param depth_location: the returned vectors depth is aligned with this since
    there is no defined depth with a 2d region input.
        :type depth_location: collections.abc.Sequence[float] | mathutils.Vector
        :return: normalized 3d vector.
        :rtype: mathutils.Vector
    """

def region_2d_to_origin_3d(
    region: bpy.types.Region,
    rv3d: bpy.types.RegionView3D,
    coord: collections.abc.Sequence[float] | mathutils.Vector,
    *,
    clamp: float | None = None,
) -> mathutils.Vector:
    """Return the 3d view origin from the region relative 2d coords.

        :param region: region of the 3D viewport, typically bpy.context.region.
        :type region: bpy.types.Region
        :param rv3d: 3D region data, typically bpy.context.space_data.region_3d.
        :type rv3d: bpy.types.RegionView3D
        :param coord: 2d coordinates relative to the region;
    (event.mouse_region_x, event.mouse_region_y) for example.
        :type coord: collections.abc.Sequence[float] | mathutils.Vector
        :param clamp: Clamp the maximum far-clip value used.
    (negative value will move the offset away from the view_location)
        :type clamp: float | None
        :return: The origin of the viewpoint in 3d space.
        :rtype: mathutils.Vector
    """

def region_2d_to_vector_3d(
    region: bpy.types.Region,
    rv3d: bpy.types.RegionView3D,
    coord: collections.abc.Sequence[float] | mathutils.Vector,
) -> mathutils.Vector:
    """Return a direction vector from the viewport at the specific 2d region
    coordinate.

        :param region: region of the 3D viewport, typically bpy.context.region.
        :type region: bpy.types.Region
        :param rv3d: 3D region data, typically bpy.context.space_data.region_3d.
        :type rv3d: bpy.types.RegionView3D
        :param coord: 2d coordinates relative to the region:
    (event.mouse_region_x, event.mouse_region_y) for example.
        :type coord: collections.abc.Sequence[float] | mathutils.Vector
        :return: normalized 3d vector.
        :rtype: mathutils.Vector
    """
