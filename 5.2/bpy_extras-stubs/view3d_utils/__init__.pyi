import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types
import mathutils

def location_3d_to_region_2d(
    region: bpy.types.Region,
    rv3d: bpy.types.RegionView3D,
    coord: collections.abc.Sequence[float] | mathutils.Vector,
    *,
    default: typing.Any | None = None,
) -> mathutils.Vector | typing.Any:
    """Return the region relative 2D location of a 3D position.

        :param region: region of the 3D viewport, typically bpy.context.region.
        :param rv3d: 3D region data, typically bpy.context.space_data.region_3d.
        :param coord: 3D world-space location.
        :param default: Return this value if coord
    is behind the origin of a perspective view.
        :return: 2D location
    """

def region_2d_to_location_3d(
    region: bpy.types.Region,
    rv3d: bpy.types.RegionView3D,
    coord: collections.abc.Sequence[float],
    depth_location: collections.abc.Sequence[float] | mathutils.Vector,
) -> mathutils.Vector:
    """Return a 3D location from the region relative 2D coords, aligned with
    depth_location.

        :param region: region of the 3D viewport, typically bpy.context.region.
        :param rv3d: 3D region data, typically bpy.context.space_data.region_3d.
        :param coord: 2D coordinates relative to the region;
    (event.mouse_region_x, event.mouse_region_y) for example.
        :param depth_location: the returned vectors depth is aligned with this since
    there is no defined depth with a 2D region input.
        :return: normalized 3D vector.
    """

def region_2d_to_origin_3d(
    region: bpy.types.Region,
    rv3d: bpy.types.RegionView3D,
    coord: collections.abc.Sequence[float],
    *,
    clamp: None | float | None = None,
) -> mathutils.Vector:
    """Return the 3D view origin from the region relative 2D coords.

        :param region: region of the 3D viewport, typically bpy.context.region.
        :param rv3d: 3D region data, typically bpy.context.space_data.region_3d.
        :param coord: 2D coordinates relative to the region;
    (event.mouse_region_x, event.mouse_region_y) for example.
        :param clamp: Clamp the maximum far-clip value used.
    (negative value will move the offset away from the view_location)
        :return: The origin of the viewpoint in 3D space.
    """

def region_2d_to_vector_3d(
    region: bpy.types.Region,
    rv3d: bpy.types.RegionView3D,
    coord: collections.abc.Sequence[float],
) -> mathutils.Vector:
    """Return a direction vector from the viewport at the specific 2D region
    coordinate.

        :param region: region of the 3D viewport, typically bpy.context.region.
        :param rv3d: 3D region data, typically bpy.context.space_data.region_3d.
        :param coord: 2D coordinates relative to the region:
    (event.mouse_region_x, event.mouse_region_y) for example.
        :return: normalized 3D vector.
    """
