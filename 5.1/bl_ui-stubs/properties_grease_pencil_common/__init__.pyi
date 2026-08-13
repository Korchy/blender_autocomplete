import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class AnnotationDataPanel:
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

    def draw_header(self, context) -> None:
        """

        :param context:
        """

    def draw_layers(self, context, layout, gpd) -> None:
        """

        :param context:
        :param layout:
        :param gpd:
        """

class AnnotationDrawingToolsPanel:
    bl_category: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

class AnnotationOnionSkin:
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

    def draw_header(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class GPENCIL_UL_annotation_layer(_bpy_types.UIList):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_item(
        self,
        _context,
        layout,
        _data,
        item,
        _icon,
        _active_data,
        _active_propname,
        _index,
    ) -> None:
        """

        :param _context:
        :param layout:
        :param _data:
        :param item:
        :param _icon:
        :param _active_data:
        :param _active_propname:
        :param _index:
        """

class GREASE_PENCIL_MT_draw_delete(_bpy_types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw(self, _context) -> None:
        """

        :param _context:
        """

class GREASE_PENCIL_MT_layer_active(_bpy_types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw(self, context) -> None:
        """

        :param context:
        """

class GREASE_PENCIL_MT_move_to_layer(_bpy_types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw(self, context) -> None:
        """

        :param context:
        """

class GREASE_PENCIL_MT_snap(_bpy_types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw(self, _context) -> None:
        """

        :param _context:
        """

class GREASE_PENCIL_MT_snap_pie(_bpy_types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw(self, _context) -> None:
        """

        :param _context:
        """

class GREASE_PENCIL_MT_stroke_simplify(_bpy_types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw(self, _context) -> None:
        """

        :param _context:
        """

class GreasePencilBrushFalloff:
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

class GreasePencilDisplayPanel:
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

    def draw_header(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class GreasePencilMaterialsPanel:
    def draw(self, context) -> None:
        """

        :param context:
        """

class GreasePencilSculptAdvancedPanel:
    def draw(self, context) -> None:
        """

        :param context:
        """

class GreasePencilSimplifyPanel:
    def draw(self, context) -> None:
        """

        :param context:
        """

    def draw_header(self, context) -> None:
        """

        :param context:
        """
