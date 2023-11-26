import sys
import typing
import bpy.types
import bpy.ops.transform

GenericType = typing.TypeVar("GenericType")


def add(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        radius: typing.Optional[typing.Any] = 1.0,
        type: typing.Optional[typing.Union[str, int]] = 'EMPTY',
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add an object to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def add_modifier_menu(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__. :File: `startup/bl_ui/properties_data_modifier.py\:236 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_ui/properties_data_modifier.py#L236>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def add_named(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        linked: typing.Optional[typing.Union[bool, typing.Any]] = False,
        name: typing.Union[str, typing.Any] = "",
        session_uuid: typing.Optional[typing.Any] = 0,
        matrix: typing.Optional[typing.Any] = ((0.0, 0.0, 0.0,
                                                0.0), (0.0, 0.0, 0.0, 0.0),
                                               (0.0, 0.0, 0.0,
                                                0.0), (0.0, 0.0, 0.0, 0.0)),
        drop_x: typing.Optional[typing.Any] = 0,
        drop_y: typing.Optional[typing.Any] = 0):
    ''' Add named object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param linked: Linked, Duplicate object but not object data, linking to the original data
    :type linked: typing.Optional[typing.Union[bool, typing.Any]]
    :param name: Name, Name of the data-block to use by the operator
    :type name: typing.Union[str, typing.Any]
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: typing.Optional[typing.Any]
    :param matrix: Matrix
    :type matrix: typing.Optional[typing.Any]
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: typing.Optional[typing.Any]
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: typing.Optional[typing.Any]
    '''

    pass


def align(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          bb_quality: typing.Optional[typing.Union[bool, typing.Any]] = True,
          align_mode: typing.Optional[typing.Any] = 'OPT_2',
          relative_to: typing.Optional[typing.Any] = 'OPT_4',
          align_axis: typing.Optional[typing.Any] = {}):
    ''' Align objects :File: `startup/bl_operators/object_align.py\:393 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_align.py#L393>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param bb_quality: High Quality, Enables high quality but slow calculation of the bounding box for perfect results on complex shape meshes with rotation/scale
    :type bb_quality: typing.Optional[typing.Union[bool, typing.Any]]
    :param align_mode: Align Mode, Side of object to use for alignment
    :type align_mode: typing.Optional[typing.Any]
    :param relative_to: Relative To, Reference location to align to * ``OPT_1`` Scene Origin -- Use the scene origin as the position for the selected objects to align to. * ``OPT_2`` 3D Cursor -- Use the 3D cursor as the position for the selected objects to align to. * ``OPT_3`` Selection -- Use the selected objects as the position for the selected objects to align to. * ``OPT_4`` Active -- Use the active object as the position for the selected objects to align to.
    :type relative_to: typing.Optional[typing.Any]
    :param align_axis: Align, Align to axis
    :type align_axis: typing.Optional[typing.Any]
    '''

    pass


def anim_transforms_to_deltas(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Convert object animation for normal transforms to delta transforms :File: `startup/bl_operators/object.py\:781 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L781>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def armature_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        radius: typing.Optional[typing.Any] = 1.0,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add an armature object to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def assign_property_defaults(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        process_data: typing.Optional[typing.Union[bool, typing.Any]] = True,
        process_bones: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Assign the current values of custom properties as their defaults, for use as part of the rest pose state in NLA track mixing :File: `startup/bl_operators/object.py\:1006 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L1006>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param process_data: Process data properties
    :type process_data: typing.Optional[typing.Union[bool, typing.Any]]
    :param process_bones: Process bone properties
    :type process_bones: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def bake(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         type: typing.Optional[typing.Union[str, int]] = 'COMBINED',
         pass_filter: typing.Optional[typing.Any] = {},
         filepath: typing.Union[str, typing.Any] = "",
         width: typing.Optional[typing.Any] = 512,
         height: typing.Optional[typing.Any] = 512,
         margin: typing.Optional[typing.Any] = 16,
         margin_type: typing.Optional[typing.Union[str, int]] = 'EXTEND',
         use_selected_to_active: typing.Optional[typing.Union[bool, typing.
                                                              Any]] = False,
         max_ray_distance: typing.Optional[typing.Any] = 0.0,
         cage_extrusion: typing.Optional[typing.Any] = 0.0,
         cage_object: typing.Union[str, typing.Any] = "",
         normal_space: typing.Optional[typing.Union[str, int]] = 'TANGENT',
         normal_r: typing.Optional[typing.Union[str, int]] = 'POS_X',
         normal_g: typing.Optional[typing.Union[str, int]] = 'POS_Y',
         normal_b: typing.Optional[typing.Union[str, int]] = 'POS_Z',
         target: typing.Optional[typing.Union[str, int]] = 'IMAGE_TEXTURES',
         save_mode: typing.Optional[typing.Union[str, int]] = 'INTERNAL',
         use_clear: typing.Optional[typing.Union[bool, typing.Any]] = False,
         use_cage: typing.Optional[typing.Union[bool, typing.Any]] = False,
         use_split_materials: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
         use_automatic_name: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = False,
         uv_layer: typing.Union[str, typing.Any] = ""):
    ''' Bake image textures of selected objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type, Type of pass to bake, some of them may not be supported by the current render engine
    :type type: typing.Optional[typing.Union[str, int]]
    :param pass_filter: Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes
    :type pass_filter: typing.Optional[typing.Any]
    :param filepath: File Path, Image filepath to use when saving externally
    :type filepath: typing.Union[str, typing.Any]
    :param width: Width, Horizontal dimension of the baking map (external only)
    :type width: typing.Optional[typing.Any]
    :param height: Height, Vertical dimension of the baking map (external only)
    :type height: typing.Optional[typing.Any]
    :param margin: Margin, Extends the baked result as a post process filter
    :type margin: typing.Optional[typing.Any]
    :param margin_type: Margin Type, Which algorithm to use to generate the margin
    :type margin_type: typing.Optional[typing.Union[str, int]]
    :param use_selected_to_active: Selected to Active, Bake shading on the surface of selected objects to the active object
    :type use_selected_to_active: typing.Optional[typing.Union[bool, typing.Any]]
    :param max_ray_distance: Max Ray Distance, The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit
    :type max_ray_distance: typing.Optional[typing.Any]
    :param cage_extrusion: Cage Extrusion, Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes
    :type cage_extrusion: typing.Optional[typing.Any]
    :param cage_object: Cage Object, Object to use as cage, instead of calculating the cage from the active object with cage extrusion
    :type cage_object: typing.Union[str, typing.Any]
    :param normal_space: Normal Space, Choose normal space for baking
    :type normal_space: typing.Optional[typing.Union[str, int]]
    :param normal_r: R, Axis to bake in red channel
    :type normal_r: typing.Optional[typing.Union[str, int]]
    :param normal_g: G, Axis to bake in green channel
    :type normal_g: typing.Optional[typing.Union[str, int]]
    :param normal_b: B, Axis to bake in blue channel
    :type normal_b: typing.Optional[typing.Union[str, int]]
    :param target: Target, Where to output the baked map
    :type target: typing.Optional[typing.Union[str, int]]
    :param save_mode: Save Mode, Where to save baked image textures
    :type save_mode: typing.Optional[typing.Union[str, int]]
    :param use_clear: Clear, Clear images before baking (only for internal saving)
    :type use_clear: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_cage: Cage, Cast rays to active object from a cage
    :type use_cage: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_split_materials: Split Materials, Split baked maps per material, using material name in output file (external only)
    :type use_split_materials: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_automatic_name: Automatic Name, Automatically name the output file with the pass type
    :type use_automatic_name: typing.Optional[typing.Union[bool, typing.Any]]
    :param uv_layer: UV Layer, UV layer to override active
    :type uv_layer: typing.Union[str, typing.Any]
    '''

    pass


def bake_image(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Bake image textures of selected objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def camera_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add a camera object to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def clear_override_library(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def collection_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add an object to a new collection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def collection_external_asset_drop(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        session_uuid: typing.Optional[typing.Any] = 0,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        use_instance: typing.Optional[typing.Union[bool, typing.Any]] = True,
        drop_x: typing.Optional[typing.Any] = 0,
        drop_y: typing.Optional[typing.Any] = 0,
        collection: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Add the dragged collection to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: typing.Optional[typing.Any]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    :param use_instance: Instance, Add the dropped collection as collection instance
    :type use_instance: typing.Optional[typing.Union[bool, typing.Any]]
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: typing.Optional[typing.Any]
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: typing.Optional[typing.Any]
    :param collection: Collection
    :type collection: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def collection_instance_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "Collection",
        collection: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        session_uuid: typing.Optional[typing.Any] = 0,
        drop_x: typing.Optional[typing.Any] = 0,
        drop_y: typing.Optional[typing.Any] = 0):
    ''' Add a collection instance

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Collection name to add
    :type name: typing.Union[str, typing.Any]
    :param collection: Collection
    :type collection: typing.Optional[typing.Union[str, int, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: typing.Optional[typing.Any]
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: typing.Optional[typing.Any]
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: typing.Optional[typing.Any]
    '''

    pass


def collection_link(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        collection: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Add an object to an existing collection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param collection: Collection
    :type collection: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def collection_objects_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select all objects in collection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def collection_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove the active object from this collection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def collection_unlink(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Unlink the collection from all objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def constraint_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Add a constraint to the active object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def constraint_add_with_targets(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Add a constraint to the active object, with target (where applicable) set to the selected objects/bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def constraints_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear all constraints from the selected objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def constraints_copy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Copy constraints to other selected objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def convert(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        target: typing.Optional[typing.Any] = 'MESH',
        keep_original: typing.Optional[typing.Union[bool, typing.Any]] = False,
        merge_customdata: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        angle: typing.Optional[typing.Any] = 1.22173,
        thickness: typing.Optional[typing.Any] = 5,
        seams: typing.Optional[typing.Union[bool, typing.Any]] = False,
        faces: typing.Optional[typing.Union[bool, typing.Any]] = True,
        offset: typing.Optional[typing.Any] = 0.01):
    ''' Convert selected objects to another type

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param target: Target, Type of object to convert to * ``CURVE`` Curve -- Curve from Mesh or Text objects. * ``MESH`` Mesh -- Mesh from Curve, Surface, Metaball, or Text objects. * ``GPENCIL`` Grease Pencil -- Grease Pencil from Curve or Mesh objects. * ``CURVES`` Curves -- Curves from evaluated curve data.
    :type target: typing.Optional[typing.Any]
    :param keep_original: Keep Original, Keep original objects instead of replacing them
    :type keep_original: typing.Optional[typing.Union[bool, typing.Any]]
    :param merge_customdata: Merge UVs, Merge UV coordinates that share a vertex to account for imprecision in some modifiers
    :type merge_customdata: typing.Optional[typing.Union[bool, typing.Any]]
    :param angle: Threshold Angle, Threshold to determine ends of the strokes
    :type angle: typing.Optional[typing.Any]
    :param thickness: Thickness
    :type thickness: typing.Optional[typing.Any]
    :param seams: Only Seam Edges, Convert only seam edges
    :type seams: typing.Optional[typing.Union[bool, typing.Any]]
    :param faces: Export Faces, Export faces as filled strokes
    :type faces: typing.Optional[typing.Union[bool, typing.Any]]
    :param offset: Stroke Offset, Offset strokes from fill
    :type offset: typing.Optional[typing.Any]
    '''

    pass


def correctivesmooth_bind(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Bind base pose in Corrective Smooth modifier

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def curves_empty_hair_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add an empty curve object to the scene with the selected mesh as surface

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def curves_random_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add a curves object with random curves to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def data_instance_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        session_uuid: typing.Optional[typing.Any] = 0,
        type: typing.Optional[typing.Union[str, int]] = 'ACTION',
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        drop_x: typing.Optional[typing.Any] = 0,
        drop_y: typing.Optional[typing.Any] = 0):
    ''' Add an object data instance

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the data-block to use by the operator
    :type name: typing.Union[str, typing.Any]
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: typing.Optional[typing.Any]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: typing.Optional[typing.Any]
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: typing.Optional[typing.Any]
    '''

    pass


def data_transfer(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_reverse_transfer: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        use_freeze: typing.Optional[typing.Union[bool, typing.Any]] = False,
        data_type: typing.Optional[typing.Any] = '',
        use_create: typing.Optional[typing.Union[bool, typing.Any]] = True,
        vert_mapping: typing.Optional[typing.Union[str, int]] = 'NEAREST',
        edge_mapping: typing.Optional[typing.Union[str, int]] = 'NEAREST',
        loop_mapping: typing.Optional[typing.
                                      Union[str, int]] = 'NEAREST_POLYNOR',
        poly_mapping: typing.Optional[typing.Union[str, int]] = 'NEAREST',
        use_auto_transform: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = False,
        use_object_transform: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = True,
        use_max_distance: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        max_distance: typing.Optional[typing.Any] = 1.0,
        ray_radius: typing.Optional[typing.Any] = 0.0,
        islands_precision: typing.Optional[typing.Any] = 0.1,
        layers_select_src: typing.Optional[typing.Union[str, int]] = 'ACTIVE',
        layers_select_dst: typing.Optional[typing.Union[str, int]] = 'ACTIVE',
        mix_mode: typing.Optional[typing.Union[str, int]] = 'REPLACE',
        mix_factor: typing.Optional[typing.Any] = 1.0):
    ''' Transfer data layer(s) (weights, edge sharp, etc.) from active to selected meshes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_reverse_transfer: Reverse Transfer, Transfer from selected objects to active one
    :type use_reverse_transfer: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_freeze: Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry
    :type use_freeze: typing.Optional[typing.Union[bool, typing.Any]]
    :param data_type: Data Type, Which data to transfer * ``VGROUP_WEIGHTS`` Vertex Group(s) -- Transfer active or all vertex groups. * ``BEVEL_WEIGHT_VERT`` Bevel Weight -- Transfer bevel weights. * ``COLOR_VERTEX`` Colors -- Color Attributes. * ``SHARP_EDGE`` Sharp -- Transfer sharp mark. * ``SEAM`` UV Seam -- Transfer UV seam mark. * ``CREASE`` Subdivision Crease -- Transfer crease values. * ``BEVEL_WEIGHT_EDGE`` Bevel Weight -- Transfer bevel weights. * ``FREESTYLE_EDGE`` Freestyle Mark -- Transfer Freestyle edge mark. * ``CUSTOM_NORMAL`` Custom Normals -- Transfer custom normals. * ``COLOR_CORNER`` Colors -- Color Attributes. * ``UV`` UVs -- Transfer UV layers. * ``SMOOTH`` Smooth -- Transfer flat/smooth mark. * ``FREESTYLE_FACE`` Freestyle Mark -- Transfer Freestyle face mark.
    :type data_type: typing.Optional[typing.Any]
    :param use_create: Create Data, Add data layers on destination meshes if needed
    :type use_create: typing.Optional[typing.Union[bool, typing.Any]]
    :param vert_mapping: Vertex Mapping, Method used to map source vertices to destination ones
    :type vert_mapping: typing.Optional[typing.Union[str, int]]
    :param edge_mapping: Edge Mapping, Method used to map source edges to destination ones
    :type edge_mapping: typing.Optional[typing.Union[str, int]]
    :param loop_mapping: Face Corner Mapping, Method used to map source faces' corners to destination ones
    :type loop_mapping: typing.Optional[typing.Union[str, int]]
    :param poly_mapping: Face Mapping, Method used to map source faces to destination ones
    :type poly_mapping: typing.Optional[typing.Union[str, int]]
    :param use_auto_transform: Results will never be as good as manual matching of objects
    :type use_auto_transform: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_object_transform: Object Transform, Evaluate source and destination meshes in global space
    :type use_object_transform: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_max_distance: Only Neighbor Geometry, Source elements must be closer than given distance from destination one
    :type use_max_distance: typing.Optional[typing.Union[bool, typing.Any]]
    :param max_distance: Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings
    :type max_distance: typing.Optional[typing.Any]
    :param ray_radius: Ray Radius, 'Width' of rays (especially useful when raycasting against vertices or edges)
    :type ray_radius: typing.Optional[typing.Any]
    :param islands_precision: Islands Precision, Factor controlling precision of islands handling (the higher, the better the results)
    :type islands_precision: typing.Optional[typing.Any]
    :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types
    :type layers_select_src: typing.Optional[typing.Union[str, int]]
    :param layers_select_dst: Destination Layers Matching, How to match source and destination layers
    :type layers_select_dst: typing.Optional[typing.Union[str, int]]
    :param mix_mode: Mix Mode, How to affect destination elements with source values
    :type mix_mode: typing.Optional[typing.Union[str, int]]
    :param mix_factor: Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode)
    :type mix_factor: typing.Optional[typing.Any]
    '''

    pass


def datalayout_transfer(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = "",
        data_type: typing.Optional[typing.Any] = '',
        use_delete: typing.Optional[typing.Union[bool, typing.Any]] = False,
        layers_select_src: typing.Optional[typing.Union[str, int]] = 'ACTIVE',
        layers_select_dst: typing.Optional[typing.Union[str, int]] = 'ACTIVE'):
    ''' Transfer layout of data layer(s) from active to selected meshes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    :param data_type: Data Type, Which data to transfer * ``VGROUP_WEIGHTS`` Vertex Group(s) -- Transfer active or all vertex groups. * ``BEVEL_WEIGHT_VERT`` Bevel Weight -- Transfer bevel weights. * ``COLOR_VERTEX`` Colors -- Color Attributes. * ``SHARP_EDGE`` Sharp -- Transfer sharp mark. * ``SEAM`` UV Seam -- Transfer UV seam mark. * ``CREASE`` Subdivision Crease -- Transfer crease values. * ``BEVEL_WEIGHT_EDGE`` Bevel Weight -- Transfer bevel weights. * ``FREESTYLE_EDGE`` Freestyle Mark -- Transfer Freestyle edge mark. * ``CUSTOM_NORMAL`` Custom Normals -- Transfer custom normals. * ``COLOR_CORNER`` Colors -- Color Attributes. * ``UV`` UVs -- Transfer UV layers. * ``SMOOTH`` Smooth -- Transfer flat/smooth mark. * ``FREESTYLE_FACE`` Freestyle Mark -- Transfer Freestyle face mark.
    :type data_type: typing.Optional[typing.Any]
    :param use_delete: Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source
    :type use_delete: typing.Optional[typing.Union[bool, typing.Any]]
    :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types
    :type layers_select_src: typing.Optional[typing.Union[str, int]]
    :param layers_select_dst: Destination Layers Matching, How to match source and destination layers
    :type layers_select_dst: typing.Optional[typing.Union[str, int]]
    '''

    pass


def delete(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           use_global: typing.Optional[typing.Union[bool, typing.Any]] = False,
           confirm: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Delete selected objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_global: Delete Globally, Remove object from all scenes
    :type use_global: typing.Optional[typing.Union[bool, typing.Any]]
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def drop_geometry_nodes(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        session_uuid: typing.Optional[typing.Any] = 0,
        show_datablock_in_modifier: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = True):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param session_uuid: Session UUID, Session UUID of the geometry node group being dropped
    :type session_uuid: typing.Optional[typing.Any]
    :param show_datablock_in_modifier: Show the datablock selector in the modifier
    :type show_datablock_in_modifier: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def drop_named_image(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        relative_path: typing.Optional[typing.Union[bool, typing.Any]] = True,
        name: typing.Union[str, typing.Any] = "",
        session_uuid: typing.Optional[typing.Any] = 0,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add an empty image type to scene with data

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: Filepath, Path to image file
    :type filepath: typing.Union[str, typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Optional[typing.Union[bool, typing.Any]]
    :param name: Name, Name of the data-block to use by the operator
    :type name: typing.Union[str, typing.Any]
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: typing.Optional[typing.Any]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def drop_named_material(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        session_uuid: typing.Optional[typing.Any] = 0):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the data-block to use by the operator
    :type name: typing.Union[str, typing.Any]
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: typing.Optional[typing.Any]
    '''

    pass


def duplicate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        linked: typing.Optional[typing.Union[bool, typing.Any]] = False,
        mode: typing.Optional[typing.Union[str, int]] = 'TRANSLATION'):
    ''' Duplicate selected objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param linked: Linked, Duplicate object but not object data, linking to the original data
    :type linked: typing.Optional[typing.Union[bool, typing.Any]]
    :param mode: Mode
    :type mode: typing.Optional[typing.Union[str, int]]
    '''

    pass


def duplicate_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        OBJECT_OT_duplicate: typing.Optional['duplicate'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Duplicate the selected objects and move them

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
    :type OBJECT_OT_duplicate: typing.Optional['duplicate']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def duplicate_move_linked(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        OBJECT_OT_duplicate: typing.Optional['duplicate'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Duplicate the selected objects, but not their object data, and move them

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
    :type OBJECT_OT_duplicate: typing.Optional['duplicate']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def duplicates_make_real(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_base_parent: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        use_hierarchy: typing.Optional[typing.Union[bool, typing.
                                                    Any]] = False):
    ''' Make instanced objects attached to this object real

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_base_parent: Parent, Parent newly created objects to the original instancer
    :type use_base_parent: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_hierarchy: Keep Hierarchy, Maintain parent child relationships
    :type use_hierarchy: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def editmode_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Toggle object's edit mode

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def effector_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'FORCE',
        radius: typing.Optional[typing.Any] = 1.0,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add an empty object with a physics effector to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def empty_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'PLAIN_AXES',
        radius: typing.Optional[typing.Any] = 1.0,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add an empty object to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def explode_refresh(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Refresh data in the Explode modifier

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def forcefield_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Toggle object's force field

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def geometry_node_tree_copy_assign(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Copy the active geometry node group and assign it to the active modifier

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def geometry_nodes_input_attribute_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        input_name: typing.Union[str, typing.Any] = "",
        modifier_name: typing.Union[str, typing.Any] = ""):
    ''' Switch between an attribute and a single value to define the data for every element

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param input_name: Input Name
    :type input_name: typing.Union[str, typing.Any]
    :param modifier_name: Modifier Name
    :type modifier_name: typing.Union[str, typing.Any]
    '''

    pass


def geometry_nodes_move_to_nodes(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Move inputs and outputs from in the modifier to a new node group :File: `startup/bl_operators/geometry_nodes.py\:147 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/geometry_nodes.py#L147>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def gpencil_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        radius: typing.Optional[typing.Any] = 1.0,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        type: typing.Optional[typing.Union[str, int]] = 'EMPTY',
        use_in_front: typing.Optional[typing.Union[bool, typing.Any]] = True,
        stroke_depth_offset: typing.Optional[typing.Any] = 0.05,
        use_lights: typing.Optional[typing.Union[bool, typing.Any]] = False,
        stroke_depth_order: typing.Optional[typing.Any] = '3D'):
    ''' Add a Grease Pencil object to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    :param use_in_front: Show In Front, Show line art grease pencil in front of everything
    :type use_in_front: typing.Optional[typing.Union[bool, typing.Any]]
    :param stroke_depth_offset: Stroke Offset, Stroke offset for the line art modifier
    :type stroke_depth_offset: typing.Optional[typing.Any]
    :param use_lights: Use Lights, Use lights for this grease pencil object
    :type use_lights: typing.Optional[typing.Union[bool, typing.Any]]
    :param stroke_depth_order: Stroke Depth Order, Defines how the strokes are ordered in 3D space (for objects not displayed 'In Front') * ``2D`` 2D Layers -- Display strokes using grease pencil layers to define order. * ``3D`` 3D Location -- Display strokes using real 3D position in 3D space.
    :type stroke_depth_order: typing.Optional[typing.Any]
    '''

    pass


def gpencil_modifier_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'GP_THICK'):
    ''' Add a procedural operation/effect to the active grease pencil object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def gpencil_modifier_apply(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        apply_as: typing.Optional[typing.Any] = 'DATA',
        modifier: typing.Union[str, typing.Any] = "",
        report: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Apply modifier and remove from the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param apply_as: Apply As, How to apply the modifier to the geometry * ``DATA`` Object Data -- Apply modifier to the object's data. * ``SHAPE`` New Shape -- Apply deform-only modifier to a new shape on this object.
    :type apply_as: typing.Optional[typing.Any]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    :param report: Report, Create a notification after the operation
    :type report: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def gpencil_modifier_copy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Duplicate modifier at the same position in the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def gpencil_modifier_copy_to_selected(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Copy the modifier from the active object to all selected objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def gpencil_modifier_move_down(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Move modifier down in the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def gpencil_modifier_move_to_index(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = "",
        index: typing.Optional[typing.Any] = 0):
    ''' Change the modifier's position in the list so it evaluates after the set number of others

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    :param index: Index, The index to move the modifier to
    :type index: typing.Optional[typing.Any]
    '''

    pass


def gpencil_modifier_move_up(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Move modifier up in the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def gpencil_modifier_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = "",
        report: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Remove a modifier from the active grease pencil object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    :param report: Report, Create a notification after the operation
    :type report: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def grease_pencil_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'EMPTY',
        radius: typing.Optional[typing.Any] = 1.0,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add a Grease Pencil object to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def hide_collection(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        collection_index: typing.Optional[typing.Any] = -1,
        toggle: typing.Optional[typing.Union[bool, typing.Any]] = False,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Show only objects in collection (Shift to extend)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param collection_index: Collection Index, Index of the collection to change visibility
    :type collection_index: typing.Optional[typing.Any]
    :param toggle: Toggle, Toggle visibility
    :type toggle: typing.Optional[typing.Union[bool, typing.Any]]
    :param extend: Extend, Extend visibility
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def hide_render_clear_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reveal all render objects by setting the hide render flag :File: `startup/bl_operators/object.py\:688 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L688>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def hide_view_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        select: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Reveal temporarily hidden objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param select: Select
    :type select: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def hide_view_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        unselected: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Temporarily hide objects from the viewport

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def hook_add_newob(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Hook selected vertices to a newly created object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def hook_add_selob(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_bone: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Hook selected vertices to the first selected object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_bone: Active Bone, Assign the hook to the hook object's active bone
    :type use_bone: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def hook_assign(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Assign the selected vertices to a hook

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Modifier number to assign to
    :type modifier: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def hook_recenter(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Set hook center to cursor position

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Modifier number to assign to
    :type modifier: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def hook_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Remove a hook from the active object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Modifier number to remove
    :type modifier: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def hook_reset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Recalculate and clear offset transformation

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Modifier number to assign to
    :type modifier: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def hook_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Select affected vertices on mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Modifier number to remove
    :type modifier: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def instance_offset_from_cursor(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Set offset used for collection instances based on cursor position :File: `startup/bl_operators/object.py\:866 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L866>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def instance_offset_from_object(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Set offset used for collection instances based on the active object position :File: `startup/bl_operators/object.py\:898 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L898>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def instance_offset_to_cursor(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Set cursor position to the offset used for collection instances :File: `startup/bl_operators/object.py\:881 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L881>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def isolate_type_render(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Hide unselected render objects of same type as active by setting the hide render flag :File: `startup/bl_operators/object.py\:668 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L668>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def join(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None):
    ''' Join selected objects into active object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def join_shapes(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Copy the current resulting shape of another selected object to this one

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def join_uvs(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None):
    ''' Transfer UV Maps from active to selected objects (needs matching geometry) :File: `startup/bl_operators/object.py\:569 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L569>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def laplaciandeform_bind(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Bind mesh to system in laplacian deform modifier

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def light_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'POINT',
        radius: typing.Optional[typing.Any] = 1.0,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add a light object to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def light_linking_blocker_collection_new(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Create new light linking collection used by the active emitter

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def light_linking_blockers_link(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        link_state: typing.Optional[typing.Any] = 'INCLUDE'):
    ''' Light link selected blockers to the active emitter object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param link_state: Link State, State of the shadow linking * ``INCLUDE`` Include -- Include selected blockers to cast shadows from the active emitter. * ``EXCLUDE`` Exclude -- Exclude selected blockers from casting shadows from the active emitter.
    :type link_state: typing.Optional[typing.Any]
    '''

    pass


def light_linking_blockers_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select all objects which block light from this emitter

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def light_linking_receiver_collection_new(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Create new light linking collection used by the active emitter

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def light_linking_receivers_link(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        link_state: typing.Optional[typing.Any] = 'INCLUDE'):
    ''' Light link selected receivers to the active emitter object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param link_state: Link State, State of the light linking * ``INCLUDE`` Include -- Include selected receivers to receive light from the active emitter. * ``EXCLUDE`` Exclude -- Exclude selected receivers from receiving light from the active emitter.
    :type link_state: typing.Optional[typing.Any]
    '''

    pass


def light_linking_receivers_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select all objects which receive light from this emitter

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def light_linking_unlink_from_collection(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove this object or collection from the light linking collection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def lightprobe_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'CUBEMAP',
        radius: typing.Optional[typing.Any] = 1.0,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add a light probe object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``CUBEMAP`` Reflection Cubemap -- Reflection probe with spherical or cubic attenuation. * ``PLANAR`` Reflection Plane -- Planar reflection probe. * ``GRID`` Irradiance Volume -- Irradiance probe to capture diffuse indirect lighting.
    :type type: typing.Optional[typing.Any]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def lightprobe_cache_bake(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        delay: typing.Optional[typing.Any] = 0,
        subset: typing.Optional[typing.Any] = 'ALL'):
    ''' Bake irradiance volume light cache

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param delay: Delay, Delay in millisecond before baking starts
    :type delay: typing.Optional[typing.Any]
    :param subset: Subset, Subset of probes to update * ``ALL`` All Light Probes -- Bake all light probes. * ``DIRTY`` Dirty Only -- Only bake light probes that are marked as dirty. * ``SELECTED`` Selected Only -- Only bake selected light probes. * ``ACTIVE`` Active Only -- Only bake the active light probe.
    :type subset: typing.Optional[typing.Any]
    '''

    pass


def lightprobe_cache_free(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        subset: typing.Optional[typing.Any] = 'SELECTED'):
    ''' Delete cached indirect lighting

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param subset: Subset, Subset of probes to update * ``ALL`` All Light Probes -- Delete all light probes' baked lighting data. * ``SELECTED`` Selected Only -- Only delete selected light probes' baked lighting data. * ``ACTIVE`` Active Only -- Only delete the active light probe's baked lighting data.
    :type subset: typing.Optional[typing.Any]
    '''

    pass


def lineart_bake_strokes(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Bake Line Art for current GPencil object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def lineart_bake_strokes_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Bake all Grease Pencil objects that have a line art modifier

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def lineart_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear all strokes in current GPencil object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def lineart_clear_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear all strokes in all Grease Pencil objects that have a line art modifier

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def link_to_collection(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        collection_index: typing.Optional[typing.Any] = -1,
        is_new: typing.Optional[typing.Union[bool, typing.Any]] = False,
        new_collection_name: typing.Union[str, typing.Any] = ""):
    ''' Link objects to a collection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param collection_index: Collection Index, Index of the collection to move to
    :type collection_index: typing.Optional[typing.Any]
    :param is_new: New, Move objects to a new collection
    :type is_new: typing.Optional[typing.Union[bool, typing.Any]]
    :param new_collection_name: Name, Name of the newly added collection
    :type new_collection_name: typing.Union[str, typing.Any]
    '''

    pass


def load_background_image(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        view_align: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Add a reference image into the background behind objects :File: `startup/bl_operators/object.py\:930 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L930>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    :param filter_image: filter_image
    :type filter_image: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_movie: filter_movie
    :type filter_movie: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_folder: filter_folder
    :type filter_folder: typing.Optional[typing.Union[bool, typing.Any]]
    :param view_align: Align to View
    :type view_align: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def load_reference_image(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        view_align: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Add a reference image into the scene between objects :File: `startup/bl_operators/object.py\:930 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L930>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    :param filter_image: filter_image
    :type filter_image: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_movie: filter_movie
    :type filter_movie: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_folder: filter_folder
    :type filter_folder: typing.Optional[typing.Union[bool, typing.Any]]
    :param view_align: Align to View
    :type view_align: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def location_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        clear_delta: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Clear the object's location

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param clear_delta: Clear Delta, Clear delta location in addition to clearing the normal location transform
    :type clear_delta: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def make_dupli_face(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Convert objects into instanced faces :File: `startup/bl_operators/object.py\:651 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L651>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def make_links_data(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'OBDATA'):
    ''' Transfer data from active object to selected objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``OBDATA`` Link Object Data -- Replace assigned Object Data. * ``MATERIAL`` Link Materials -- Replace assigned Materials. * ``ANIMATION`` Link Animation Data -- Replace assigned Animation Data. * ``GROUPS`` Link Collections -- Replace assigned Collections. * ``DUPLICOLLECTION`` Link Instance Collection -- Replace assigned Collection Instance. * ``FONTS`` Link Fonts to Text -- Replace Text object Fonts. * ``MODIFIERS`` Copy Modifiers -- Replace Modifiers. * ``EFFECTS`` Copy Grease Pencil Effects -- Replace Grease Pencil Effects.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def make_links_scene(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        scene: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Link selection to another scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param scene: Scene
    :type scene: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def make_local(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'SELECT_OBJECT'):
    ''' Make library linked data-blocks local to this file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def make_override_library(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        collection: typing.Optional[typing.Any] = 0):
    ''' Create a local override of the selected linked objects, and their hierarchy of dependencies

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param collection: Override Collection, Session UUID of the directly linked collection containing the selected object, to make an override from
    :type collection: typing.Optional[typing.Any]
    '''

    pass


def make_single_user(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'SELECTED_OBJECTS',
        object: typing.Optional[typing.Union[bool, typing.Any]] = False,
        obdata: typing.Optional[typing.Union[bool, typing.Any]] = False,
        material: typing.Optional[typing.Union[bool, typing.Any]] = False,
        animation: typing.Optional[typing.Union[bool, typing.Any]] = False,
        obdata_animation: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False):
    ''' Make linked data local to each object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param object: Object, Make single user objects
    :type object: typing.Optional[typing.Union[bool, typing.Any]]
    :param obdata: Object Data, Make single user object data
    :type obdata: typing.Optional[typing.Union[bool, typing.Any]]
    :param material: Materials, Make materials local to each data-block
    :type material: typing.Optional[typing.Union[bool, typing.Any]]
    :param animation: Object Animation, Make object animation data local to each object
    :type animation: typing.Optional[typing.Union[bool, typing.Any]]
    :param obdata_animation: Object Data Animation, Make object data (mesh, curve etc.) animation data local to each object
    :type obdata_animation: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def material_slot_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add a new material slot

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_slot_assign(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Assign active material slot to selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_slot_copy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Copy material to selected objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_slot_deselect(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Deselect by active material slot

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_slot_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        direction: typing.Optional[typing.Any] = 'UP'):
    ''' Move the active material up/down in the list

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Direction to move the active material towards
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def material_slot_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove the selected material slot

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_slot_remove_unused(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove unused material slots

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_slot_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select by active material slot

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def meshdeform_bind(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Bind mesh to cage in mesh deform modifier

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def metaball_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'BALL',
        radius: typing.Optional[typing.Any] = 2.0,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add an metaball object to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Primitive
    :type type: typing.Optional[typing.Union[str, int]]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def mode_set(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None,
             *,
             mode: typing.Optional[typing.Union[str, int]] = 'OBJECT',
             toggle: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Sets the object interaction mode

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Union[str, int]]
    :param toggle: Toggle
    :type toggle: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def mode_set_with_submode(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Union[str, int]] = 'OBJECT',
        toggle: typing.Optional[typing.Union[bool, typing.Any]] = False,
        mesh_select_mode: typing.Optional[typing.Any] = {}):
    ''' Sets the object interaction mode

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Union[str, int]]
    :param toggle: Toggle
    :type toggle: typing.Optional[typing.Union[bool, typing.Any]]
    :param mesh_select_mode: Mesh Mode
    :type mesh_select_mode: typing.Optional[typing.Any]
    '''

    pass


def modifier_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'SUBSURF'):
    ''' Add a procedural operation/effect to the active object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def modifier_add_node_group(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        asset_library_type: typing.Optional[typing.Union[str, int]] = 'LOCAL',
        asset_library_identifier: typing.Union[str, typing.Any] = "",
        relative_asset_identifier: typing.Union[str, typing.Any] = "",
        session_uuid: typing.Optional[typing.Any] = 0):
    ''' Add a procedural operation/effect to the active object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param asset_library_type: Asset Library Type
    :type asset_library_type: typing.Optional[typing.Union[str, int]]
    :param asset_library_identifier: Asset Library Identifier
    :type asset_library_identifier: typing.Union[str, typing.Any]
    :param relative_asset_identifier: Relative Asset Identifier
    :type relative_asset_identifier: typing.Union[str, typing.Any]
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: typing.Optional[typing.Any]
    '''

    pass


def modifier_apply(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = "",
        report: typing.Optional[typing.Union[bool, typing.Any]] = False,
        merge_customdata: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        single_user: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Apply modifier and remove from the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    :param report: Report, Create a notification after the operation
    :type report: typing.Optional[typing.Union[bool, typing.Any]]
    :param merge_customdata: Merge UVs, For mesh objects, merge UV coordinates that share a vertex to account for imprecision in some modifiers
    :type merge_customdata: typing.Optional[typing.Union[bool, typing.Any]]
    :param single_user: Make Data Single User, Make the object's data single user if needed
    :type single_user: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def modifier_apply_as_shapekey(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        keep_modifier: typing.Optional[typing.Union[bool, typing.Any]] = False,
        modifier: typing.Union[str, typing.Any] = "",
        report: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Apply modifier as a new shape key and remove from the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param keep_modifier: Keep Modifier, Do not remove the modifier from stack
    :type keep_modifier: typing.Optional[typing.Union[bool, typing.Any]]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    :param report: Report, Create a notification after the operation
    :type report: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def modifier_convert(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Convert particles to a mesh object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def modifier_copy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Duplicate modifier at the same position in the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def modifier_copy_to_selected(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Copy the modifier from the active object to all selected objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def modifier_move_down(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Move modifier down in the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def modifier_move_to_index(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = "",
        index: typing.Optional[typing.Any] = 0):
    ''' Change the modifier's index in the stack so it evaluates after the set number of others

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    :param index: Index, The index to move the modifier to
    :type index: typing.Optional[typing.Any]
    '''

    pass


def modifier_move_up(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Move modifier up in the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def modifier_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = "",
        report: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Remove a modifier from the active object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    :param report: Report, Create a notification after the operation
    :type report: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def modifier_set_active(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Activate the modifier to use as the context

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def move_to_collection(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        collection_index: typing.Optional[typing.Any] = -1,
        is_new: typing.Optional[typing.Union[bool, typing.Any]] = False,
        new_collection_name: typing.Union[str, typing.Any] = ""):
    ''' Move objects to a collection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param collection_index: Collection Index, Index of the collection to move to
    :type collection_index: typing.Optional[typing.Any]
    :param is_new: New, Move objects to a new collection
    :type is_new: typing.Optional[typing.Union[bool, typing.Any]]
    :param new_collection_name: Name, Name of the newly added collection
    :type new_collection_name: typing.Union[str, typing.Any]
    '''

    pass


def multires_base_apply(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Modify the base mesh to conform to the displaced mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def multires_external_pack(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Pack displacements from an external file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def multires_external_save(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        hide_props_region: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        check_existing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_sound: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 9,
        relative_path: typing.Optional[typing.Union[bool, typing.Any]] = True,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Save displacements to an external file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: typing.Optional[typing.Union[bool, typing.Any]]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_image: Filter image files
    :type filter_image: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_python: Filter Python files
    :type filter_python: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_font: Filter font files
    :type filter_font: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_text: Filter text files
    :type filter_text: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Optional[typing.Union[bool, typing.Any]]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Optional[typing.Union[bool, typing.Any]]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Optional[typing.Union[str, int, typing.Any]]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def multires_higher_levels_delete(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Deletes the higher resolution mesh, potential loss of detail

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def multires_rebuild_subdiv(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Rebuilds all possible subdivisions levels to generate a lower resolution base mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def multires_reshape(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Copy vertex coordinates from other object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def multires_subdivide(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = "",
        mode: typing.Optional[typing.Any] = 'CATMULL_CLARK'):
    ''' Add a new level of subdivision

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    :param mode: Subdivision Mode, How the mesh is going to be subdivided to create a new level * ``CATMULL_CLARK`` Catmull-Clark -- Create a new level using Catmull-Clark subdivisions. * ``SIMPLE`` Simple -- Create a new level using simple subdivisions. * ``LINEAR`` Linear -- Create a new level using linear interpolation of the sculpted displacement.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def multires_unsubdivide(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Rebuild a lower subdivision level of the current base mesh

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def ocean_bake(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = "",
        free: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Bake an image sequence of ocean data

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    :param free: Free, Free the bake, rather than generating it
    :type free: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def origin_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear the object's origin

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def origin_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'GEOMETRY_ORIGIN',
        center: typing.Optional[typing.Any] = 'MEDIAN'):
    ''' Set the object's origin, by either moving the data, or set to center of data, or use 3D cursor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``GEOMETRY_ORIGIN`` Geometry to Origin -- Move object geometry to object origin. * ``ORIGIN_GEOMETRY`` Origin to Geometry -- Calculate the center of geometry based on the current pivot point (median, otherwise bounding box). * ``ORIGIN_CURSOR`` Origin to 3D Cursor -- Move object origin to position of the 3D cursor. * ``ORIGIN_CENTER_OF_MASS`` Origin to Center of Mass (Surface) -- Calculate the center of mass from the surface area. * ``ORIGIN_CENTER_OF_VOLUME`` Origin to Center of Mass (Volume) -- Calculate the center of mass from the volume (must be manifold geometry with consistent normals).
    :type type: typing.Optional[typing.Any]
    :param center: Center
    :type center: typing.Optional[typing.Any]
    '''

    pass


def parent_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'CLEAR'):
    ''' Clear the object's parenting

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``CLEAR`` Clear Parent -- Completely clear the parenting relationship, including involved modifiers if any. * ``CLEAR_KEEP_TRANSFORM`` Clear and Keep Transformation -- As 'Clear Parent', but keep the current visual transformations of the object. * ``CLEAR_INVERSE`` Clear Parent Inverse -- Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def parent_inverse_apply(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Apply the object's parent inverse to its data

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def parent_no_inverse_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        confirm: typing.Optional[typing.Union[bool, typing.Any]] = True,
        keep_transform: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False):
    ''' Set the object's parenting without setting the inverse parent correction

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: typing.Optional[typing.Union[bool, typing.Any]]
    :param keep_transform: Keep Transform, Preserve the world transform throughout parenting
    :type keep_transform: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def parent_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'OBJECT',
        xmirror: typing.Optional[typing.Union[bool, typing.Any]] = False,
        keep_transform: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False):
    ''' Set the object's parenting

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param xmirror: X Mirror, Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation
    :type xmirror: typing.Optional[typing.Union[bool, typing.Any]]
    :param keep_transform: Keep Transform, Apply transformation before parenting
    :type keep_transform: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def particle_system_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add a particle system

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def particle_system_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove the selected particle system

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def paths_calculate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        display_type: typing.Optional[typing.Union[str, int]] = 'RANGE',
        range: typing.Optional[typing.Union[str, int]] = 'SCENE'):
    ''' Generate motion paths for the selected objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param display_type: Display type
    :type display_type: typing.Optional[typing.Union[str, int]]
    :param range: Computation Range
    :type range: typing.Optional[typing.Union[str, int]]
    '''

    pass


def paths_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        only_selected: typing.Optional[typing.Union[bool, typing.
                                                    Any]] = False):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param only_selected: Only Selected, Only clear motion paths of selected objects
    :type only_selected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def paths_update(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Recalculate motion paths for selected objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def paths_update_visible(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Recalculate all visible motion paths for objects and poses

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def pointcloud_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add a point cloud object to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def posemode_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Enable or disable posing/selecting bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def quadriflow_remesh(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_mesh_symmetry: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        use_preserve_sharp: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = False,
        use_preserve_boundary: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        preserve_paint_mask: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = False,
        smooth_normals: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        mode: typing.Optional[typing.Any] = 'FACES',
        target_ratio: typing.Optional[typing.Any] = 1.0,
        target_edge_length: typing.Optional[typing.Any] = 0.1,
        target_faces: typing.Optional[typing.Any] = 4000,
        mesh_area: typing.Optional[typing.Any] = -1.0,
        seed: typing.Optional[typing.Any] = 0):
    ''' Create a new quad based mesh using the surface data of the current mesh. All data layers will be lost

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_mesh_symmetry: Use Mesh Symmetry, Generates a symmetrical mesh using the mesh symmetry configuration
    :type use_mesh_symmetry: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_preserve_sharp: Preserve Sharp, Try to preserve sharp features on the mesh
    :type use_preserve_sharp: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_preserve_boundary: Preserve Mesh Boundary, Try to preserve mesh boundary on the mesh
    :type use_preserve_boundary: typing.Optional[typing.Union[bool, typing.Any]]
    :param preserve_paint_mask: Preserve Paint Mask, Reproject the paint mask onto the new mesh
    :type preserve_paint_mask: typing.Optional[typing.Union[bool, typing.Any]]
    :param smooth_normals: Smooth Normals, Set the output mesh normals to smooth
    :type smooth_normals: typing.Optional[typing.Union[bool, typing.Any]]
    :param mode: Mode, How to specify the amount of detail for the new mesh * ``RATIO`` Ratio -- Specify target number of faces relative to the current mesh. * ``EDGE`` Edge Length -- Input target edge length in the new mesh. * ``FACES`` Faces -- Input target number of faces in the new mesh.
    :type mode: typing.Optional[typing.Any]
    :param target_ratio: Ratio, Relative number of faces compared to the current mesh
    :type target_ratio: typing.Optional[typing.Any]
    :param target_edge_length: Edge Length, Target edge length in the new mesh
    :type target_edge_length: typing.Optional[typing.Any]
    :param target_faces: Number of Faces, Approximate number of faces (quads) in the new mesh
    :type target_faces: typing.Optional[typing.Any]
    :param mesh_area: Old Object Face Area, This property is only used to cache the object area for later calculations
    :type mesh_area: typing.Optional[typing.Any]
    :param seed: Seed, Random seed to use with the solver. Different seeds will cause the remesher to come up with different quad layouts on the mesh
    :type seed: typing.Optional[typing.Any]
    '''

    pass


def quick_explode(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        style: typing.Optional[typing.Any] = 'EXPLODE',
        amount: typing.Optional[typing.Any] = 100,
        frame_duration: typing.Optional[typing.Any] = 50,
        frame_start: typing.Optional[typing.Any] = 1,
        frame_end: typing.Optional[typing.Any] = 10,
        velocity: typing.Optional[typing.Any] = 1.0,
        fade: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Make selected objects explode :File: `startup/bl_operators/object_quick_effects.py\:260 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L260>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param style: Explode Style
    :type style: typing.Optional[typing.Any]
    :param amount: Number of Pieces
    :type amount: typing.Optional[typing.Any]
    :param frame_duration: Duration
    :type frame_duration: typing.Optional[typing.Any]
    :param frame_start: Start Frame
    :type frame_start: typing.Optional[typing.Any]
    :param frame_end: End Frame
    :type frame_end: typing.Optional[typing.Any]
    :param velocity: Outwards Velocity
    :type velocity: typing.Optional[typing.Any]
    :param fade: Fade, Fade the pieces over time
    :type fade: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def quick_fur(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        density: typing.Optional[typing.Any] = 'MEDIUM',
        length: typing.Optional[typing.Any] = 0.1,
        radius: typing.Optional[typing.Any] = 0.001,
        view_percentage: typing.Optional[typing.Any] = 1.0,
        apply_hair_guides: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        use_noise: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_frizz: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Add a fur setup to the selected objects :File: `startup/bl_operators/object_quick_effects.py\:91 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L91>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param density: Density
    :type density: typing.Optional[typing.Any]
    :param length: Length
    :type length: typing.Optional[typing.Any]
    :param radius: Hair Radius
    :type radius: typing.Optional[typing.Any]
    :param view_percentage: View Percentage
    :type view_percentage: typing.Optional[typing.Any]
    :param apply_hair_guides: Apply Hair Guides
    :type apply_hair_guides: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_noise: Noise
    :type use_noise: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_frizz: Frizz
    :type use_frizz: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def quick_liquid(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        show_flows: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Make selected objects liquid :File: `startup/bl_operators/object_quick_effects.py\:548 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L548>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param show_flows: Render Liquid Objects, Keep the liquid objects visible during rendering
    :type show_flows: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def quick_smoke(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        style: typing.Optional[typing.Any] = 'SMOKE',
        show_flows: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Use selected objects as smoke emitters :File: `startup/bl_operators/object_quick_effects.py\:440 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L440>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param style: Smoke Style
    :type style: typing.Optional[typing.Any]
    :param show_flows: Render Smoke Objects, Keep the smoke objects visible during rendering
    :type show_flows: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def randomize_transform(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        random_seed: typing.Optional[typing.Any] = 0,
        use_delta: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_loc: typing.Optional[typing.Union[bool, typing.Any]] = True,
        loc: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        use_rot: typing.Optional[typing.Union[bool, typing.Any]] = True,
        rot: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        use_scale: typing.Optional[typing.Union[bool, typing.Any]] = True,
        scale_even: typing.Optional[typing.Union[bool, typing.Any]] = False,
        scale: typing.Optional[typing.Any] = (1.0, 1.0, 1.0)):
    ''' Randomize objects location, rotation, and scale :File: `startup/bl_operators/object_randomize_transform.py\:164 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_randomize_transform.py#L164>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param random_seed: Random Seed, Seed value for the random generator
    :type random_seed: typing.Optional[typing.Any]
    :param use_delta: Transform Delta, Randomize delta transform values instead of regular transform
    :type use_delta: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_loc: Randomize Location, Randomize the location values
    :type use_loc: typing.Optional[typing.Union[bool, typing.Any]]
    :param loc: Location, Maximum distance the objects can spread over each axis
    :type loc: typing.Optional[typing.Any]
    :param use_rot: Randomize Rotation, Randomize the rotation values
    :type use_rot: typing.Optional[typing.Union[bool, typing.Any]]
    :param rot: Rotation, Maximum rotation over each axis
    :type rot: typing.Optional[typing.Any]
    :param use_scale: Randomize Scale, Randomize the scale values
    :type use_scale: typing.Optional[typing.Union[bool, typing.Any]]
    :param scale_even: Scale Even, Use the same scale value for all axis
    :type scale_even: typing.Optional[typing.Union[bool, typing.Any]]
    :param scale: Scale, Maximum scale randomization over each axis
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def reset_override_library(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reset the selected local overrides to their linked references values

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def rotation_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        clear_delta: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Clear the object's rotation

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param clear_delta: Clear Delta, Clear delta rotation in addition to clearing the normal rotation transform
    :type clear_delta: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def scale_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        clear_delta: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Clear the object's scale

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param clear_delta: Clear Delta, Clear delta scale in addition to clearing the normal scale transform
    :type clear_delta: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Change selection of all visible objects in scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param action: Action, Selection action to execute * ``TOGGLE`` Toggle -- Toggle selection for all elements. * ``SELECT`` Select -- Select all elements. * ``DESELECT`` Deselect -- Deselect all elements. * ``INVERT`` Invert -- Invert selection of all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_by_type(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False,
        type: typing.Optional[typing.Union[str, int]] = 'MESH'):
    ''' Select all visible objects that are of a type

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def select_camera(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select the active camera :File: `startup/bl_operators/object.py\:117 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L117>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend the selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_grouped(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False,
        type: typing.Optional[typing.Any] = 'CHILDREN_RECURSIVE'):
    ''' Select all visible objects grouped by various properties

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param type: Type * ``CHILDREN_RECURSIVE`` Children. * ``CHILDREN`` Immediate Children. * ``PARENT`` Parent. * ``SIBLINGS`` Siblings -- Shared parent. * ``TYPE`` Type -- Shared object type. * ``COLLECTION`` Collection -- Shared collection. * ``HOOK`` Hook. * ``PASS`` Pass -- Render pass index. * ``COLOR`` Color -- Object color. * ``KEYINGSET`` Keying Set -- Objects included in active Keying Set. * ``LIGHT_TYPE`` Light Type -- Matching light types.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def select_hierarchy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        direction: typing.Optional[typing.Any] = 'PARENT',
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select object relative to the active object's position in the hierarchy :File: `startup/bl_operators/object.py\:167 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L167>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Direction to select in the hierarchy
    :type direction: typing.Optional[typing.Any]
    :param extend: Extend, Extend the existing selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_less(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Deselect objects at the boundaries of parent/child relationships

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_linked(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False,
        type: typing.Optional[typing.Any] = 'OBDATA'):
    ''' Select all visible objects that are linked

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def select_mirror(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select the mirror objects of the selected object e.g. "L.sword" and "R.sword"

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_more(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select connected parent/child objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_pattern(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        pattern: typing.Union[str, typing.Any] = "*",
        case_sensitive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Select objects matching a naming pattern :File: `startup/bl_operators/object.py\:40 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L40>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param pattern: Pattern, Name filter using '*', '?' and '[abc]' unix style wildcards
    :type pattern: typing.Union[str, typing.Any]
    :param case_sensitive: Case Sensitive, Do a case sensitive compare
    :type case_sensitive: typing.Optional[typing.Union[bool, typing.Any]]
    :param extend: Extend, Extend the existing selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_random(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        ratio: typing.Optional[typing.Any] = 0.5,
        seed: typing.Optional[typing.Any] = 0,
        action: typing.Optional[typing.Any] = 'SELECT'):
    ''' Select or deselect random visible objects

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param ratio: Ratio, Portion of items to select randomly
    :type ratio: typing.Optional[typing.Any]
    :param seed: Random Seed, Seed for the random number generator
    :type seed: typing.Optional[typing.Any]
    :param action: Action, Selection action to execute * ``SELECT`` Select -- Select all elements. * ``DESELECT`` Deselect -- Deselect all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_same_collection(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        collection: typing.Union[str, typing.Any] = ""):
    ''' Select object in the same collection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param collection: Collection, Name of the collection to select
    :type collection: typing.Union[str, typing.Any]
    '''

    pass


def shade_flat(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Render and display faces uniform, using Face Normals

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def shade_smooth(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_auto_smooth: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        auto_smooth_angle: typing.Optional[typing.Any] = 0.523599):
    ''' Render and display faces smooth, using interpolated Vertex Normals

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_auto_smooth: Auto Smooth, Enable automatic smooth based on smooth/sharp faces/edges and angle between faces
    :type use_auto_smooth: typing.Optional[typing.Union[bool, typing.Any]]
    :param auto_smooth_angle: Angle, Maximum angle between face normals that will be considered as smooth (unused if custom split normals data are available)
    :type auto_smooth_angle: typing.Optional[typing.Any]
    '''

    pass


def shaderfx_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'FX_BLUR'):
    ''' Add a visual effect to the active object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def shaderfx_copy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        shaderfx: typing.Union[str, typing.Any] = ""):
    ''' Duplicate effect at the same position in the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: typing.Union[str, typing.Any]
    '''

    pass


def shaderfx_move_down(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        shaderfx: typing.Union[str, typing.Any] = ""):
    ''' Move effect down in the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: typing.Union[str, typing.Any]
    '''

    pass


def shaderfx_move_to_index(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        shaderfx: typing.Union[str, typing.Any] = "",
        index: typing.Optional[typing.Any] = 0):
    ''' Change the effect's position in the list so it evaluates after the set number of others

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: typing.Union[str, typing.Any]
    :param index: Index, The index to move the effect to
    :type index: typing.Optional[typing.Any]
    '''

    pass


def shaderfx_move_up(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        shaderfx: typing.Union[str, typing.Any] = ""):
    ''' Move effect up in the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: typing.Union[str, typing.Any]
    '''

    pass


def shaderfx_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        shaderfx: typing.Union[str, typing.Any] = "",
        report: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Remove a effect from the active grease pencil object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: typing.Union[str, typing.Any]
    :param report: Report, Create a notification after the operation
    :type report: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def shape_key_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        from_mix: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Add shape key to the object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param from_mix: From Mix, Create the new shape key from the existing mix of keys
    :type from_mix: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def shape_key_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear weights for all shape keys

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def shape_key_mirror(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_topology: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Mirror the current shape key along the local X axis

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
    :type use_topology: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def shape_key_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'TOP'):
    ''' Move the active shape key up/down in the list

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``TOP`` Top -- Top of the list. * ``UP`` Up. * ``DOWN`` Down. * ``BOTTOM`` Bottom -- Bottom of the list.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def shape_key_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        all: typing.Optional[typing.Union[bool, typing.Any]] = False,
        apply_mix: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Remove shape key from the object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param all: All, Remove all shape keys
    :type all: typing.Optional[typing.Union[bool, typing.Any]]
    :param apply_mix: Apply Mix, Apply current mix of shape keys to the geometry before removing them
    :type apply_mix: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def shape_key_retime(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Resets the timing for absolute shape keys

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def shape_key_transfer(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'OFFSET',
        use_clamp: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Copy the active shape key of another selected object to this one :File: `startup/bl_operators/object.py\:464 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L464>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Transformation Mode, Relative shape positions to the new shape method * ``OFFSET`` Offset -- Apply the relative positional offset. * ``RELATIVE_FACE`` Relative Face -- Calculate relative position (using faces). * ``RELATIVE_EDGE`` Relative Edge -- Calculate relative position (using edges).
    :type mode: typing.Optional[typing.Any]
    :param use_clamp: Clamp Offset, Clamp the transformation to the distance each vertex moves in the original shape
    :type use_clamp: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def simulation_nodes_cache_bake(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        selected: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Bake simulations in geometry nodes modifiers

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param selected: Selected, Bake cache on all selected objects
    :type selected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def simulation_nodes_cache_bake_single(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        session_uuid: typing.Optional[typing.Any] = 0,
        modifier_name: typing.Union[str, typing.Any] = "",
        bake_id: typing.Optional[typing.Any] = 0):
    ''' Bake a single simulation zone

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: typing.Optional[typing.Any]
    :param modifier_name: Modifier Name, Name of the modifier that contains the node to bake
    :type modifier_name: typing.Union[str, typing.Any]
    :param bake_id: Bake ID, Nested node id of the node to bake
    :type bake_id: typing.Optional[typing.Any]
    '''

    pass


def simulation_nodes_cache_calculate_to_frame(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        selected: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Calculate simulations in geometry nodes modifiers from the start to current frame

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param selected: Selected, Calculate all selected objects instead of just the active object
    :type selected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def simulation_nodes_cache_delete(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        selected: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Delete cached/baked simulations in geometry nodes modifiers

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param selected: Selected, Delete cache on all selected objects
    :type selected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def simulation_nodes_cache_delete_single(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        session_uuid: typing.Optional[typing.Any] = 0,
        modifier_name: typing.Union[str, typing.Any] = "",
        bake_id: typing.Optional[typing.Any] = 0):
    ''' Delete simulation data of a single simulation zone

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: typing.Optional[typing.Any]
    :param modifier_name: Modifier Name, Name of the modifier that contains the node
    :type modifier_name: typing.Union[str, typing.Any]
    :param bake_id: Bake ID, Nested node id of the bake to delete
    :type bake_id: typing.Optional[typing.Any]
    '''

    pass


def skin_armature_create(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Create an armature that parallels the skin layout

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def skin_loose_mark_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        action: typing.Optional[typing.Any] = 'MARK'):
    ''' Mark/clear selected vertices as loose

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param action: Action * ``MARK`` Mark -- Mark selected vertices as loose. * ``CLEAR`` Clear -- Set selected vertices as not loose.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def skin_radii_equalize(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Make skin radii of selected vertices equal on each axis

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def skin_root_mark(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Mark selected vertices as roots

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def speaker_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add a speaker object to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def subdivision_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        level: typing.Optional[typing.Any] = 1,
        relative: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Sets a Subdivision Surface level (1 to 5) :File: `startup/bl_operators/object.py\:235 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L235>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param level: Level
    :type level: typing.Optional[typing.Any]
    :param relative: Relative, Apply the subdivision surface level as an offset relative to the current level
    :type relative: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def surfacedeform_bind(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Bind mesh to target in surface deform modifier

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def text_add(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None,
             *,
             radius: typing.Optional[typing.Any] = 1.0,
             enter_editmode: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = False,
             align: typing.Optional[typing.Any] = 'WORLD',
             location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
             rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
             scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add a text object to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def track_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'CLEAR'):
    ''' Clear tracking constraint or flag from object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def track_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'DAMPTRACK'):
    ''' Make the object track another object, using various methods/constraints

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def transfer_mode(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_flash_on_transfer: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = True):
    ''' Switches the active object and assigns the same mode to a new one under the mouse cursor, leaving the active mode in the current one

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_flash_on_transfer: Flash On Transfer, Flash the target object when transferring the mode
    :type use_flash_on_transfer: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def transform_apply(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        location: typing.Optional[typing.Union[bool, typing.Any]] = True,
        rotation: typing.Optional[typing.Union[bool, typing.Any]] = True,
        scale: typing.Optional[typing.Union[bool, typing.Any]] = True,
        properties: typing.Optional[typing.Union[bool, typing.Any]] = True,
        isolate_users: typing.Optional[typing.Union[bool, typing.
                                                    Any]] = False):
    ''' Apply the object's transformation to its data

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param location: Location
    :type location: typing.Optional[typing.Union[bool, typing.Any]]
    :param rotation: Rotation
    :type rotation: typing.Optional[typing.Union[bool, typing.Any]]
    :param scale: Scale
    :type scale: typing.Optional[typing.Union[bool, typing.Any]]
    :param properties: Apply Properties, Modify properties such as curve vertex radius, font size and bone envelope
    :type properties: typing.Optional[typing.Union[bool, typing.Any]]
    :param isolate_users: Isolate Multi User Data, Create new object-data users if needed
    :type isolate_users: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def transform_axis_target(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Interactively point cameras and lights to a location (Ctrl translates)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def transform_to_mouse(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        session_uuid: typing.Optional[typing.Any] = 0,
        matrix: typing.Optional[typing.Any] = ((0.0, 0.0, 0.0,
                                                0.0), (0.0, 0.0, 0.0, 0.0),
                                               (0.0, 0.0, 0.0,
                                                0.0), (0.0, 0.0, 0.0, 0.0)),
        drop_x: typing.Optional[typing.Any] = 0,
        drop_y: typing.Optional[typing.Any] = 0):
    ''' Snap selected item(s) to the mouse location

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Name, Object name to place (uses the active object when this and 'session_uuid' are unset)
    :type name: typing.Union[str, typing.Any]
    :param session_uuid: Session UUID, Session UUID of the object to place (uses the active object when this and 'name' are unset)
    :type session_uuid: typing.Optional[typing.Any]
    :param matrix: Matrix
    :type matrix: typing.Optional[typing.Any]
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: typing.Optional[typing.Any]
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: typing.Optional[typing.Any]
    '''

    pass


def transforms_to_deltas(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'ALL',
        reset_values: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Convert normal object transforms to delta transforms, any existing delta transforms will be included as well :File: `startup/bl_operators/object.py\:723 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L723>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode, Which transforms to transfer * ``ALL`` All Transforms -- Transfer location, rotation, and scale transforms. * ``LOC`` Location -- Transfer location transforms only. * ``ROT`` Rotation -- Transfer rotation transforms only. * ``SCALE`` Scale -- Transfer scale transforms only.
    :type mode: typing.Optional[typing.Any]
    :param reset_values: Reset Values, Clear transform values after transferring to deltas
    :type reset_values: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def unlink_data(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Undocumented, consider `contributing <https://developer.blender.org/>`__.

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add a new vertex group to the active object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_assign(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Assign the selected vertices to the active vertex group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_assign_new(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Assign the selected vertices to a new vertex group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_clean(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        group_select_mode: typing.Optional[typing.Union[str, int, typing.
                                                        Any]] = '',
        limit: typing.Optional[typing.Any] = 0.0,
        keep_single: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Remove vertex group assignments which are not required

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Optional[typing.Union[str, int, typing.Any]]
    :param limit: Limit, Remove vertices which weight is below or equal to this limit
    :type limit: typing.Optional[typing.Any]
    :param keep_single: Keep Single, Keep verts assigned to at least one group when cleaning
    :type keep_single: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def vertex_group_copy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Make a copy of the active vertex group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_copy_to_selected(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Replace vertex groups of selected objects by vertex groups of active object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_deselect(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Deselect all selected vertices assigned to the active vertex group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_invert(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        group_select_mode: typing.Optional[typing.Union[str, int, typing.
                                                        Any]] = '',
        auto_assign: typing.Optional[typing.Union[bool, typing.Any]] = True,
        auto_remove: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Invert active vertex group's weights

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Optional[typing.Union[str, int, typing.Any]]
    :param auto_assign: Add Weights, Add vertices from groups that have zero weight before inverting
    :type auto_assign: typing.Optional[typing.Union[bool, typing.Any]]
    :param auto_remove: Remove Weights, Remove vertices from groups that have zero weight after inverting
    :type auto_remove: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def vertex_group_levels(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        group_select_mode: typing.Optional[typing.Union[str, int, typing.
                                                        Any]] = '',
        offset: typing.Optional[typing.Any] = 0.0,
        gain: typing.Optional[typing.Any] = 1.0):
    ''' Add some offset and multiply with some gain the weights of the active vertex group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Optional[typing.Union[str, int, typing.Any]]
    :param offset: Offset, Value to add to weights
    :type offset: typing.Optional[typing.Any]
    :param gain: Gain, Value to multiply weights by
    :type gain: typing.Optional[typing.Any]
    '''

    pass


def vertex_group_limit_total(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        group_select_mode: typing.Optional[typing.Union[str, int, typing.
                                                        Any]] = '',
        limit: typing.Optional[typing.Any] = 4):
    ''' Limit deform weights associated with a vertex to a specified number by removing lowest weights

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Optional[typing.Union[str, int, typing.Any]]
    :param limit: Limit, Maximum number of deform weights
    :type limit: typing.Optional[typing.Any]
    '''

    pass


def vertex_group_lock(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        action: typing.Optional[typing.Any] = 'TOGGLE',
        mask: typing.Optional[typing.Any] = 'ALL'):
    ''' Change the lock state of all or some vertex groups of active object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param action: Action, Lock action to execute on vertex groups * ``TOGGLE`` Toggle -- Unlock all vertex groups if there is at least one locked group, lock all in other case. * ``LOCK`` Lock -- Lock all vertex groups. * ``UNLOCK`` Unlock -- Unlock all vertex groups. * ``INVERT`` Invert -- Invert the lock state of all vertex groups.
    :type action: typing.Optional[typing.Any]
    :param mask: Mask, Apply the action based on vertex group selection * ``ALL`` All -- Apply action to all vertex groups. * ``SELECTED`` Selected -- Apply to selected vertex groups. * ``UNSELECTED`` Unselected -- Apply to unselected vertex groups. * ``INVERT_UNSELECTED`` Invert Unselected -- Apply the opposite of Lock/Unlock to unselected vertex groups.
    :type mask: typing.Optional[typing.Any]
    '''

    pass


def vertex_group_mirror(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mirror_weights: typing.Optional[typing.Union[bool, typing.Any]] = True,
        flip_group_names: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        all_groups: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_topology: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mirror_weights: Mirror Weights, Mirror weights
    :type mirror_weights: typing.Optional[typing.Union[bool, typing.Any]]
    :param flip_group_names: Flip Group Names, Flip vertex group names
    :type flip_group_names: typing.Optional[typing.Union[bool, typing.Any]]
    :param all_groups: All Groups, Mirror all vertex groups weights
    :type all_groups: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
    :type use_topology: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def vertex_group_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        direction: typing.Optional[typing.Any] = 'UP'):
    ''' Move the active vertex group up/down in the list

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Direction to move the active vertex group towards
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def vertex_group_normalize(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Normalize weights of the active vertex group, so that the highest ones are now 1.0

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_normalize_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        group_select_mode: typing.Optional[typing.Union[str, int, typing.
                                                        Any]] = '',
        lock_active: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Optional[typing.Union[str, int, typing.Any]]
    :param lock_active: Lock Active, Keep the values of the active group while normalizing others
    :type lock_active: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def vertex_group_quantize(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        group_select_mode: typing.Optional[typing.Union[str, int, typing.
                                                        Any]] = '',
        steps: typing.Optional[typing.Any] = 4):
    ''' Set weights to a fixed number of steps

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Optional[typing.Union[str, int, typing.Any]]
    :param steps: Steps, Number of steps between 0 and 1
    :type steps: typing.Optional[typing.Any]
    '''

    pass


def vertex_group_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        all: typing.Optional[typing.Union[bool, typing.Any]] = False,
        all_unlocked: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Delete the active or all vertex groups from the active object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param all: All, Remove all vertex groups
    :type all: typing.Optional[typing.Union[bool, typing.Any]]
    :param all_unlocked: All Unlocked, Remove all unlocked vertex groups
    :type all_unlocked: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def vertex_group_remove_from(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_all_groups: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        use_all_verts: typing.Optional[typing.Union[bool, typing.
                                                    Any]] = False):
    ''' Remove the selected vertices from active or all vertex group(s)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_all_groups: All Groups, Remove from all groups
    :type use_all_groups: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_all_verts: All Vertices, Clear the active group
    :type use_all_verts: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def vertex_group_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select all the vertices assigned to the active vertex group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_set_active(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        group: typing.Optional[typing.Union[str, int, typing.Any]] = ''):
    ''' Set the active vertex group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param group: Group, Vertex group to set as active
    :type group: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def vertex_group_smooth(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        group_select_mode: typing.Optional[typing.Union[str, int, typing.
                                                        Any]] = '',
        factor: typing.Optional[typing.Any] = 0.5,
        repeat: typing.Optional[typing.Any] = 1,
        expand: typing.Optional[typing.Any] = 0.0):
    ''' Smooth weights for selected vertices

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Optional[typing.Union[str, int, typing.Any]]
    :param factor: Factor
    :type factor: typing.Optional[typing.Any]
    :param repeat: Iterations
    :type repeat: typing.Optional[typing.Any]
    :param expand: Expand/Contract, Expand/contract weights
    :type expand: typing.Optional[typing.Any]
    '''

    pass


def vertex_group_sort(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        sort_type: typing.Optional[typing.Any] = 'NAME'):
    ''' Sort vertex groups

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param sort_type: Sort Type, Sort type
    :type sort_type: typing.Optional[typing.Any]
    '''

    pass


def vertex_parent_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        confirm: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Parent selected objects to the selected vertices

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def vertex_weight_copy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Copy weights from active to selected

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_weight_delete(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        weight_group: typing.Optional[typing.Any] = -1):
    ''' Delete this weight from the vertex (disabled if vertex group is locked)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: typing.Optional[typing.Any]
    '''

    pass


def vertex_weight_normalize_active_vertex(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Normalize active vertex's weights

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_weight_paste(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        weight_group: typing.Optional[typing.Any] = -1):
    ''' Copy this group's weight to other selected vertices (disabled if vertex group is locked)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: typing.Optional[typing.Any]
    '''

    pass


def vertex_weight_set_active(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        weight_group: typing.Optional[typing.Any] = -1):
    ''' Set as active vertex group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: typing.Optional[typing.Any]
    '''

    pass


def visual_transform_apply(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Apply the object's visual transformation to its data

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def volume_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Add a volume object to the scene

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def volume_import(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        directory: typing.Union[str, typing.Any] = "",
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        hide_props_region: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        check_existing: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_sound: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 9,
        relative_path: typing.Optional[typing.Union[bool, typing.Any]] = True,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        use_sequence_detection: typing.Optional[typing.Union[bool, typing.
                                                             Any]] = True,
        align: typing.Optional[typing.Any] = 'WORLD',
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        scale: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Import OpenVDB volume file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param files: Files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: typing.Optional[typing.Union[bool, typing.Any]]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_image: Filter image files
    :type filter_image: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_python: Filter Python files
    :type filter_python: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_font: Filter font files
    :type filter_font: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_text: Filter text files
    :type filter_text: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Optional[typing.Union[bool, typing.Any]]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Optional[typing.Union[bool, typing.Any]]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Optional[typing.Union[str, int, typing.Any]]
    :param use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected volume files (based on file names)
    :type use_sequence_detection: typing.Optional[typing.Union[bool, typing.Any]]
    :param align: Align, The alignment of the new object * ``WORLD`` World -- Align the new object to the world. * ``VIEW`` View -- Align the new object to the view. * ``CURSOR`` 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Optional[typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def voxel_remesh(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Calculates a new manifold mesh based on the volume of the current mesh. All data layers will be lost

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def voxel_size_edit(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Modify the mesh voxel size interactively used in the voxel remesher

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass
