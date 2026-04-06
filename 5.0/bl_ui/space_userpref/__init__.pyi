import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bl_ui.utils
import bpy.types

class AddOnPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class AnimationPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class CenterAlignMixIn:
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    def draw(self, context) -> None:
        """

        :param context:
        """

class EditingPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class ExperimentalPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    @classmethod
    def poll(cls, _context) -> None:
        """

        :param _context:
        """

class ExtensionsPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class FilePathsPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class InputPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class InterfacePanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class KeymapPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class NavigationPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class PreferenceThemeSpacePanel:
    def draw(self, context) -> None:
        """

        :param context:
        """

    def draw_header(self, _context) -> None:
        """

        :param _context:
        """

class PreferenceThemeWidgetColorPanel:
    bl_parent_id: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

class PreferenceThemeWidgetShadePanel:
    def draw(self, context) -> None:
        """

        :param context:
        """

    def draw_header(self, context) -> None:
        """

        :param context:
        """

class SaveLoadPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class StudioLightPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class StudioLightPanelMixin:
    def draw(self, context) -> None:
        """

        :param context:
        """

    def draw_light_list(self, layout, lights) -> None:
        """

        :param layout:
        :param lights:
        """

    def draw_studio_light(self, layout, studio_light) -> None:
        """

        :param layout:
        :param studio_light:
        """

    def get_error_message(self) -> None: ...

class SystemPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class ThemeGenericClassGenerator:
    @staticmethod
    def generate_panel_classes_for_wcols() -> None: ...
    @staticmethod
    def generate_panel_classes_from_theme_areas() -> None: ...
    @staticmethod
    def generate_theme_area_child_panel_classes(
        parent_id, rna_type, theme_area, datapath
    ) -> None:
        """

        :param parent_id:
        :param rna_type:
        :param theme_area:
        :param datapath:
        """

class ThemePanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class USERPREF_HT_header(_bpy_types.Header):
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    @staticmethod
    def draw_buttons(layout, context) -> None:
        """

        :param layout:
        :param context:
        """

class USERPREF_MT_editor_menus(_bpy_types.Menu):
    bl_idname: typing.Any
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

class USERPREF_MT_extensions_active_repo(_bpy_types.Menu):
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

class USERPREF_MT_extensions_active_repo_remove(_bpy_types.Menu):
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

