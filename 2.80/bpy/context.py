import sys
import typing
import bpy

active_base: 'bpy.types.ObjectBase' = None

active_bone: 'bpy.types.EditBone' = None

active_editable_fcurve: 'bpy.types.FCurve' = None

active_gpencil_frame = None

active_gpencil_layer: 'bpy.types.GPencilLayer' = None

active_node: 'bpy.types.Node' = None

active_object: 'bpy.types.Object' = None

active_operator: 'bpy.types.Operator' = None

active_pose_bone: 'bpy.types.PoseBone' = None

area: 'bpy.types.Area' = None

armature: 'bpy.types.Armature' = None

blend_data: 'bpy.types.BlendData' = None

bone: 'bpy.types.Bone' = None

brush: 'bpy.types.Brush' = None

camera: 'bpy.types.Camera' = None

cloth: 'bpy.types.ClothModifier' = None

collection: 'bpy.types.Collection' = None

collision: 'bpy.types.CollisionModifier' = None

curve: 'bpy.types.Curve' = None

dynamic_paint: 'bpy.types.DynamicPaintModifier' = None

edit_bone: 'bpy.types.EditBone' = None

edit_image: 'bpy.types.Image' = None

edit_mask: 'bpy.types.Mask' = None

edit_movieclip: 'bpy.types.MovieClip' = None

edit_object: 'bpy.types.Object' = None

edit_text: 'bpy.types.Text' = None

editable_bones: 'bpy.types.EditBone' = None

editable_fcurves: 'bpy.types.FCurve' = None

editable_gpencil_layers: 'bpy.types.GPencilLayer' = None

editable_gpencil_strokes: 'bpy.types.GPencilStroke' = None

editable_objects: 'bpy.types.Object' = None

engine: str = None

fluid: 'bpy.types.FluidSimulationModifier' = None

gizmo_group: 'bpy.types.GizmoGroup' = None

gpencil: 'bpy.types.GreasePencil' = None

gpencil_data: 'bpy.types.GreasePencil' = None

gpencil_data_owner: 'bpy.types.ID' = None

image_paint_object: 'bpy.types.Object' = None

lattice: 'bpy.types.Lattice' = None

layer_collection: 'bpy.types.LayerCollection' = None

light: 'bpy.types.Light' = None

lightprobe: 'bpy.types.LightProbe' = None

line_style: 'bpy.types.FreestyleLineStyle' = None

material: 'bpy.types.Material' = None

material_slot: 'bpy.types.MaterialSlot' = None

mesh: 'bpy.types.Mesh' = None

meta_ball: 'bpy.types.MetaBall' = None

mode: int = None

object: 'bpy.types.Object' = None

objects_in_mode: 'bpy.types.Object' = None

objects_in_mode_unique_data: 'bpy.types.Object' = None

particle_edit_object: 'bpy.types.Object' = None

particle_settings: 'bpy.types.ParticleSettings' = None

particle_system: 'bpy.types.ParticleSystem' = None

particle_system_editable: 'bpy.types.ParticleSystem' = None

pose_bone: 'bpy.types.PoseBone' = None

pose_object: 'bpy.types.Object' = None

preferences: 'bpy.types.Preferences' = None

region: 'bpy.types.Region' = None

region_data: 'bpy.types.RegionView3D' = None

scene: 'bpy.types.Scene' = None

screen: 'bpy.types.Screen' = None

sculpt_object: 'bpy.types.Object' = None

selectable_objects: 'bpy.types.Object' = None

selected_bones: 'bpy.types.EditBone' = None

selected_editable_bones: 'bpy.types.EditBone' = None

selected_editable_fcurves: 'bpy.types.FCurve' = None

selected_editable_objects: 'bpy.types.Object' = None

selected_editable_sequences: 'bpy.types.Sequence' = None

selected_nodes: 'bpy.types.Node' = None

selected_objects: 'bpy.types.Object' = None

selected_pose_bones: 'bpy.types.PoseBone' = None

selected_pose_bones_from_active_object: 'bpy.types.PoseBone' = None

selected_sequences: 'bpy.types.Sequence' = None

selected_visible_fcurves: 'bpy.types.FCurve' = None

sequences: 'bpy.types.Sequence' = None

smoke: 'bpy.types.SmokeModifier' = None

soft_body: 'bpy.types.SoftBodyModifier' = None

space_data: 'bpy.types.Space' = None

speaker: 'bpy.types.Speaker' = None

texture: 'bpy.types.Texture' = None

texture_slot = None

texture_user: 'bpy.types.ID' = None

texture_user_property: 'bpy.types.Property' = None

tool_settings: 'bpy.types.ToolSettings' = None

vertex_paint_object: 'bpy.types.Object' = None

view_layer: 'bpy.types.ViewLayer' = None

visible_bones: 'bpy.types.EditBone' = None

visible_fcurves: 'bpy.types.FCurve' = None

visible_gpencil_layers: 'bpy.types.GPencilLayer' = None

visible_objects: 'bpy.types.Object' = None

visible_pose_bones: 'bpy.types.PoseBone' = None

weight_paint_object: 'bpy.types.Object' = None

window: 'bpy.types.Window' = None

window_manager: 'bpy.types.WindowManager' = None

workspace: 'bpy.types.WorkSpace' = None

world: 'bpy.types.World' = None
