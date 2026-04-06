import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums

def attribute_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    domain: bpy.stub_internal.rna_enums.AttributeDomainItems | None = "POINT",
    data_type: bpy.stub_internal.rna_enums.AttributeTypeItems | None = "FLOAT",
) -> None:
    """Add attribute to geometry

    :param name: Name, Name of new attribute
    :param domain: Domain, Type of element that attribute is stored on
    :param data_type: Data Type, Type of data stored in attribute
    """

def attribute_convert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["GENERIC", "VERTEX_GROUP"] | None = "GENERIC",
    domain: bpy.stub_internal.rna_enums.AttributeDomainItems | None = "POINT",
    data_type: bpy.stub_internal.rna_enums.AttributeTypeItems | None = "FLOAT",
) -> None:
    """Change how the attribute is stored

    :param mode: Mode
    :param domain: Domain, Which geometry element to move the attribute to
    :param data_type: Data Type
    """

def attribute_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove attribute from geometry"""

def color_attribute_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    domain: bpy.stub_internal.rna_enums.ColorAttributeDomainItems | None = "POINT",
    data_type: bpy.stub_internal.rna_enums.ColorAttributeTypeItems
    | None = "FLOAT_COLOR",
    color: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0, 1.0),
) -> None:
    """Add color attribute to geometry

    :param name: Name, Name of new color attribute
    :param domain: Domain, Type of element that attribute is stored on
    :param data_type: Data Type, Type of data stored in attribute
    :param color: Color, Default fill color
    """

def color_attribute_convert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    domain: bpy.stub_internal.rna_enums.ColorAttributeDomainItems | None = "POINT",
    data_type: bpy.stub_internal.rna_enums.ColorAttributeTypeItems
    | None = "FLOAT_COLOR",
) -> None:
    """Change how the color attribute is stored

    :param domain: Domain, Type of element that attribute is stored on
    :param data_type: Data Type, Type of data stored in attribute
    """

def color_attribute_duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Duplicate color attribute"""

def color_attribute_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove color attribute from geometry"""

def color_attribute_render_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "Color",
) -> None:
    """Set default color attribute used for rendering

    :param name: Name, Name of color attribute
    """

def execute_node_group(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    asset_library_type: bpy.stub_internal.rna_enums.AssetLibraryTypeItems
    | None = "LOCAL",
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
) -> None:
    """Execute a node group on geometry

    :param asset_library_type: Asset Library Type
    :param asset_library_identifier: Asset Library Identifier
    :param relative_asset_identifier: Relative Asset Identifier
    :param name: Name, Name of the data-block to use by the operator
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :param mouse_position: Mouse Position, Mouse coordinates in region space
    :param region_size: Region Size
    :param cursor_position: 3D Cursor Position
    :param cursor_rotation: 3D Cursor Rotation
    :param viewport_projection_matrix: Viewport Projection Transform
    :param viewport_view_matrix: Viewport View Transform
    :param viewport_is_perspective: Viewport Is Perspective
    """

def geometry_randomization(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: bool | None = False,
) -> None:
    """Toggle geometry randomization for debugging purposes

    :param value: Value, Randomize the order of geometry elements (e.g. vertices or edges) after some operations where there are no guarantees about the order. This avoids accidentally depending on something that may change in the future
    """
