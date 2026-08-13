import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class attribute_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        domain: typing.Literal[bpy.stub_internal.rna_enums.AttributeDomainItems]
        | None = "POINT",
        data_type: typing.Literal[bpy.stub_internal.rna_enums.AttributeTypeItems]
        | None = "FLOAT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add attribute to geometry

        :param execution_context:
        :param undo:
        :param name: Name, Name of new attribute (optional, never None)
        :param domain: Domain, Type of element that attribute is stored on (optional)
        :param data_type: Data Type, Type of data stored in attribute (optional)
        :return: Result of the operator call.
        """

class attribute_convert(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["GENERIC", "VERTEX_GROUP"] | None = "GENERIC",
        domain: typing.Literal[bpy.stub_internal.rna_enums.AttributeDomainItems]
        | None = "POINT",
        data_type: typing.Literal[bpy.stub_internal.rna_enums.AttributeTypeItems]
        | None = "FLOAT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change how the attribute is stored

        :param execution_context:
        :param undo:
        :param mode: Mode, (optional)
        :param domain: Domain, Which geometry element to move the attribute to (optional)
        :param data_type: Data Type, (optional)
        :return: Result of the operator call.
        """

class attribute_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove attribute from geometry

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class color_attribute_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        domain: typing.Literal[bpy.stub_internal.rna_enums.ColorAttributeDomainItems]
        | None = "POINT",
        data_type: typing.Literal[bpy.stub_internal.rna_enums.ColorAttributeTypeItems]
        | None = "FLOAT_COLOR",
        color: collections.abc.Sequence[float] | None = (0.0, 0.0, 0.0, 1.0),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add color attribute to geometry

        :param execution_context:
        :param undo:
        :param name: Name, Name of new color attribute (optional, never None)
        :param domain: Domain, Type of element that attribute is stored on (optional)
        :param data_type: Data Type, Type of data stored in attribute (optional)
        :param color: Color, Default fill color (array of 4 items, in [0, inf], optional)
        :return: Result of the operator call.
        """

class color_attribute_convert(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        domain: typing.Literal[bpy.stub_internal.rna_enums.ColorAttributeDomainItems]
        | None = "POINT",
        data_type: typing.Literal[bpy.stub_internal.rna_enums.ColorAttributeTypeItems]
        | None = "FLOAT_COLOR",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change how the color attribute is stored

        :param execution_context:
        :param undo:
        :param domain: Domain, Type of element that attribute is stored on (optional)
        :param data_type: Data Type, Type of data stored in attribute (optional)
        :return: Result of the operator call.
        """

class color_attribute_duplicate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate color attribute

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class color_attribute_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove color attribute from geometry

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class color_attribute_render_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "Color",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set default color attribute used for rendering

        :param execution_context:
        :param undo:
        :param name: Name, Name of color attribute (optional, never None)
        :return: Result of the operator call.
        """

class geometry_randomization(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        value: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle geometry randomization for debugging purposes

        :param execution_context:
        :param undo:
        :param value: Value, Randomize the order of geometry elements (e.g. vertices or edges) after some operations where there are no guarantees about the order. This avoids accidentally depending on something that may change in the future (optional)
        :return: Result of the operator call.
        """
