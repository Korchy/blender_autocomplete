import typing
import collections.abc
import typing_extensions
import mathutils

def primitive_nurbs_surface_circle_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
):
    """Construct a Nurbs surface Circle

        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: float | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def primitive_nurbs_surface_curve_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
):
    """Construct a Nurbs surface Curve

        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: float | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def primitive_nurbs_surface_cylinder_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
):
    """Construct a Nurbs surface Cylinder

        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: float | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def primitive_nurbs_surface_sphere_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
):
    """Construct a Nurbs surface Sphere

        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: float | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def primitive_nurbs_surface_surface_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
):
    """Construct a Nurbs surface Patch

        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: float | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def primitive_nurbs_surface_torus_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
    enter_editmode: bool | None = False,
    align: typing.Literal["WORLD", "VIEW", "CURSOR"] | None = "WORLD",
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (
        0.0,
        0.0,
        0.0,
    ),
    rotation: collections.abc.Sequence[float] | mathutils.Euler | None = (
        0.0,
        0.0,
        0.0,
    ),
    scale: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
):
    """Construct a Nurbs surface Torus

        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: float | None
        :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
        :type enter_editmode: bool | None
        :param align: Align, The alignment of the new object

    WORLD
    World -- Align the new object to the world.

    VIEW
    View -- Align the new object to the view.

    CURSOR
    3D Cursor -- Use the 3D cursor orientation for the new object.
        :type align: typing.Literal['WORLD','VIEW','CURSOR'] | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Sequence[float] | mathutils.Vector | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Sequence[float] | mathutils.Euler | None
        :param scale: Scale, Scale for the newly added object
        :type scale: collections.abc.Sequence[float] | mathutils.Vector | None
    """
