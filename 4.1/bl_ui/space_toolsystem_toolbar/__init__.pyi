import typing
import collections.abc
import bl_ui.space_toolsystem_common
import bpy_types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class IMAGE_PT_tools_active(
    bpy_types.Panel,
    bl_ui.space_toolsystem_common.ToolSelectPanelHelper,
    bpy_types._GenericUI,
):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    keymap_prefix: typing.Any
    tool_fallback_id: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param context:
        """
        ...

    def draw_active_tool_fallback(
        self, context, layout, tool, is_horizontal_layout=False
    ):
        """

        :param context:
        :param layout:
        :param tool:
        :param is_horizontal_layout:
        """
        ...

    def draw_active_tool_header(
        self, context, layout, show_tool_icon_always=False, tool_key=None
    ):
        """

        :param context:
        :param layout:
        :param show_tool_icon_always:
        :param tool_key:
        """
        ...

    def draw_cls(self, layout, context, detect_layout=True, scale_y=1.75):
        """

        :param layout:
        :param context:
        :param detect_layout:
        :param scale_y:
        """
        ...

    def draw_fallback_tool_items(self, layout, context):
        """

        :param layout:
        :param context:
        """
        ...

    def draw_fallback_tool_items_for_pie_menu(self, layout, context):
        """

        :param layout:
        :param context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keymap_ui_hierarchy(self, context_mode):
        """

        :param context_mode:
        """
        ...

    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def register(self): ...
    def register_ensure(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def tool_active_from_context(self, context):
        """

        :param context:
        """
        ...

    def tools_all(self): ...
    def tools_from_context(self, context, mode=None):
        """

        :param context:
        :param mode:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class NODE_PT_tools_active(
    bpy_types.Panel,
    bl_ui.space_toolsystem_common.ToolSelectPanelHelper,
    bpy_types._GenericUI,
):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    keymap_prefix: typing.Any
    tool_fallback_id: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param context:
        """
        ...

    def draw_active_tool_fallback(
        self, context, layout, tool, is_horizontal_layout=False
    ):
        """

        :param context:
        :param layout:
        :param tool:
        :param is_horizontal_layout:
        """
        ...

    def draw_active_tool_header(
        self, context, layout, show_tool_icon_always=False, tool_key=None
    ):
        """

        :param context:
        :param layout:
        :param show_tool_icon_always:
        :param tool_key:
        """
        ...

    def draw_cls(self, layout, context, detect_layout=True, scale_y=1.75):
        """

        :param layout:
        :param context:
        :param detect_layout:
        :param scale_y:
        """
        ...

    def draw_fallback_tool_items(self, layout, context):
        """

        :param layout:
        :param context:
        """
        ...

    def draw_fallback_tool_items_for_pie_menu(self, layout, context):
        """

        :param layout:
        :param context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keymap_ui_hierarchy(self, context_mode):
        """

        :param context_mode:
        """
        ...

    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def register(self): ...
    def register_ensure(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def tool_active_from_context(self, context):
        """

        :param context:
        """
        ...

    def tools_all(self): ...
    def tools_from_context(self, context, mode=None):
        """

        :param context:
        :param mode:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class SEQUENCER_PT_tools_active(
    bpy_types.Panel,
    bl_ui.space_toolsystem_common.ToolSelectPanelHelper,
    bpy_types._GenericUI,
):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    keymap_prefix: typing.Any
    tool_fallback_id: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param context:
        """
        ...

    def draw_active_tool_fallback(
        self, context, layout, tool, is_horizontal_layout=False
    ):
        """

        :param context:
        :param layout:
        :param tool:
        :param is_horizontal_layout:
        """
        ...

    def draw_active_tool_header(
        self, context, layout, show_tool_icon_always=False, tool_key=None
    ):
        """

        :param context:
        :param layout:
        :param show_tool_icon_always:
        :param tool_key:
        """
        ...

    def draw_cls(self, layout, context, detect_layout=True, scale_y=1.75):
        """

        :param layout:
        :param context:
        :param detect_layout:
        :param scale_y:
        """
        ...

    def draw_fallback_tool_items(self, layout, context):
        """

        :param layout:
        :param context:
        """
        ...

    def draw_fallback_tool_items_for_pie_menu(self, layout, context):
        """

        :param layout:
        :param context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keymap_ui_hierarchy(self, context_mode):
        """

        :param context_mode:
        """
        ...

    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def register(self): ...
    def register_ensure(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def tool_active_from_context(self, context):
        """

        :param context:
        """
        ...

    def tools_all(self): ...
    def tools_from_context(self, context, mode=None):
        """

        :param context:
        :param mode:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class VIEW3D_PT_tools_active(
    bpy_types.Panel,
    bl_ui.space_toolsystem_common.ToolSelectPanelHelper,
    bpy_types._GenericUI,
):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    keymap_prefix: typing.Any
    tool_fallback_id: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param context:
        """
        ...

    def draw_active_tool_fallback(
        self, context, layout, tool, is_horizontal_layout=False
    ):
        """

        :param context:
        :param layout:
        :param tool:
        :param is_horizontal_layout:
        """
        ...

    def draw_active_tool_header(
        self, context, layout, show_tool_icon_always=False, tool_key=None
    ):
        """

        :param context:
        :param layout:
        :param show_tool_icon_always:
        :param tool_key:
        """
        ...

    def draw_cls(self, layout, context, detect_layout=True, scale_y=1.75):
        """

        :param layout:
        :param context:
        :param detect_layout:
        :param scale_y:
        """
        ...

    def draw_fallback_tool_items(self, layout, context):
        """

        :param layout:
        :param context:
        """
        ...

    def draw_fallback_tool_items_for_pie_menu(self, layout, context):
        """

        :param layout:
        :param context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def id_properties_clear(self): ...
    def id_properties_ensure(self): ...
    def id_properties_ui(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keymap_ui_hierarchy(self, context_mode):
        """

        :param context_mode:
        """
        ...

    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def register(self): ...
    def register_ensure(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def tool_active_from_context(self, context):
        """

        :param context:
        """
        ...

    def tools_all(self): ...
    def tools_from_context(self, context, mode=None):
        """

        :param context:
        :param mode:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

class _defs_annotate:
    eraser: typing.Any
    line: typing.Any
    poly: typing.Any
    scribble: typing.Any

    def draw_settings_common(self, context, layout, tool):
        """

        :param context:
        :param layout:
        :param tool:
        """
        ...

class _defs_curves_sculpt:
    def generate_from_brushes(self, context):
        """

        :param context:
        """
        ...

class _defs_edit_armature:
    bone_envelope: typing.Any
    bone_size: typing.Any
    extrude: typing.Any
    extrude_cursor: typing.Any
    roll: typing.Any

class _defs_edit_curve:
    curve_radius: typing.Any
    curve_vertex_randomize: typing.Any
    draw: typing.Any
    extrude: typing.Any
    extrude_cursor: typing.Any
    pen: typing.Any
    tilt: typing.Any

class _defs_edit_curves:
    draw: typing.Any

class _defs_edit_mesh:
    bevel: typing.Any
    bisect: typing.Any
    edge_slide: typing.Any
    extrude: typing.Any
    extrude_cursor: typing.Any
    extrude_individual: typing.Any
    extrude_manifold: typing.Any
    extrude_normals: typing.Any
    inset: typing.Any
    knife: typing.Any
    loopcut_slide: typing.Any
    offset_edge_loops_slide: typing.Any
    poly_build: typing.Any
    push_pull: typing.Any
    rip_edge: typing.Any
    rip_region: typing.Any
    shrink_fatten: typing.Any
    spin: typing.Any
    tosphere: typing.Any
    vert_slide: typing.Any
    vertex_randomize: typing.Any
    vertex_smooth: typing.Any

class _defs_edit_text:
    select_text: typing.Any

class _defs_gpencil_edit:
    bend: typing.Any
    box_select: typing.Any
    circle_select: typing.Any
    extrude: typing.Any
    interpolate: typing.Any
    lasso_select: typing.Any
    radius: typing.Any
    select: typing.Any
    shear: typing.Any
    tosphere: typing.Any
    transform_fill: typing.Any

    def is_segment(self, context):
        """

        :param context:
        """
        ...

class _defs_gpencil_paint:
    arc: typing.Any
    box: typing.Any
    circle: typing.Any
    curve: typing.Any
    cutter: typing.Any
    eyedropper: typing.Any
    interpolate: typing.Any
    line: typing.Any
    polyline: typing.Any

    def generate_from_brushes(self, context):
        """

        :param context:
        """
        ...

    def gpencil_primitive_toolbar(self, context, layout, _tool, props):
        """

        :param context:
        :param layout:
        :param _tool:
        :param props:
        """
        ...

class _defs_gpencil_sculpt:
    def generate_from_brushes(self, context):
        """

        :param context:
        """
        ...

    def poll_select_mask(self, context):
        """

        :param context:
        """
        ...

class _defs_gpencil_vertex:
    def generate_from_brushes(self, context):
        """

        :param context:
        """
        ...

    def poll_select_mask(self, context):
        """

        :param context:
        """
        ...

class _defs_gpencil_weight:
    def generate_from_brushes(self, context):
        """

        :param context:
        """
        ...

class _defs_image_generic:
    cursor: typing.Any
    sample: typing.Any

    def poll_uvedit(self, context):
        """

        :param context:
        """
        ...

class _defs_image_uv_edit:
    rip_region: typing.Any

class _defs_image_uv_sculpt:
    def generate_from_brushes(self, context):
        """

        :param context:
        """
        ...

class _defs_image_uv_select:
    box: typing.Any
    circle: typing.Any
    lasso: typing.Any
    select: typing.Any

class _defs_image_uv_transform:
    rotate: typing.Any
    scale: typing.Any
    transform: typing.Any
    translate: typing.Any

class _defs_node_edit:
    links_cut: typing.Any

class _defs_node_select:
    box: typing.Any
    circle: typing.Any
    lasso: typing.Any
    select: typing.Any

class _defs_paint_grease_pencil:
    draw: typing.Any
    erase: typing.Any

class _defs_particle:
    def generate_from_brushes(self, context):
        """

        :param context:
        """
        ...

class _defs_pose:
    breakdown: typing.Any
    push: typing.Any
    relax: typing.Any

class _defs_sculpt:
    cloth_filter: typing.Any
    color_filter: typing.Any
    face_set_box: typing.Any
    face_set_edit: typing.Any
    face_set_lasso: typing.Any
    hide_border: typing.Any
    mask_border: typing.Any
    mask_by_color: typing.Any
    mask_lasso: typing.Any
    mask_line: typing.Any
    mesh_filter: typing.Any
    project_line: typing.Any
    trim_box: typing.Any
    trim_lasso: typing.Any

    def generate_from_brushes(self, context):
        """

        :param context:
        """
        ...

class _defs_sequencer_generic:
    blade: typing.Any
    cursor: typing.Any
    rotate: typing.Any
    sample: typing.Any
    scale: typing.Any
    transform: typing.Any
    translate: typing.Any

class _defs_sequencer_select:
    box: typing.Any
    select: typing.Any

class _defs_texture_paint:
    def generate_from_brushes(self, context):
        """

        :param context:
        """
        ...

    def poll_select_mask(self, context):
        """

        :param context:
        """
        ...

class _defs_transform:
    bend: typing.Any
    rotate: typing.Any
    scale: typing.Any
    scale_cage: typing.Any
    shear: typing.Any
    transform: typing.Any
    translate: typing.Any

    def draw_transform_sculpt_tool_settings(self, context, layout):
        """

        :param context:
        :param layout:
        """
        ...

class _defs_vertex_paint:
    def generate_from_brushes(self, context):
        """

        :param context:
        """
        ...

    def poll_select_mask(self, context):
        """

        :param context:
        """
        ...

class _defs_view3d_add:
    cone_add: typing.Any
    cube_add: typing.Any
    cylinder_add: typing.Any
    ico_sphere_add: typing.Any
    uv_sphere_add: typing.Any

    def description_interactive_add(self, context, _item, _km, prefix):
        """

        :param context:
        :param _item:
        :param _km:
        :param prefix:
        """
        ...

    def draw_settings_interactive_add(self, layout, tool_settings, tool, extra):
        """

        :param layout:
        :param tool_settings:
        :param tool:
        :param extra:
        """
        ...

class _defs_view3d_generic:
    cursor: typing.Any
    cursor_click: typing.Any
    ruler: typing.Any

class _defs_view3d_select:
    box: typing.Any
    circle: typing.Any
    lasso: typing.Any
    select: typing.Any

class _defs_weight_paint:
    gradient: typing.Any
    sample_weight: typing.Any
    sample_weight_group: typing.Any

    def generate_from_brushes(self, context):
        """

        :param context:
        """
        ...

    def poll_select_tools(self, context):
        """

        :param context:
        """
        ...

class _template_widget:
    def VIEW3D_GGT_xform_extrude(self): ...
    def VIEW3D_GGT_xform_gizmo(self): ...

def curve_draw_settings(context, layout, _tool, extra=False): ...
def generate_from_enum_ex(
    _context,
    idname_prefix,
    icon_prefix,
    type,
    attr,
    cursor="DEFAULT",
    tooldef_keywords=None,
    icon_map=None,
    use_separators=True,
): ...
def kmi_to_string_or_none(kmi): ...
