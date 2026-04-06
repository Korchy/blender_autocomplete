import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bl_ui.space_toolsystem_common

class IMAGE_PT_tools_active(
    bl_ui.space_toolsystem_common.ToolSelectPanelHelper, _bpy_types.Panel
):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    keymap_prefix: typing.Any
    tool_fallback_id: typing.Any

    def bl_rna_get_subclass(self) -> None: ...
    def bl_rna_get_subclass_py(self) -> None: ...
    @classmethod
    def tools_all(cls) -> None: ...
    @classmethod
    def tools_from_context(cls, context, mode=None) -> None:
        """

        :param context:
        :param mode:
        """

class NODE_PT_tools_active(
    bl_ui.space_toolsystem_common.ToolSelectPanelHelper, _bpy_types.Panel
):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    keymap_prefix: typing.Any
    tool_fallback_id: typing.Any

    def bl_rna_get_subclass(self) -> None: ...
    def bl_rna_get_subclass_py(self) -> None: ...
    @classmethod
    def tools_all(cls) -> None: ...
    @classmethod
    def tools_from_context(cls, context, mode=None) -> None:
        """

        :param context:
        :param mode:
        """

class SEQUENCER_PT_tools_active(
    bl_ui.space_toolsystem_common.ToolSelectPanelHelper, _bpy_types.Panel
):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    keymap_prefix: typing.Any
    tool_fallback_id: typing.Any

    def bl_rna_get_subclass(self) -> None: ...
    def bl_rna_get_subclass_py(self) -> None: ...
    @classmethod
    def tools_all(cls) -> None: ...
    @classmethod
    def tools_from_context(cls, context, mode=None) -> None:
        """

        :param context:
        :param mode:
        """

class VIEW3D_PT_tools_active(
    bl_ui.space_toolsystem_common.ToolSelectPanelHelper, _bpy_types.Panel
):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    keymap_prefix: typing.Any
    tool_fallback_id: typing.Any

    def bl_rna_get_subclass(self) -> None: ...
    def bl_rna_get_subclass_py(self) -> None: ...
    @classmethod
    def tools_all(cls) -> None: ...
    @classmethod
    def tools_from_context(cls, context, mode=None) -> None:
        """

        :param context:
        :param mode:
        """

class _defs_annotate:
    eraser: typing.Any
    line: typing.Any
    poly: typing.Any
    scribble: typing.Any

    def draw_settings_common(self, context, layout, tool) -> None:
        """

        :param context:
        :param layout:
        :param tool:
        """

class _defs_curves_sculpt:
    add: typing.Any
    delete: typing.Any
    density: typing.Any
    select: typing.Any

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
    pen: typing.Any

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

class _defs_grease_pencil_edit:
    interpolate: typing.Any
    pen: typing.Any
    shear: typing.Any
    texture_gradient: typing.Any

class _defs_grease_pencil_paint:
    arc: typing.Any
    box: typing.Any
    circle: typing.Any
    curve: typing.Any
    erase: typing.Any
    eyedropper: typing.Any
    fill: typing.Any
    interpolate: typing.Any
    line: typing.Any
    polyline: typing.Any
    trim: typing.Any

    @staticmethod
    def grease_pencil_primitive_toolbar(context, layout, _tool, props) -> None:
        """

        :param context:
        :param layout:
        :param _tool:
        :param props:
        """

class _defs_grease_pencil_sculpt:
    clone: typing.Any

    @staticmethod
    def poll_select_mask(context) -> None:
        """

        :param context:
        """

class _defs_grease_pencil_vertex:
    average: typing.Any
    blur: typing.Any
    replace: typing.Any
    smear: typing.Any

    @staticmethod
    def poll_select_mask(context) -> None:
        """

        :param context:
        """

class _defs_grease_pencil_weight:
    average: typing.Any
    blur: typing.Any
    smear: typing.Any

class _defs_image_generic:
    cursor: typing.Any
    sample: typing.Any

    @staticmethod
    def poll_uvedit(context) -> None:
        """

        :param context:
        """

class _defs_image_mask_primitive:
    box: typing.Any
    circle: typing.Any

class _defs_image_mask_select:
    box: typing.Any
    circle: typing.Any
    lasso: typing.Any
    select: typing.Any

class _defs_image_mask_transform:
    rotate: typing.Any
    scale: typing.Any
    transform: typing.Any
    translate: typing.Any

class _defs_image_uv_edit:
    rip_region: typing.Any

