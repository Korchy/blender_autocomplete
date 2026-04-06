import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types
import mathutils

class AddObjectHelper:
    def align_update_callback(self, _context) -> None:
        """

        :param _context:
        """

def add_object_align_init(
    context: bpy.types.Context, operator: bpy.types.Operator
) -> mathutils.Matrix:
    """Return a matrix using the operator settings and view context.

    :param context: The context to use.
    :param operator: The operator, checked for location and rotation properties.
    :return: the matrix from the context and settings.
    """

def object_add_grid_scale(context) -> None:
    """Return scale which should be applied on object
    data to align it to grid scale

    """

def object_add_grid_scale_apply_operator(operator, context) -> None:
    """Scale an operators distance values by the grid size."""

def object_data_add(
    context: bpy.types.Context,
    obdata: None | bpy.types.ID,
    operator: bpy.types.Operator | None = None,
    name: str | None = None,
) -> bpy.types.Object:
    """Add an object using the view context and preference to initialize the
    location, rotation and layer.

        :param context: The context to use.
        :param obdata: Valid object data to used for the new object or None.
        :param operator: The operator, checked for location and rotation properties.
        :param name: Optional name
        :return: the newly created object in the scene.
    """

def object_report_if_active_shape_key_is_locked(
    obj: bpy.types.Object, operator: bpy.types.Operator
) -> None:
    """Checks if the active shape key of the specified object is locked, and reports an error if so.If the object has no shape keys, there is nothing to lock, and the function returns False.

    :param obj: Object to check.
    :param operator: Currently running operator to report the error through. Use None to suppress emitting the message.
    :return: True if the shape key was locked.
    """

def world_to_camera_view(
    scene: bpy.types.Scene,
    obj: bpy.types.Object,
    coord: collections.abc.Sequence[float] | mathutils.Vector,
) -> mathutils.Vector:
    """Returns the camera space coords for a 3d point.
    (also known as: normalized device coordinates - NDC).Where (0, 0) is the bottom left and (1, 1)
    is the top right of the camera frame.
    values outside 0-1 are also supported.
    A negative z value means the point is behind the camera.Takes shift-x/y, lens angle and sensor size into account
    as well as perspective/ortho projections.

        :param scene: Scene to use for frame size.
        :param obj: Camera object.
        :param coord: World space location.
        :return: a vector where X and Y map to the view plane and
    Z is the depth on the view axis.
    """
