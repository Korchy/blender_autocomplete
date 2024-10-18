import typing
import collections.abc
import typing_extensions
import bpy.types
import bpy.typing

def attribute_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "",
    domain: bpy.typing.AttributeDomainItems | None = "POINT",
    data_type: bpy.typing.AttributeTypeItems | None = "FLOAT",
):
    """Add attribute to geometry

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of new attribute
    :type name: str
    :param domain: Domain, Type of element that attribute is stored on
    :type domain: bpy.typing.AttributeDomainItems | None
    :param data_type: Data Type, Type of data stored in attribute
    :type data_type: bpy.typing.AttributeTypeItems | None
    """

def attribute_convert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Literal["GENERIC", "VERTEX_GROUP"] | None = "GENERIC",
    domain: bpy.typing.AttributeDomainItems | None = "POINT",
    data_type: bpy.typing.AttributeTypeItems | None = "FLOAT",
):
    """Change how the attribute is stored

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['GENERIC','VERTEX_GROUP'] | None
    :param domain: Domain, Which geometry element to move the attribute to
    :type domain: bpy.typing.AttributeDomainItems | None
    :param data_type: Data Type
    :type data_type: bpy.typing.AttributeTypeItems | None
    """

def attribute_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove attribute from geometry

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def color_attribute_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "",
    domain: bpy.typing.ColorAttributeDomainItems | None = "POINT",
    data_type: bpy.typing.ColorAttributeTypeItems | None = "FLOAT_COLOR",
    color: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0, 1.0),
):
    """Add color attribute to geometry

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of new color attribute
    :type name: str
    :param domain: Domain, Type of element that attribute is stored on
    :type domain: bpy.typing.ColorAttributeDomainItems | None
    :param data_type: Data Type, Type of data stored in attribute
    :type data_type: bpy.typing.ColorAttributeTypeItems | None
    :param color: Color, Default fill color
    :type color: collections.abc.Iterable[float] | None
    """

def color_attribute_convert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    domain: bpy.typing.ColorAttributeDomainItems | None = "POINT",
    data_type: bpy.typing.ColorAttributeTypeItems | None = "FLOAT_COLOR",
):
    """Change how the color attribute is stored

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param domain: Domain, Type of element that attribute is stored on
    :type domain: bpy.typing.ColorAttributeDomainItems | None
    :param data_type: Data Type, Type of data stored in attribute
    :type data_type: bpy.typing.ColorAttributeTypeItems | None
    """

def color_attribute_duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Duplicate color attribute

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def color_attribute_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove color attribute from geometry

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def color_attribute_render_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str = "Color",
):
    """Set default color attribute used for rendering

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of color attribute
    :type name: str
    """

def execute_node_group(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    asset_library_type: bpy.typing.AssetLibraryTypeItems | None = "LOCAL",
    asset_library_identifier: str = "",
    relative_asset_identifier: str = "",
    name: str = "",
    session_uid: int | None = 0,
    mouse_position: collections.abc.Iterable[int] | None = (0, 0),
    region_size: collections.abc.Iterable[int] | None = (0, 0),
    cursor_position: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    cursor_rotation: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0, 0.0),
    viewport_projection_matrix: collections.abc.Iterable[float] | None = (
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ),
    viewport_view_matrix: collections.abc.Iterable[float] | None = (
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ),
    viewport_is_perspective: bool | None = False,
):
    """Execute a node group on geometry

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param asset_library_type: Asset Library Type
    :type asset_library_type: bpy.typing.AssetLibraryTypeItems | None
    :param asset_library_identifier: Asset Library Identifier
    :type asset_library_identifier: str
    :param relative_asset_identifier: Relative Asset Identifier
    :type relative_asset_identifier: str
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :type session_uid: int | None
    :param mouse_position: Mouse Position, Mouse coordinates in region space
    :type mouse_position: collections.abc.Iterable[int] | None
    :param region_size: Region Size
    :type region_size: collections.abc.Iterable[int] | None
    :param cursor_position: 3D Cursor Position
    :type cursor_position: collections.abc.Iterable[float] | None
    :param cursor_rotation: 3D Cursor Rotation
    :type cursor_rotation: collections.abc.Iterable[float] | None
    :param viewport_projection_matrix: Viewport Projection Transform
    :type viewport_projection_matrix: collections.abc.Iterable[float] | None
    :param viewport_view_matrix: Viewport View Transform
    :type viewport_view_matrix: collections.abc.Iterable[float] | None
    :param viewport_is_perspective: Viewport Is Perspective
    :type viewport_is_perspective: bool | None
    """

def geometry_randomization(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: bool | None = False,
):
    """Toggle geometry randomization for debugging purposes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param value: Value, Randomize the order of geometry elements (e.g. vertices or edges) after some operations where there are no guarantees about the order. This avoids accidentally depending on something that may change in the future
    :type value: bool | None
    """