class _defs_image_uv_sculpt:
    grab: typing.Any
    pinch: typing.Any
    relax: typing.Any

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
    add_reroute: typing.Any
    links_cut: typing.Any
    links_mute: typing.Any

class _defs_node_select:
    box: typing.Any
    circle: typing.Any
    lasso: typing.Any
    select: typing.Any

class _defs_particle:
    @staticmethod
    def generate_from_brushes(context) -> None:
        """

        :param context:
        """

class _defs_pose:
    breakdown: typing.Any
    push: typing.Any
    relax: typing.Any

class _defs_sculpt:
    cloth_filter: typing.Any
    color_filter: typing.Any
    draw_face_sets: typing.Any
    dyntopo_density: typing.Any
    face_set_box: typing.Any
    face_set_edit: typing.Any
    face_set_lasso: typing.Any
    face_set_line: typing.Any
    face_set_polyline: typing.Any
    hide_border: typing.Any
    hide_lasso: typing.Any
    hide_line: typing.Any
    hide_polyline: typing.Any
    mask: typing.Any
    mask_border: typing.Any
    mask_by_color: typing.Any
    mask_lasso: typing.Any
    mask_line: typing.Any
    mask_polyline: typing.Any
    mesh_filter: typing.Any
    multires_eraser: typing.Any
    multires_smear: typing.Any
    paint: typing.Any
    project_line: typing.Any
    trim_box: typing.Any
    trim_lasso: typing.Any
    trim_line: typing.Any
    trim_polyline: typing.Any

    @staticmethod
    def draw_lasso_stroke_settings(layout, props, draw_inline, draw_popover) -> None:
        """

        :param layout:
        :param props:
        :param draw_inline:
        :param draw_popover:
        """

    @staticmethod
    def poll_dyntopo(context) -> None:
        """

        :param context:
        """

    @staticmethod
    def poll_multires(context) -> None:
        """

        :param context:
        """

class _defs_sequencer_generic:
    blade: typing.Any
    cursor: typing.Any
    rotate: typing.Any
    sample: typing.Any
    scale: typing.Any
    slip: typing.Any
    transform: typing.Any
    translate: typing.Any

class _defs_sequencer_select:
    box_preview: typing.Any
    box_timeline: typing.Any
    circle_preview: typing.Any
    circle_timeline: typing.Any
    lasso_preview: typing.Any
    lasso_timeline: typing.Any
    select_preview: typing.Any

class _defs_texture_paint:
    blur: typing.Any
    brush: typing.Any
    clone: typing.Any
    fill: typing.Any
    mask: typing.Any
    smear: typing.Any

    @staticmethod
    def poll_select_mask(context) -> None:
        """

        :param context:
        """

class _defs_transform:
    bend: typing.Any
    rotate: typing.Any
    scale: typing.Any
    scale_cage: typing.Any
    shear: typing.Any
    transform: typing.Any
    translate: typing.Any

    def draw_transform_sculpt_tool_settings(self, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

class _defs_vertex_paint:
    average: typing.Any
    blur: typing.Any
    smear: typing.Any

    @staticmethod
    def poll_select_mask(context) -> None:
        """

        :param context:
        """

class _defs_view3d_add:
    cone_add: typing.Any
    cube_add: typing.Any
    cylinder_add: typing.Any
    ico_sphere_add: typing.Any
    uv_sphere_add: typing.Any

    @staticmethod
    def description_interactive_add(context, _item, _km, *, prefix) -> None:
        """

        :param context:
        :param _item:
        :param _km:
        :param prefix:
        """

    @staticmethod
    def draw_settings_interactive_add(layout, tool_settings, tool, extra) -> None:
        """

        :param layout:
        :param tool_settings:
        :param tool:
        :param extra:
        """

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
    average: typing.Any
    blur: typing.Any
    gradient: typing.Any
    sample_weight: typing.Any
    sample_weight_group: typing.Any
    smear: typing.Any

    @staticmethod
    def poll_select_tools(context) -> None:
        """

        :param context:
        """

class _template_widget:
    def VIEW3D_GGT_xform_extrude(self) -> None: ...
    def VIEW3D_GGT_xform_gizmo(self) -> None: ...

def curve_draw_settings(context, layout, tool, *, extra=False) -> None: ...
def generate_from_enum_ex(
    _context,
    *,
    idname_prefix,
    icon_prefix,
    type,
    attr,
    options,
    cursor="DEFAULT",
    tooldef_keywords=None,
    icon_map=None,
    use_separators=True,
) -> None: ...
def kmi_to_string_or_none(kmi) -> None: ...