class USERPREF_MT_interface_theme_presets(_bpy_types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_operator: typing.Any
    preset_subdir: typing.Any
    preset_type: typing.Any
    preset_xml_map: typing.Any
    preset_xml_secure_types: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    @staticmethod
    def post_cb(context, filepath) -> None:
        """

        :param context:
        :param filepath:
        """

    @staticmethod
    def reset_cb(_context, _filepath) -> None:
        """

        :param _context:
        :param _filepath:
        """

class USERPREF_MT_keyconfigs(_bpy_types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_operator: typing.Any
    preset_subdir: typing.Any

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

class USERPREF_MT_save_load(_bpy_types.Menu):
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

class USERPREF_MT_view(_bpy_types.Menu):
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

class USERPREF_PT_addons(AddOnPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    @staticmethod
    def draw_addon_preferences(layout, context, addon_preferences) -> None:
        """

        :param layout:
        :param context:
        :param addon_preferences:
        """

    @staticmethod
    def draw_error(layout, message) -> None:
        """

        :param layout:
        :param message:
        """

    @staticmethod
    def is_user_addon(mod, user_addon_paths) -> None:
        """

        :param mod:
        :param user_addon_paths:
        """

class USERPREF_PT_addons_filter(_bpy_types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class USERPREF_PT_animation_fcurves(CenterAlignMixIn, AnimationPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_animation_keyframes(
    CenterAlignMixIn, AnimationPanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_animation_timeline(
    CenterAlignMixIn, AnimationPanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_developer_tools(_bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class USERPREF_PT_edit_annotations(CenterAlignMixIn, EditingPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_cursor(CenterAlignMixIn, EditingPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_gpencil(CenterAlignMixIn, EditingPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_misc(CenterAlignMixIn, EditingPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_node_editor(CenterAlignMixIn, EditingPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_objects(EditingPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

class USERPREF_PT_edit_objects_duplicate_data(
    CenterAlignMixIn, EditingPanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_objects_new(CenterAlignMixIn, EditingPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_sequence_editor(
    CenterAlignMixIn, EditingPanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_text_editor(CenterAlignMixIn, EditingPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_weight_paint(CenterAlignMixIn, EditingPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_experimental_new_features(ExperimentalPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

class USERPREF_PT_experimental_prototypes(ExperimentalPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

class USERPREF_PT_extensions(ExtensionsPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class USERPREF_PT_extensions_repos(_bpy_types.Panel):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class USERPREF_PT_file_paths_applications(FilePathsPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

class USERPREF_PT_file_paths_asset_libraries(FilePathsPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

class USERPREF_PT_file_paths_data(FilePathsPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

class USERPREF_PT_file_paths_development(FilePathsPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class USERPREF_PT_file_paths_render(FilePathsPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

class USERPREF_PT_file_paths_script_directories(FilePathsPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

class USERPREF_PT_input_keyboard(CenterAlignMixIn, InputPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_input_mouse(CenterAlignMixIn, InputPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_input_ndof(CenterAlignMixIn, InputPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class USERPREF_PT_input_tablet(CenterAlignMixIn, InputPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_input_touchpad(CenterAlignMixIn, InputPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class USERPREF_PT_interface_accessibility(
    CenterAlignMixIn, InterfacePanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_interface_display(CenterAlignMixIn, InterfacePanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_interface_editors(CenterAlignMixIn, InterfacePanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_interface_menus(CenterAlignMixIn, InterfacePanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_interface_menus_mouse_over(
    CenterAlignMixIn, InterfacePanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

    def draw_header(self, context) -> None:
        """

        :param context:
        """

class USERPREF_PT_interface_menus_pie(
    CenterAlignMixIn, InterfacePanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_interface_statusbar(
    CenterAlignMixIn, InterfacePanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_interface_temporary_windows(
    CenterAlignMixIn, InterfacePanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_interface_text(CenterAlignMixIn, InterfacePanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_interface_translation(
    CenterAlignMixIn, InterfacePanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_translation_context: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

    @classmethod
    def poll(cls, _context) -> None:
        """

        :param _context:
        """

class USERPREF_PT_keymap(KeymapPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

class USERPREF_PT_navigation_bar(_bpy_types.Panel):
    bl_category: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

class USERPREF_PT_navigation_fly_walk(
    CenterAlignMixIn, NavigationPanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_navigation_fly_walk_gravity(
    CenterAlignMixIn, NavigationPanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
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

class USERPREF_PT_navigation_fly_walk_navigation(
    CenterAlignMixIn, NavigationPanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class USERPREF_PT_navigation_orbit(CenterAlignMixIn, NavigationPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_navigation_zoom(CenterAlignMixIn, NavigationPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_ndof_settings(_bpy_types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

    @staticmethod
    def draw_settings(layout, props, show_3dview_settings=True) -> None:
        """

        :param layout:
        :param props:
        :param show_3dview_settings:
        """

class USERPREF_PT_save_preferences(_bpy_types.Panel):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class USERPREF_PT_saveload_autorun(FilePathsPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_header(self, context) -> None:
        """

        :param context:
        """

class USERPREF_PT_saveload_blend(CenterAlignMixIn, SaveLoadPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_saveload_file_browser(
    CenterAlignMixIn, SaveLoadPanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_studiolight_light_editor(StudioLightPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    @staticmethod
    def opengl_light_buttons(layout, light) -> None:
        """

        :param layout:
        :param light:
        """

class USERPREF_PT_studiolight_lights(
    StudioLightPanelMixin, StudioLightPanel, _bpy_types.Panel
):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    sl_type: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_header_preset(self, _context) -> None:
        """

        :param _context:
        """

    def get_error_message(self) -> None: ...

class USERPREF_PT_studiolight_matcaps(
    StudioLightPanelMixin, StudioLightPanel, _bpy_types.Panel
):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    sl_type: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_header_preset(self, _context) -> None:
        """

        :param _context:
        """

    def get_error_message(self) -> None: ...

class USERPREF_PT_studiolight_world(
    StudioLightPanelMixin, StudioLightPanel, _bpy_types.Panel
):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    sl_type: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_header_preset(self, _context) -> None:
        """

        :param _context:
        """

    def get_error_message(self) -> None: ...

class USERPREF_PT_system_cycles_devices(
    CenterAlignMixIn, SystemPanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_system_display_graphics(
    CenterAlignMixIn, SystemPanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

    @classmethod
    def poll(cls, _context) -> None:
        """

        :param _context:
        """

class USERPREF_PT_system_memory(CenterAlignMixIn, SystemPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_system_network(CenterAlignMixIn, SystemPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_system_os_settings(CenterAlignMixIn, SystemPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

    @classmethod
    def poll(cls, _context) -> None:
        """

        :param _context:
        """

class USERPREF_PT_system_sound(CenterAlignMixIn, SystemPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_system_video_sequencer(
    CenterAlignMixIn, SystemPanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_text_editor(FilePathsPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_header_preset(self, _context) -> None:
        """

        :param _context:
        """

class USERPREF_PT_text_editor_presets(bl_ui.utils.PresetPanel, _bpy_types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    preset_add_operator: typing.Any
    preset_operator: typing.Any
    preset_subdir: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class USERPREF_PT_theme(ThemePanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

class USERPREF_PT_theme_bone_color_sets(CenterAlignMixIn, ThemePanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

    def draw_header(self, _context) -> None:
        """

        :param _context:
        """

class USERPREF_PT_theme_collection_colors(
    CenterAlignMixIn, ThemePanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

    def draw_header(self, _context) -> None:
        """

        :param _context:
        """

class USERPREF_PT_theme_interface_gizmos(
    CenterAlignMixIn, ThemePanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_theme_interface_icons(CenterAlignMixIn, ThemePanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_theme_interface_panel(CenterAlignMixIn, ThemePanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_theme_interface_state(CenterAlignMixIn, ThemePanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_theme_interface_styles(
    CenterAlignMixIn, ThemePanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_theme_interface_transparent_checker(
    CenterAlignMixIn, ThemePanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_theme_strip_colors(CenterAlignMixIn, ThemePanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

    def draw_header(self, _context) -> None:
        """

        :param _context:
        """

class USERPREF_PT_theme_text_style(CenterAlignMixIn, ThemePanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

    def draw_header(self, _context) -> None:
        """

        :param _context:
        """

class USERPREF_PT_theme_user_interface(CenterAlignMixIn, ThemePanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_header(self, _context) -> None:
        """

        :param _context:
        """

class USERPREF_PT_viewport_display(CenterAlignMixIn, ViewportPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_viewport_quality(CenterAlignMixIn, ViewportPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_viewport_subdivision(
    CenterAlignMixIn, ViewportPanel, _bpy_types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_viewport_textures(CenterAlignMixIn, ViewportPanel, _bpy_types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw_centered(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class USERPREF_UL_asset_libraries(_bpy_types.UIList):
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

class USERPREF_UL_extension_repos(_bpy_types.UIList):
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
        icon,
        _active_data,
        _active_propname,
        _index,
    ) -> None:
        """

        :param _context:
        :param layout:
        :param _data:
        :param item:
        :param icon:
        :param _active_data:
        :param _active_propname:
        :param _index:
        """

    def filter_items(self, _context, data, propname) -> None:
        """

        :param _context:
        :param data:
        :param propname:
        """

class ViewportPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any
