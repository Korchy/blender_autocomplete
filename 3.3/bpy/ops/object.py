import sys
import typing
import bpy.types
import mathutils
import bpy.ops.transform

GenericType = typing.TypeVar("GenericType")


def add(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        radius: float = 1.0,
        type: typing.Union[int, str] = 'EMPTY',
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add an object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param radius: Radius
    :type radius: float
    :param type: Type
    :type type: typing.Union[int, str]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def add_named(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        linked: bool = False,
        name: str = "",
        session_uuid: int = 0,
        matrix: typing.
        Union[typing.List[typing.List[float]], typing.
              Tuple[typing.Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float]], 'mathutils.Matrix'] = (
                        (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0),
                        (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)),
        drop_x: int = 0,
        drop_y: int = 0):
    ''' Add named object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param linked: Linked, Duplicate object but not object data, linking to the original data
    :type linked: bool
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    :param matrix: Matrix
    :type matrix: typing.Union[typing.List[typing.List[float]], typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]], 'mathutils.Matrix']
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: int
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: int
    '''

    pass


def align(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None,
          *,
          bb_quality: bool = True,
          align_mode: typing.Union[str, int] = 'OPT_2',
          relative_to: typing.Union[str, int] = 'OPT_4',
          align_axis: typing.Union[typing.Set[str], typing.Set[int]] = {}):
    ''' Align objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param bb_quality: High Quality, Enables high quality but slow calculation of the bounding box for perfect results on complex shape meshes with rotation/scale
    :type bb_quality: bool
    :param align_mode: Align Mode, Side of object to use for alignment
    :type align_mode: typing.Union[str, int]
    :param relative_to: Relative To, Reference location to align to * OPT_1 Scene Origin -- Use the scene origin as the position for the selected objects to align to. * OPT_2 3D Cursor -- Use the 3D cursor as the position for the selected objects to align to. * OPT_3 Selection -- Use the selected objects as the position for the selected objects to align to. * OPT_4 Active -- Use the active object as the position for the selected objects to align to.
    :type relative_to: typing.Union[str, int]
    :param align_axis: Align, Align to axis
    :type align_axis: typing.Union[typing.Set[str], typing.Set[int]]
    '''

    pass


def anim_transforms_to_deltas(override_context: typing.
                              Union[typing.Dict, 'bpy.types.Context'] = None,
                              execution_context: typing.Union[str, int] = None,
                              undo: bool = None):
    ''' Convert object animation for normal transforms to delta transforms :file: startup/bl_operators/object.py\:771 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/object.py$771> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def armature_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        radius: float = 1.0,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add an armature object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def assign_property_defaults(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None,
                             *,
                             process_data: bool = True,
                             process_bones: bool = True):
    ''' Assign the current values of custom properties as their defaults, for use as part of the rest pose state in NLA track mixing

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param process_data: Process data properties
    :type process_data: bool
    :param process_bones: Process bone properties
    :type process_bones: bool
    '''

    pass


def bake(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         type: typing.Union[int, str] = 'COMBINED',
         pass_filter: typing.Union[typing.Set[int], typing.Set[str]] = {},
         filepath: str = "",
         width: int = 512,
         height: int = 512,
         margin: int = 16,
         margin_type: typing.Union[int, str] = 'EXTEND',
         use_selected_to_active: bool = False,
         max_ray_distance: float = 0.0,
         cage_extrusion: float = 0.0,
         cage_object: str = "",
         normal_space: typing.Union[int, str] = 'TANGENT',
         normal_r: typing.Union[int, str] = 'POS_X',
         normal_g: typing.Union[int, str] = 'POS_Y',
         normal_b: typing.Union[int, str] = 'POS_Z',
         target: typing.Union[int, str] = 'IMAGE_TEXTURES',
         save_mode: typing.Union[int, str] = 'INTERNAL',
         use_clear: bool = False,
         use_cage: bool = False,
         use_split_materials: bool = False,
         use_automatic_name: bool = False,
         uv_layer: str = ""):
    ''' Bake image textures of selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Type of pass to bake, some of them may not be supported by the current render engine
    :type type: typing.Union[int, str]
    :param pass_filter: Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes
    :type pass_filter: typing.Union[typing.Set[int], typing.Set[str]]
    :param filepath: File Path, Image filepath to use when saving externally
    :type filepath: str
    :param width: Width, Horizontal dimension of the baking map (external only)
    :type width: int
    :param height: Height, Vertical dimension of the baking map (external only)
    :type height: int
    :param margin: Margin, Extends the baked result as a post process filter
    :type margin: int
    :param margin_type: Margin Type, Which algorithm to use to generate the margin
    :type margin_type: typing.Union[int, str]
    :param use_selected_to_active: Selected to Active, Bake shading on the surface of selected objects to the active object
    :type use_selected_to_active: bool
    :param max_ray_distance: Max Ray Distance, The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit
    :type max_ray_distance: float
    :param cage_extrusion: Cage Extrusion, Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes
    :type cage_extrusion: float
    :param cage_object: Cage Object, Object to use as cage, instead of calculating the cage from the active object with cage extrusion
    :type cage_object: str
    :param normal_space: Normal Space, Choose normal space for baking
    :type normal_space: typing.Union[int, str]
    :param normal_r: R, Axis to bake in red channel
    :type normal_r: typing.Union[int, str]
    :param normal_g: G, Axis to bake in green channel
    :type normal_g: typing.Union[int, str]
    :param normal_b: B, Axis to bake in blue channel
    :type normal_b: typing.Union[int, str]
    :param target: Target, Where to output the baked map
    :type target: typing.Union[int, str]
    :param save_mode: Save Mode, Where to save baked image textures
    :type save_mode: typing.Union[int, str]
    :param use_clear: Clear, Clear images before baking (only for internal saving)
    :type use_clear: bool
    :param use_cage: Cage, Cast rays to active object from a cage
    :type use_cage: bool
    :param use_split_materials: Split Materials, Split baked maps per material, using material name in output file (external only)
    :type use_split_materials: bool
    :param use_automatic_name: Automatic Name, Automatically name the output file with the pass type
    :type use_automatic_name: bool
    :param uv_layer: UV Layer, UV layer to override active
    :type uv_layer: str
    '''

    pass


def bake_image(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Bake image textures of selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def camera_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add a camera object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def clear_override_library(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None):
    ''' Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def collection_add(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Add an object to a new collection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def collection_external_asset_drop(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        session_uuid: int = 0,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0),
        use_instance: bool = True,
        drop_x: int = 0,
        drop_y: int = 0,
        collection: typing.Union[str, int] = ''):
    ''' Add the dragged collection to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param use_instance: Instance, Add the dropped collection as collection instance
    :type use_instance: bool
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: int
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: int
    :param collection: Collection
    :type collection: typing.Union[str, int]
    '''

    pass


def collection_instance_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        name: str = "Collection",
        collection: typing.Union[str, int] = '',
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0),
        session_uuid: int = 0,
        drop_x: int = 0,
        drop_y: int = 0):
    ''' Add a collection instance

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Collection name to add
    :type name: str
    :param collection: Collection
    :type collection: typing.Union[str, int]
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: int
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: int
    '''

    pass


def collection_link(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    collection: typing.Union[str, int] = ''):
    ''' Add an object to an existing collection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param collection: Collection
    :type collection: typing.Union[str, int]
    '''

    pass


def collection_objects_select(override_context: typing.
                              Union[typing.Dict, 'bpy.types.Context'] = None,
                              execution_context: typing.Union[str, int] = None,
                              undo: bool = None):
    ''' Select all objects in collection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def collection_remove(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Remove the active object from this collection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def collection_unlink(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Unlink the collection from all objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def constraint_add(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   type: typing.Union[str, int] = ''):
    ''' Add a constraint to the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def constraint_add_with_targets(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        type: typing.Union[str, int] = ''):
    ''' Add a constraint to the active object, with target (where applicable) set to the selected objects/bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def constraints_clear(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Clear all the constraints for the active object only

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def constraints_copy(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Copy constraints to other selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def convert(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: bool = None,
            *,
            target: typing.Union[str, int] = 'MESH',
            keep_original: bool = False,
            merge_customdata: bool = True,
            angle: float = 1.22173,
            thickness: int = 5,
            seams: bool = False,
            faces: bool = True,
            offset: float = 0.01):
    ''' Convert selected objects to another type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param target: Target, Type of object to convert to * CURVE Curve -- Curve from Mesh or Text objects. * MESH Mesh -- Mesh from Curve, Surface, Metaball, or Text objects. * GPENCIL Grease Pencil -- Grease Pencil from Curve or Mesh objects. * CURVES Curves -- Curves from evaluated curve data.
    :type target: typing.Union[str, int]
    :param keep_original: Keep Original, Keep original objects instead of replacing them
    :type keep_original: bool
    :param merge_customdata: Merge UV's, Merge UV coordinates that share a vertex to account for imprecision in some modifiers
    :type merge_customdata: bool
    :param angle: Threshold Angle, Threshold to determine ends of the strokes
    :type angle: float
    :param thickness: Thickness
    :type thickness: int
    :param seams: Only Seam Edges, Convert only seam edges
    :type seams: bool
    :param faces: Export Faces, Export faces as filled strokes
    :type faces: bool
    :param offset: Stroke Offset, Offset strokes from fill
    :type offset: float
    '''

    pass


def correctivesmooth_bind(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          modifier: str = ""):
    ''' Bind base pose in Corrective Smooth modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def curves_empty_hair_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add an empty curve object to the scene with the selected mesh as surface

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def curves_random_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add a curves object with random curves to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def data_instance_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        name: str = "",
        session_uuid: int = 0,
        type: typing.Union[int, str] = 'ACTION',
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0),
        drop_x: int = 0,
        drop_y: int = 0):
    ''' Add an object data instance

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    :param type: Type
    :type type: typing.Union[int, str]
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: int
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: int
    '''

    pass


def data_transfer(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  use_reverse_transfer: bool = False,
                  use_freeze: bool = False,
                  data_type: typing.Union[str, int] = '',
                  use_create: bool = True,
                  vert_mapping: typing.Union[int, str] = 'NEAREST',
                  edge_mapping: typing.Union[int, str] = 'NEAREST',
                  loop_mapping: typing.Union[int, str] = 'NEAREST_POLYNOR',
                  poly_mapping: typing.Union[int, str] = 'NEAREST',
                  use_auto_transform: bool = False,
                  use_object_transform: bool = True,
                  use_max_distance: bool = False,
                  max_distance: float = 1.0,
                  ray_radius: float = 0.0,
                  islands_precision: float = 0.1,
                  layers_select_src: typing.Union[int, str] = 'ACTIVE',
                  layers_select_dst: typing.Union[int, str] = 'ACTIVE',
                  mix_mode: typing.Union[int, str] = 'REPLACE',
                  mix_factor: float = 1.0):
    ''' Transfer data layer(s) (weights, edge sharp, etc.) from active to selected meshes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_reverse_transfer: Reverse Transfer, Transfer from selected objects to active one
    :type use_reverse_transfer: bool
    :param use_freeze: Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry
    :type use_freeze: bool
    :param data_type: Data Type, Which data to transfer * VGROUP_WEIGHTS Vertex Group(s) -- Transfer active or all vertex groups. * BEVEL_WEIGHT_VERT Bevel Weight -- Transfer bevel weights. * SHARP_EDGE Sharp -- Transfer sharp mark. * SEAM UV Seam -- Transfer UV seam mark. * CREASE Subdivision Crease -- Transfer crease values. * BEVEL_WEIGHT_EDGE Bevel Weight -- Transfer bevel weights. * FREESTYLE_EDGE Freestyle Mark -- Transfer Freestyle edge mark. * CUSTOM_NORMAL Custom Normals -- Transfer custom normals. * VCOL Colors -- Color Attributes. * UV UVs -- Transfer UV layers. * SMOOTH Smooth -- Transfer flat/smooth mark. * FREESTYLE_FACE Freestyle Mark -- Transfer Freestyle face mark.
    :type data_type: typing.Union[str, int]
    :param use_create: Create Data, Add data layers on destination meshes if needed
    :type use_create: bool
    :param vert_mapping: Vertex Mapping, Method used to map source vertices to destination ones
    :type vert_mapping: typing.Union[int, str]
    :param edge_mapping: Edge Mapping, Method used to map source edges to destination ones
    :type edge_mapping: typing.Union[int, str]
    :param loop_mapping: Face Corner Mapping, Method used to map source faces' corners to destination ones
    :type loop_mapping: typing.Union[int, str]
    :param poly_mapping: Face Mapping, Method used to map source faces to destination ones
    :type poly_mapping: typing.Union[int, str]
    :param use_auto_transform: Auto Transform, Automatically compute transformation to get the best possible match between source and destination meshes. Warning: Results will never be as good as manual matching of objects
    :type use_auto_transform: bool
    :param use_object_transform: Object Transform, Evaluate source and destination meshes in global space
    :type use_object_transform: bool
    :param use_max_distance: Only Neighbor Geometry, Source elements must be closer than given distance from destination one
    :type use_max_distance: bool
    :param max_distance: Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings
    :type max_distance: float
    :param ray_radius: Ray Radius, 'Width' of rays (especially useful when raycasting against vertices or edges)
    :type ray_radius: float
    :param islands_precision: Islands Precision, Factor controlling precision of islands handling (the higher, the better the results)
    :type islands_precision: float
    :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types
    :type layers_select_src: typing.Union[int, str]
    :param layers_select_dst: Destination Layers Matching, How to match source and destination layers
    :type layers_select_dst: typing.Union[int, str]
    :param mix_mode: Mix Mode, How to affect destination elements with source values
    :type mix_mode: typing.Union[int, str]
    :param mix_factor: Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode)
    :type mix_factor: float
    '''

    pass


def datalayout_transfer(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        modifier: str = "",
                        data_type: typing.Union[str, int] = '',
                        use_delete: bool = False,
                        layers_select_src: typing.Union[int, str] = 'ACTIVE',
                        layers_select_dst: typing.Union[int, str] = 'ACTIVE'):
    ''' Transfer layout of data layer(s) from active to selected meshes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param data_type: Data Type, Which data to transfer * VGROUP_WEIGHTS Vertex Group(s) -- Transfer active or all vertex groups. * BEVEL_WEIGHT_VERT Bevel Weight -- Transfer bevel weights. * SHARP_EDGE Sharp -- Transfer sharp mark. * SEAM UV Seam -- Transfer UV seam mark. * CREASE Subdivision Crease -- Transfer crease values. * BEVEL_WEIGHT_EDGE Bevel Weight -- Transfer bevel weights. * FREESTYLE_EDGE Freestyle Mark -- Transfer Freestyle edge mark. * CUSTOM_NORMAL Custom Normals -- Transfer custom normals. * VCOL Colors -- Color Attributes. * UV UVs -- Transfer UV layers. * SMOOTH Smooth -- Transfer flat/smooth mark. * FREESTYLE_FACE Freestyle Mark -- Transfer Freestyle face mark.
    :type data_type: typing.Union[str, int]
    :param use_delete: Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source
    :type use_delete: bool
    :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types
    :type layers_select_src: typing.Union[int, str]
    :param layers_select_dst: Destination Layers Matching, How to match source and destination layers
    :type layers_select_dst: typing.Union[int, str]
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           use_global: bool = False,
           confirm: bool = True):
    ''' Delete selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_global: Delete Globally, Remove object from all scenes
    :type use_global: bool
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool
    '''

    pass


def drop_named_image(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        filepath: str = "",
        relative_path: bool = True,
        name: str = "",
        session_uuid: int = 0,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add an empty image type to scene with data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: Filepath, Path to image file
    :type filepath: str
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def drop_named_material(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        name: str = "",
                        session_uuid: int = 0):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    '''

    pass


def duplicate(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              linked: bool = False,
              mode: typing.Union[int, str] = 'TRANSLATION'):
    ''' Duplicate selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param linked: Linked, Duplicate object but not object data, linking to the original data
    :type linked: bool
    :param mode: Mode
    :type mode: typing.Union[int, str]
    '''

    pass


def duplicate_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        OBJECT_OT_duplicate: 'duplicate' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Duplicate the selected objects and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
    :type OBJECT_OT_duplicate: 'duplicate'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def duplicate_move_linked(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        OBJECT_OT_duplicate: 'duplicate' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None):
    ''' Duplicate the selected objects, but not their object data, and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
    :type OBJECT_OT_duplicate: 'duplicate'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    '''

    pass


def duplicates_make_real(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         use_base_parent: bool = False,
                         use_hierarchy: bool = False):
    ''' Make instanced objects attached to this object real

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_base_parent: Parent, Parent newly created objects to the original instancer
    :type use_base_parent: bool
    :param use_hierarchy: Keep Hierarchy, Maintain parent child relationships
    :type use_hierarchy: bool
    '''

    pass


def editmode_toggle(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Toggle object's edit mode

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def effector_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        type: typing.Union[str, int] = 'FORCE',
        radius: float = 1.0,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add an empty object with a physics effector to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def empty_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        type: typing.Union[int, str] = 'PLAIN_AXES',
        radius: float = 1.0,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add an empty object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[int, str]
    :param radius: Radius
    :type radius: float
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def explode_refresh(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    modifier: str = ""):
    ''' Refresh data in the Explode modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def face_map_add(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Add a new face map to the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def face_map_assign(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Assign faces to a face map

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def face_map_deselect(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Deselect faces belonging to a face map

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def face_map_move(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  direction: typing.Union[str, int] = 'UP'):
    ''' Move the active face map up/down in the list

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param direction: Direction, Direction to move, up or down
    :type direction: typing.Union[str, int]
    '''

    pass


def face_map_remove(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Remove a face map from the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def face_map_remove_from(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Remove faces from a face map

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def face_map_select(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Select faces belonging to a face map

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def forcefield_toggle(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Toggle object's force field

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def geometry_node_tree_copy_assign(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Copy the active geometry node group and assign it to the active modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def geometry_nodes_input_attribute_toggle(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        prop_path: str = "",
        modifier_name: str = ""):
    ''' Switch between an attribute and a single value to define the data for every element

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param prop_path: Prop Path
    :type prop_path: str
    :param modifier_name: Modifier Name
    :type modifier_name: str
    '''

    pass


def gpencil_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        radius: float = 1.0,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0),
        type: typing.Union[int, str] = 'EMPTY',
        use_in_front: bool = True,
        stroke_depth_offset: float = 0.05,
        use_lights: bool = False,
        stroke_depth_order: typing.Union[str, int] = '3D'):
    ''' Add a Grease Pencil object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param radius: Radius
    :type radius: float
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param type: Type
    :type type: typing.Union[int, str]
    :param use_in_front: Show In Front, Show line art grease pencil in front of everything
    :type use_in_front: bool
    :param stroke_depth_offset: Stroke Offset, Stroke offset for the line art modifier
    :type stroke_depth_offset: float
    :param use_lights: Use Lights, Use lights for this grease pencil object
    :type use_lights: bool
    :param stroke_depth_order: Stroke Depth Order, Defines how the strokes are ordered in 3D space for objects not displayed 'In Front') * 2D 2D Layers -- Display strokes using grease pencil layers to define order. * 3D 3D Location -- Display strokes using real 3D position in 3D space.
    :type stroke_depth_order: typing.Union[str, int]
    '''

    pass


def gpencil_modifier_add(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         type: typing.Union[int, str] = 'GP_THICK'):
    ''' Add a procedural operation/effect to the active grease pencil object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def gpencil_modifier_apply(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None,
                           *,
                           apply_as: typing.Union[str, int] = 'DATA',
                           modifier: str = "",
                           report: bool = False):
    ''' Apply modifier and remove from the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param apply_as: Apply As, How to apply the modifier to the geometry * DATA Object Data -- Apply modifier to the object's data. * SHAPE New Shape -- Apply deform-only modifier to a new shape on this object.
    :type apply_as: typing.Union[str, int]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def gpencil_modifier_copy(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          modifier: str = ""):
    ''' Duplicate modifier at the same position in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def gpencil_modifier_copy_to_selected(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        modifier: str = ""):
    ''' Copy the modifier from the active object to all selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def gpencil_modifier_move_down(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        modifier: str = ""):
    ''' Move modifier down in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def gpencil_modifier_move_to_index(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        modifier: str = "",
        index: int = 0):
    ''' Change the modifier's position in the list so it evaluates after the set number of others

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param index: Index, The index to move the modifier to
    :type index: int
    '''

    pass


def gpencil_modifier_move_up(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None,
                             *,
                             modifier: str = ""):
    ''' Move modifier up in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def gpencil_modifier_remove(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None,
                            *,
                            modifier: str = "",
                            report: bool = False):
    ''' Remove a modifier from the active grease pencil object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def hide_collection(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    collection_index: int = -1,
                    toggle: bool = False,
                    extend: bool = False):
    ''' Show only objects in collection (Shift to extend)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param collection_index: Collection Index, Index of the collection to change visibility
    :type collection_index: int
    :param toggle: Toggle, Toggle visibility
    :type toggle: bool
    :param extend: Extend, Extend visibility
    :type extend: bool
    '''

    pass


def hide_render_clear_all(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Reveal all render objects by setting the hide render flag :file: startup/bl_operators/object.py\:678 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/object.py$678> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def hide_view_clear(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    select: bool = True):
    ''' Reveal temporarily hidden objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param select: Select
    :type select: bool
    '''

    pass


def hide_view_set(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  unselected: bool = False):
    ''' Temporarily hide objects from the viewport

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: bool
    '''

    pass


def hook_add_newob(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Hook selected vertices to a newly created object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def hook_add_selob(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   use_bone: bool = False):
    ''' Hook selected vertices to the first selected object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_bone: Active Bone, Assign the hook to the hook objects active bone
    :type use_bone: bool
    '''

    pass


def hook_assign(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                modifier: typing.Union[str, int] = ''):
    ''' Assign the selected vertices to a hook

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Modifier number to assign to
    :type modifier: typing.Union[str, int]
    '''

    pass


def hook_recenter(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  modifier: typing.Union[str, int] = ''):
    ''' Set hook center to cursor position

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Modifier number to assign to
    :type modifier: typing.Union[str, int]
    '''

    pass


def hook_remove(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                modifier: typing.Union[str, int] = ''):
    ''' Remove a hook from the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Modifier number to remove
    :type modifier: typing.Union[str, int]
    '''

    pass


def hook_reset(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               modifier: typing.Union[str, int] = ''):
    ''' Recalculate and clear offset transformation

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Modifier number to assign to
    :type modifier: typing.Union[str, int]
    '''

    pass


def hook_select(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                modifier: typing.Union[str, int] = ''):
    ''' Select affected vertices on mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Modifier number to remove
    :type modifier: typing.Union[str, int]
    '''

    pass


def instance_offset_from_cursor(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Set offset used for collection instances based on cursor position :file: startup/bl_operators/object.py\:856 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/object.py$856> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def instance_offset_from_object(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Set offset used for collection instances based on the active object position :file: startup/bl_operators/object.py\:888 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/object.py$888> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def instance_offset_to_cursor(override_context: typing.
                              Union[typing.Dict, 'bpy.types.Context'] = None,
                              execution_context: typing.Union[str, int] = None,
                              undo: bool = None):
    ''' Set cursor position to the offset used for collection instances :file: startup/bl_operators/object.py\:871 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/object.py$871> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def isolate_type_render(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Hide unselected render objects of same type as active by setting the hide render flag :file: startup/bl_operators/object.py\:658 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/object.py$658> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def join(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None):
    ''' Join selected objects into active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def join_shapes(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Copy the current resulting shape of another selected object to this one

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def join_uvs(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None):
    ''' Transfer UV Maps from active to selected objects (needs matching geometry) :file: startup/bl_operators/object.py\:565 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/object.py$565> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def laplaciandeform_bind(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         modifier: str = ""):
    ''' Bind mesh to system in laplacian deform modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def light_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        type: typing.Union[int, str] = 'POINT',
        radius: float = 1.0,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add a light object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[int, str]
    :param radius: Radius
    :type radius: float
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def lightprobe_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        type: typing.Union[str, int] = 'CUBEMAP',
        radius: float = 1.0,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add a light probe object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * CUBEMAP Reflection Cubemap -- Reflection probe with spherical or cubic attenuation. * PLANAR Reflection Plane -- Planar reflection probe. * GRID Irradiance Volume -- Irradiance probe to capture diffuse indirect lighting.
    :type type: typing.Union[str, int]
    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def lineart_bake_strokes(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Bake Line Art for current GPencil object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def lineart_bake_strokes_all(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None):
    ''' Bake all Grease Pencil objects that have a line art modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def lineart_clear(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Clear all strokes in current GPencil object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def lineart_clear_all(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Clear all strokes in all Grease Pencil objects that have a line art modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def link_to_collection(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       collection_index: int = -1,
                       is_new: bool = False,
                       new_collection_name: str = ""):
    ''' Link objects to a collection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param collection_index: Collection Index, Index of the collection to move to
    :type collection_index: int
    :param is_new: New, Move objects to a new collection
    :type is_new: bool
    :param new_collection_name: Name, Name of the newly added collection
    :type new_collection_name: str
    '''

    pass


def load_background_image(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          filepath: str = "",
                          filter_image: bool = True,
                          filter_folder: bool = True,
                          view_align: bool = True):
    ''' Add a reference image into the background behind objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: filepath
    :type filepath: str
    :param filter_image: filter_image
    :type filter_image: bool
    :param filter_folder: filter_folder
    :type filter_folder: bool
    :param view_align: Align to View
    :type view_align: bool
    '''

    pass


def load_reference_image(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         filepath: str = "",
                         filter_image: bool = True,
                         filter_folder: bool = True,
                         view_align: bool = True):
    ''' Add a reference image into the scene between objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: filepath
    :type filepath: str
    :param filter_image: filter_image
    :type filter_image: bool
    :param filter_folder: filter_folder
    :type filter_folder: bool
    :param view_align: Align to View
    :type view_align: bool
    '''

    pass


def location_clear(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   clear_delta: bool = False):
    ''' Clear the object's location

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param clear_delta: Clear Delta, Clear delta location in addition to clearing the normal location transform
    :type clear_delta: bool
    '''

    pass


def make_dupli_face(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Convert objects into instanced faces :file: startup/bl_operators/object.py\:646 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/object.py$646> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def make_links_data(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    type: typing.Union[str, int] = 'OBDATA'):
    ''' Transfer data from active object to selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * OBDATA Link Object Data -- Replace assigned Object Data. * MATERIAL Link Materials -- Replace assigned Materials. * ANIMATION Link Animation Data -- Replace assigned Animation Data. * GROUPS Link Collections -- Replace assigned Collections. * DUPLICOLLECTION Link Instance Collection -- Replace assigned Collection Instance. * FONTS Link Fonts to Text -- Replace Text object Fonts. * MODIFIERS Copy Modifiers -- Replace Modifiers. * EFFECTS Copy Grease Pencil Effects -- Replace Grease Pencil Effects.
    :type type: typing.Union[str, int]
    '''

    pass


def make_links_scene(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     scene: typing.Union[str, int] = ''):
    ''' Link selection to another scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param scene: Scene
    :type scene: typing.Union[str, int]
    '''

    pass


def make_local(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               type: typing.Union[str, int] = 'SELECT_OBJECT'):
    ''' Make library linked data-blocks local to this file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def make_override_library(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          collection: int = 0):
    ''' Create a local override of the selected linked objects, and their hierarchy of dependencies

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param collection: Override Collection, Session UUID of the directly linked collection containing the selected object, to make an override from
    :type collection: int
    '''

    pass


def make_single_user(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     type: typing.Union[str, int] = 'SELECTED_OBJECTS',
                     object: bool = False,
                     obdata: bool = False,
                     material: bool = False,
                     animation: bool = False,
                     obdata_animation: bool = False):
    ''' Make linked data local to each object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    :param object: Object, Make single user objects
    :type object: bool
    :param obdata: Object Data, Make single user object data
    :type obdata: bool
    :param material: Materials, Make materials local to each data-block
    :type material: bool
    :param animation: Object Animation, Make object animation data local to each object
    :type animation: bool
    :param obdata_animation: Object Data Animation, Make object data (mesh, curve etc.) animation data local to each object
    :type obdata_animation: bool
    '''

    pass


def material_slot_add(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Add a new material slot

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def material_slot_assign(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Assign active material slot to selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def material_slot_copy(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Copy material to selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def material_slot_deselect(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None):
    ''' Deselect by active material slot

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def material_slot_move(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       direction: typing.Union[str, int] = 'UP'):
    ''' Move the active material up/down in the list

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param direction: Direction, Direction to move the active material towards
    :type direction: typing.Union[str, int]
    '''

    pass


def material_slot_remove(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Remove the selected material slot

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def material_slot_remove_unused(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Remove unused material slots

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def material_slot_select(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Select by active material slot

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def meshdeform_bind(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    modifier: str = ""):
    ''' Bind mesh to cage in mesh deform modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def metaball_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        type: typing.Union[int, str] = 'BALL',
        radius: float = 2.0,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add an metaball object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Primitive
    :type type: typing.Union[int, str]
    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def mode_set(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             mode: typing.Union[int, str] = 'OBJECT',
             toggle: bool = False):
    ''' Sets the object interaction mode

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[int, str]
    :param toggle: Toggle
    :type toggle: bool
    '''

    pass


def mode_set_with_submode(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        mode: typing.Union[int, str] = 'OBJECT',
        toggle: bool = False,
        mesh_select_mode: typing.Union[typing.Set[int], typing.Set[str]] = {}):
    ''' Sets the object interaction mode

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[int, str]
    :param toggle: Toggle
    :type toggle: bool
    :param mesh_select_mode: Mesh Mode
    :type mesh_select_mode: typing.Union[typing.Set[int], typing.Set[str]]
    '''

    pass


def modifier_add(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 type: typing.Union[int, str] = 'SUBSURF'):
    ''' Add a procedural operation/effect to the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def modifier_apply(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   modifier: str = "",
                   report: bool = False,
                   merge_customdata: bool = True,
                   single_user: bool = False):
    ''' Apply modifier and remove from the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param report: Report, Create a notification after the operation
    :type report: bool
    :param merge_customdata: Merge UV's, For mesh objects, merge UV coordinates that share a vertex to account for imprecision in some modifiers
    :type merge_customdata: bool
    :param single_user: Make Data Single User, Make the object's data single user if needed
    :type single_user: bool
    '''

    pass


def modifier_apply_as_shapekey(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        keep_modifier: bool = False,
        modifier: str = "",
        report: bool = False):
    ''' Apply modifier as a new shape key and remove from the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param keep_modifier: Keep Modifier, Do not remove the modifier from stack
    :type keep_modifier: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def modifier_convert(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     modifier: str = ""):
    ''' Convert particles to a mesh object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def modifier_copy(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  modifier: str = ""):
    ''' Duplicate modifier at the same position in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def modifier_copy_to_selected(override_context: typing.
                              Union[typing.Dict, 'bpy.types.Context'] = None,
                              execution_context: typing.Union[str, int] = None,
                              undo: bool = None,
                              *,
                              modifier: str = ""):
    ''' Copy the modifier from the active object to all selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def modifier_move_down(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       modifier: str = ""):
    ''' Move modifier down in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def modifier_move_to_index(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None,
                           *,
                           modifier: str = "",
                           index: int = 0):
    ''' Change the modifier's index in the stack so it evaluates after the set number of others

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param index: Index, The index to move the modifier to
    :type index: int
    '''

    pass


def modifier_move_up(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     modifier: str = ""):
    ''' Move modifier up in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def modifier_remove(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    modifier: str = "",
                    report: bool = False):
    ''' Remove a modifier from the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def modifier_set_active(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        modifier: str = ""):
    ''' Activate the modifier to use as the context

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def move_to_collection(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       collection_index: int = -1,
                       is_new: bool = False,
                       new_collection_name: str = ""):
    ''' Move objects to a collection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param collection_index: Collection Index, Index of the collection to move to
    :type collection_index: int
    :param is_new: New, Move objects to a new collection
    :type is_new: bool
    :param new_collection_name: Name, Name of the newly added collection
    :type new_collection_name: str
    '''

    pass


def multires_base_apply(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        modifier: str = ""):
    ''' Modify the base mesh to conform to the displaced mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def multires_external_pack(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None):
    ''' Pack displacements from an external file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def multires_external_save(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None,
                           *,
                           filepath: str = "",
                           hide_props_region: bool = True,
                           check_existing: bool = True,
                           filter_blender: bool = False,
                           filter_backup: bool = False,
                           filter_image: bool = False,
                           filter_movie: bool = False,
                           filter_python: bool = False,
                           filter_font: bool = False,
                           filter_sound: bool = False,
                           filter_text: bool = False,
                           filter_archive: bool = False,
                           filter_btx: bool = True,
                           filter_collada: bool = False,
                           filter_alembic: bool = False,
                           filter_usd: bool = False,
                           filter_obj: bool = False,
                           filter_volume: bool = False,
                           filter_folder: bool = True,
                           filter_blenlib: bool = False,
                           filemode: int = 9,
                           relative_path: bool = True,
                           display_type: typing.Union[str, int] = 'DEFAULT',
                           sort_method: typing.Union[str, int] = '',
                           modifier: str = ""):
    ''' Save displacements to an external file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Path to file
    :type filepath: str
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: bool
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def multires_higher_levels_delete(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        modifier: str = ""):
    ''' Deletes the higher resolution mesh, potential loss of detail

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def multires_rebuild_subdiv(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None,
                            *,
                            modifier: str = ""):
    ''' Rebuilds all possible subdivisions levels to generate a lower resolution base mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def multires_reshape(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     modifier: str = ""):
    ''' Copy vertex coordinates from other object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def multires_subdivide(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       modifier: str = "",
                       mode: typing.Union[str, int] = 'CATMULL_CLARK'):
    ''' Add a new level of subdivision

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param mode: Subdivision Mode, How the mesh is going to be subdivided to create a new level * CATMULL_CLARK Catmull-Clark -- Create a new level using Catmull-Clark subdivisions. * SIMPLE Simple -- Create a new level using simple subdivisions. * LINEAR Linear -- Create a new level using linear interpolation of the sculpted displacement.
    :type mode: typing.Union[str, int]
    '''

    pass


def multires_unsubdivide(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         modifier: str = ""):
    ''' Rebuild a lower subdivision level of the current base mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def ocean_bake(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               modifier: str = "",
               free: bool = False):
    ''' Bake an image sequence of ocean data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param free: Free, Free the bake, rather than generating it
    :type free: bool
    '''

    pass


def origin_clear(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Clear the object's origin

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def origin_set(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               type: typing.Union[str, int] = 'GEOMETRY_ORIGIN',
               center: typing.Union[str, int] = 'MEDIAN'):
    ''' Set the object's origin, by either moving the data, or set to center of data, or use 3D cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * GEOMETRY_ORIGIN Geometry to Origin -- Move object geometry to object origin. * ORIGIN_GEOMETRY Origin to Geometry -- Calculate the center of geometry based on the current pivot point (median, otherwise bounding box). * ORIGIN_CURSOR Origin to 3D Cursor -- Move object origin to position of the 3D cursor. * ORIGIN_CENTER_OF_MASS Origin to Center of Mass (Surface) -- Calculate the center of mass from the surface area. * ORIGIN_CENTER_OF_VOLUME Origin to Center of Mass (Volume) -- Calculate the center of mass from the volume (must be manifold geometry with consistent normals).
    :type type: typing.Union[str, int]
    :param center: Center
    :type center: typing.Union[str, int]
    '''

    pass


def parent_clear(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 type: typing.Union[str, int] = 'CLEAR'):
    ''' Clear the object's parenting

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * CLEAR Clear Parent -- Completely clear the parenting relationship, including involved modifiers if any. * CLEAR_KEEP_TRANSFORM Clear and Keep Transformation -- As 'Clear Parent', but keep the current visual transformations of the object. * CLEAR_INVERSE Clear Parent Inverse -- Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.
    :type type: typing.Union[str, int]
    '''

    pass


def parent_inverse_apply(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Apply the object's parent inverse to its data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def parent_no_inverse_set(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          keep_transform: bool = False):
    ''' Set the object's parenting without setting the inverse parent correction

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param keep_transform: Keep Transform, Preserve the world transform throughout parenting
    :type keep_transform: bool
    '''

    pass


def parent_set(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               type: typing.Union[str, int] = 'OBJECT',
               xmirror: bool = False,
               keep_transform: bool = False):
    ''' Set the object's parenting

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    :param xmirror: X Mirror, Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation
    :type xmirror: bool
    :param keep_transform: Keep Transform, Apply transformation before parenting
    :type keep_transform: bool
    '''

    pass


def particle_system_add(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Add a particle system

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def particle_system_remove(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None):
    ''' Remove the selected particle system

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def paths_calculate(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    display_type: typing.Union[int, str] = 'RANGE',
                    range: typing.Union[int, str] = 'SCENE'):
    ''' Generate motion paths for the selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param display_type: Display type
    :type display_type: typing.Union[int, str]
    :param range: Computation Range
    :type range: typing.Union[int, str]
    '''

    pass


def paths_clear(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                only_selected: bool = False):
    ''' Clear path caches for all objects, hold Shift key for selected objects only

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param only_selected: Only Selected, Only clear paths from selected objects
    :type only_selected: bool
    '''

    pass


def paths_update(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Recalculate motion paths for selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def paths_update_visible(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Recalculate all visible motion paths for objects and poses

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def pointcloud_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add a point cloud object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def posemode_toggle(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Enable or disable posing/selecting bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def quadriflow_remesh(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      use_mesh_symmetry: bool = True,
                      use_preserve_sharp: bool = False,
                      use_preserve_boundary: bool = False,
                      preserve_paint_mask: bool = False,
                      smooth_normals: bool = False,
                      mode: typing.Union[str, int] = 'FACES',
                      target_ratio: float = 1.0,
                      target_edge_length: float = 0.1,
                      target_faces: int = 4000,
                      mesh_area: float = -1.0,
                      seed: int = 0):
    ''' Create a new quad based mesh using the surface data of the current mesh. All data layers will be lost

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_mesh_symmetry: Use Mesh Symmetry, Generates a symmetrical mesh using the mesh symmetry configuration
    :type use_mesh_symmetry: bool
    :param use_preserve_sharp: Preserve Sharp, Try to preserve sharp features on the mesh
    :type use_preserve_sharp: bool
    :param use_preserve_boundary: Preserve Mesh Boundary, Try to preserve mesh boundary on the mesh
    :type use_preserve_boundary: bool
    :param preserve_paint_mask: Preserve Paint Mask, Reproject the paint mask onto the new mesh
    :type preserve_paint_mask: bool
    :param smooth_normals: Smooth Normals, Set the output mesh normals to smooth
    :type smooth_normals: bool
    :param mode: Mode, How to specify the amount of detail for the new mesh * RATIO Ratio -- Specify target number of faces relative to the current mesh. * EDGE Edge Length -- Input target edge length in the new mesh. * FACES Faces -- Input target number of faces in the new mesh.
    :type mode: typing.Union[str, int]
    :param target_ratio: Ratio, Relative number of faces compared to the current mesh
    :type target_ratio: float
    :param target_edge_length: Edge Length, Target edge length in the new mesh
    :type target_edge_length: float
    :param target_faces: Number of Faces, Approximate number of faces (quads) in the new mesh
    :type target_faces: int
    :param mesh_area: Old Object Face Area, This property is only used to cache the object area for later calculations
    :type mesh_area: float
    :param seed: Seed, Random seed to use with the solver. Different seeds will cause the remesher to come up with different quad layouts on the mesh
    :type seed: int
    '''

    pass


def quick_explode(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  style: typing.Union[str, int] = 'EXPLODE',
                  amount: int = 100,
                  frame_duration: int = 50,
                  frame_start: int = 1,
                  frame_end: int = 10,
                  velocity: float = 1.0,
                  fade: bool = True):
    ''' Make selected objects explode

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param style: Explode Style
    :type style: typing.Union[str, int]
    :param amount: Number of Pieces
    :type amount: int
    :param frame_duration: Duration
    :type frame_duration: int
    :param frame_start: Start Frame
    :type frame_start: int
    :param frame_end: End Frame
    :type frame_end: int
    :param velocity: Outwards Velocity
    :type velocity: float
    :param fade: Fade, Fade the pieces over time
    :type fade: bool
    '''

    pass


def quick_fur(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              density: typing.Union[str, int] = 'MEDIUM',
              view_percentage: int = 10,
              length: float = 0.1):
    ''' Add fur setup to the selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param density: Fur Density
    :type density: typing.Union[str, int]
    :param view_percentage: View %
    :type view_percentage: int
    :param length: Length
    :type length: float
    '''

    pass


def quick_liquid(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 show_flows: bool = False):
    ''' Make selected objects liquid

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param show_flows: Render Liquid Objects, Keep the liquid objects visible during rendering
    :type show_flows: bool
    '''

    pass


def quick_smoke(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                style: typing.Union[str, int] = 'SMOKE',
                show_flows: bool = False):
    ''' Use selected objects as smoke emitters

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param style: Smoke Style
    :type style: typing.Union[str, int]
    :param show_flows: Render Smoke Objects, Keep the smoke objects visible during rendering
    :type show_flows: bool
    '''

    pass


def randomize_transform(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        random_seed: int = 0,
        use_delta: bool = False,
        use_loc: bool = True,
        loc: typing.Union[typing.List[float], typing.
                          Tuple[float, float, float], 'mathutils.Vector'] = (
                              0.0, 0.0, 0.0),
        use_rot: bool = True,
        rot: typing.Union[typing.List[float], typing.
                          Tuple[float, float, float], 'mathutils.Vector'] = (
                              0.0, 0.0, 0.0),
        use_scale: bool = True,
        scale_even: bool = False,
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                1.0, 1.0, 1.0)):
    ''' Randomize objects location, rotation, and scale

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param random_seed: Random Seed, Seed value for the random generator
    :type random_seed: int
    :param use_delta: Transform Delta, Randomize delta transform values instead of regular transform
    :type use_delta: bool
    :param use_loc: Randomize Location, Randomize the location values
    :type use_loc: bool
    :param loc: Location, Maximum distance the objects can spread over each axis
    :type loc: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param use_rot: Randomize Rotation, Randomize the rotation values
    :type use_rot: bool
    :param rot: Rotation, Maximum rotation over each axis
    :type rot: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param use_scale: Randomize Scale, Randomize the scale values
    :type use_scale: bool
    :param scale_even: Scale Even, Use the same scale value for all axis
    :type scale_even: bool
    :param scale: Scale, Maximum scale randomization over each axis
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def reset_override_library(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None):
    ''' Reset the selected local overrides to their linked references values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def rotation_clear(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   clear_delta: bool = False):
    ''' Clear the object's rotation

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param clear_delta: Clear Delta, Clear delta rotation in addition to clearing the normal rotation transform
    :type clear_delta: bool
    '''

    pass


def scale_clear(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                clear_delta: bool = False):
    ''' Clear the object's scale

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param clear_delta: Clear Delta, Clear delta scale in addition to clearing the normal scale transform
    :type clear_delta: bool
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               action: typing.Union[str, int] = 'TOGGLE'):
    ''' Change selection of all visible objects in scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_by_type(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   extend: bool = False,
                   type: typing.Union[int, str] = 'MESH'):
    ''' Select all visible objects that are of a type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def select_camera(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  extend: bool = False):
    ''' Select the active camera

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend the selection
    :type extend: bool
    '''

    pass


def select_grouped(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   extend: bool = False,
                   type: typing.Union[str, int] = 'CHILDREN_RECURSIVE'):
    ''' Select all visible objects grouped by various properties

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param type: Type * CHILDREN_RECURSIVE Children. * CHILDREN Immediate Children. * PARENT Parent. * SIBLINGS Siblings -- Shared parent. * TYPE Type -- Shared object type. * COLLECTION Collection -- Shared collection. * HOOK Hook. * PASS Pass -- Render pass index. * COLOR Color -- Object color. * KEYINGSET Keying Set -- Objects included in active Keying Set. * LIGHT_TYPE Light Type -- Matching light types.
    :type type: typing.Union[str, int]
    '''

    pass


def select_hierarchy(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     direction: typing.Union[str, int] = 'PARENT',
                     extend: bool = False):
    ''' Select object relative to the active object's position in the hierarchy

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param direction: Direction, Direction to select in the hierarchy
    :type direction: typing.Union[str, int]
    :param extend: Extend, Extend the existing selection
    :type extend: bool
    '''

    pass


def select_less(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Deselect objects at the boundaries of parent/child relationships

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_linked(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  extend: bool = False,
                  type: typing.Union[str, int] = 'OBDATA'):
    ''' Select all visible objects that are linked

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def select_mirror(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  extend: bool = False):
    ''' Select the mirror objects of the selected object e.g. "L.sword" and "R.sword"

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    '''

    pass


def select_more(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Select connected parent/child objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_pattern(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   pattern: str = "*",
                   case_sensitive: bool = False,
                   extend: bool = True):
    ''' Select objects matching a naming pattern

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param pattern: Pattern, Name filter using '*', '?' and '[abc]' unix style wildcards
    :type pattern: str
    :param case_sensitive: Case Sensitive, Do a case sensitive compare
    :type case_sensitive: bool
    :param extend: Extend, Extend the existing selection
    :type extend: bool
    '''

    pass


def select_random(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  ratio: float = 0.5,
                  seed: int = 0,
                  action: typing.Union[str, int] = 'SELECT'):
    ''' Set select on random visible objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param ratio: Ratio, Portion of items to select randomly
    :type ratio: float
    :param seed: Random Seed, Seed for the random number generator
    :type seed: int
    :param action: Action, Selection action to execute * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_same_collection(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None,
                           *,
                           collection: str = ""):
    ''' Select object in the same collection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param collection: Collection, Name of the collection to select
    :type collection: str
    '''

    pass


def shade_flat(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Render and display faces uniform, using Face Normals

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def shade_smooth(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 use_auto_smooth: bool = False,
                 auto_smooth_angle: float = 0.523599):
    ''' Render and display faces smooth, using interpolated Vertex Normals

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_auto_smooth: Auto Smooth, Enable automatic smooth based on smooth/sharp faces/edges and angle between faces
    :type use_auto_smooth: bool
    :param auto_smooth_angle: Angle, Maximum angle between face normals that will be considered as smooth(unused if custom split normals data are available)
    :type auto_smooth_angle: float
    '''

    pass


def shaderfx_add(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 type: typing.Union[int, str] = 'FX_BLUR'):
    ''' Add a visual effect to the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def shaderfx_copy(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  shaderfx: str = ""):
    ''' Duplicate effect at the same position in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: str
    '''

    pass


def shaderfx_move_down(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       shaderfx: str = ""):
    ''' Move effect down in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: str
    '''

    pass


def shaderfx_move_to_index(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None,
                           *,
                           shaderfx: str = "",
                           index: int = 0):
    ''' Change the effect's position in the list so it evaluates after the set number of others

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: str
    :param index: Index, The index to move the effect to
    :type index: int
    '''

    pass


def shaderfx_move_up(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     shaderfx: str = ""):
    ''' Move effect up in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: str
    '''

    pass


def shaderfx_remove(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    shaderfx: str = "",
                    report: bool = False):
    ''' Remove a effect from the active grease pencil object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: str
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def shape_key_add(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  from_mix: bool = True):
    ''' Add shape key to the object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param from_mix: From Mix, Create the new shape key from the existing mix of keys
    :type from_mix: bool
    '''

    pass


def shape_key_clear(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Clear weights for all shape keys

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def shape_key_mirror(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     use_topology: bool = False):
    ''' Mirror the current shape key along the local X axis

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
    :type use_topology: bool
    '''

    pass


def shape_key_move(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   type: typing.Union[str, int] = 'TOP'):
    ''' Move the active shape key up/down in the list

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * TOP Top -- Top of the list. * UP Up. * DOWN Down. * BOTTOM Bottom -- Bottom of the list.
    :type type: typing.Union[str, int]
    '''

    pass


def shape_key_remove(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     all: bool = False,
                     apply_mix: bool = False):
    ''' Remove shape key from the object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param all: All, Remove all shape keys
    :type all: bool
    :param apply_mix: Apply Mix, Apply current mix of shape keys to the geometry before removing them
    :type apply_mix: bool
    '''

    pass


def shape_key_retime(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Resets the timing for absolute shape keys

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def shape_key_transfer(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       mode: typing.Union[str, int] = 'OFFSET',
                       use_clamp: bool = False):
    ''' Copy the active shape key of another selected object to this one

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Transformation Mode, Relative shape positions to the new shape method * OFFSET Offset -- Apply the relative positional offset. * RELATIVE_FACE Relative Face -- Calculate relative position (using faces). * RELATIVE_EDGE Relative Edge -- Calculate relative position (using edges).
    :type mode: typing.Union[str, int]
    :param use_clamp: Clamp Offset, Clamp the transformation to the distance each vertex moves in the original shape
    :type use_clamp: bool
    '''

    pass


def skin_armature_create(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         modifier: str = ""):
    ''' Create an armature that parallels the skin layout

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def skin_loose_mark_clear(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          action: typing.Union[str, int] = 'MARK'):
    ''' Mark/clear selected vertices as loose

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param action: Action * MARK Mark -- Mark selected vertices as loose. * CLEAR Clear -- Set selected vertices as not loose.
    :type action: typing.Union[str, int]
    '''

    pass


def skin_radii_equalize(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Make skin radii of selected vertices equal on each axis

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def skin_root_mark(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Mark selected vertices as roots

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def speaker_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add a speaker object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def subdivision_set(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    level: int = 1,
                    relative: bool = False):
    ''' Sets a Subdivision Surface level (1 to 5)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param level: Level
    :type level: int
    :param relative: Relative, Apply the subdivision surface level as an offset relative to the current level
    :type relative: bool
    '''

    pass


def surfacedeform_bind(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       modifier: str = ""):
    ''' Bind mesh to target in surface deform modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def text_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        radius: float = 1.0,
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add a text object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def track_clear(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                type: typing.Union[str, int] = 'CLEAR'):
    ''' Clear tracking constraint or flag from object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def track_set(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              type: typing.Union[str, int] = 'DAMPTRACK'):
    ''' Make the object track another object, using various methods/constraints

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def transfer_mode(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  use_flash_on_transfer: bool = True):
    ''' Switches the active object and assigns the same mode to a new one under the mouse cursor, leaving the active mode in the current one

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_flash_on_transfer: Flash On Transfer, Flash the target object when transferring the mode
    :type use_flash_on_transfer: bool
    '''

    pass


def transform_apply(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    location: bool = True,
                    rotation: bool = True,
                    scale: bool = True,
                    properties: bool = True,
                    isolate_users: bool = False):
    ''' Apply the object's transformation to its data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param location: Location
    :type location: bool
    :param rotation: Rotation
    :type rotation: bool
    :param scale: Scale
    :type scale: bool
    :param properties: Apply Properties, Modify properties such as curve vertex radius, font size and bone envelope
    :type properties: bool
    :param isolate_users: Isolate Multi User Data, Create new object-data users if needed
    :type isolate_users: bool
    '''

    pass


def transform_axis_target(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Interactively point cameras and lights to a location (Ctrl translates)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def transform_to_mouse(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        name: str = "",
        session_uuid: int = 0,
        matrix: typing.
        Union[typing.List[typing.List[float]], typing.
              Tuple[typing.Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float], typing.
                    Tuple[float, float, float, float]], 'mathutils.Matrix'] = (
                        (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0),
                        (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)),
        drop_x: int = 0,
        drop_y: int = 0):
    ''' Snap selected item(s) to the mouse location

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Object name to place (uses the active object when this and 'session_uuid' are unset)
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the object to place (uses the active object when this and 'name' are unset)
    :type session_uuid: int
    :param matrix: Matrix
    :type matrix: typing.Union[typing.List[typing.List[float]], typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]], 'mathutils.Matrix']
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: int
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: int
    '''

    pass


def transforms_to_deltas(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         mode: typing.Union[str, int] = 'ALL',
                         reset_values: bool = True):
    ''' Convert normal object transforms to delta transforms, any existing delta transforms will be included as well

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode, Which transforms to transfer * ALL All Transforms -- Transfer location, rotation, and scale transforms. * LOC Location -- Transfer location transforms only. * ROT Rotation -- Transfer rotation transforms only. * SCALE Scale -- Transfer scale transforms only.
    :type mode: typing.Union[str, int]
    :param reset_values: Reset Values, Clear transform values after transferring to deltas
    :type reset_values: bool
    '''

    pass


def unlink_data(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_add(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Add a new vertex group to the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_assign(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Assign the selected vertices to the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_assign_new(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None):
    ''' Assign the selected vertices to a new vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_clean(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       group_select_mode: typing.Union[str, int] = '',
                       limit: float = 0.0,
                       keep_single: bool = False):
    ''' Remove vertex group assignments which are not required

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Union[str, int]
    :param limit: Limit, Remove vertices which weight is below or equal to this limit
    :type limit: float
    :param keep_single: Keep Single, Keep verts assigned to at least one group when cleaning
    :type keep_single: bool
    '''

    pass


def vertex_group_copy(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Make a copy of the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_copy_to_selected(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Replace vertex groups of selected objects by vertex groups of active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_deselect(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Deselect all selected vertices assigned to the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_fix(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     dist: float = 0.0,
                     strength: float = 1.0,
                     accuracy: float = 1.0):
    ''' Modify the position of selected vertices by changing only their respective groups' weights (this tool may be slow for many vertices)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param dist: Distance, The distance to move to
    :type dist: float
    :param strength: Strength, The distance moved can be changed by this multiplier
    :type strength: float
    :param accuracy: Change Sensitivity, Change the amount weights are altered with each iteration: lower values are slower
    :type accuracy: float
    '''

    pass


def vertex_group_invert(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        group_select_mode: typing.Union[str, int] = '',
                        auto_assign: bool = True,
                        auto_remove: bool = True):
    ''' Invert active vertex group's weights

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Union[str, int]
    :param auto_assign: Add Weights, Add vertices from groups that have zero weight before inverting
    :type auto_assign: bool
    :param auto_remove: Remove Weights, Remove vertices from groups that have zero weight after inverting
    :type auto_remove: bool
    '''

    pass


def vertex_group_levels(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        group_select_mode: typing.Union[str, int] = '',
                        offset: float = 0.0,
                        gain: float = 1.0):
    ''' Add some offset and multiply with some gain the weights of the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Union[str, int]
    :param offset: Offset, Value to add to weights
    :type offset: float
    :param gain: Gain, Value to multiply weights by
    :type gain: float
    '''

    pass


def vertex_group_limit_total(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None,
                             *,
                             group_select_mode: typing.Union[str, int] = '',
                             limit: int = 4):
    ''' Limit deform weights associated with a vertex to a specified number by removing lowest weights

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Union[str, int]
    :param limit: Limit, Maximum number of deform weights
    :type limit: int
    '''

    pass


def vertex_group_lock(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      action: typing.Union[str, int] = 'TOGGLE',
                      mask: typing.Union[str, int] = 'ALL'):
    ''' Change the lock state of all or some vertex groups of active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param action: Action, Lock action to execute on vertex groups * TOGGLE Toggle -- Unlock all vertex groups if there is at least one locked group, lock all in other case. * LOCK Lock -- Lock all vertex groups. * UNLOCK Unlock -- Unlock all vertex groups. * INVERT Invert -- Invert the lock state of all vertex groups.
    :type action: typing.Union[str, int]
    :param mask: Mask, Apply the action based on vertex group selection * ALL All -- Apply action to all vertex groups. * SELECTED Selected -- Apply to selected vertex groups. * UNSELECTED Unselected -- Apply to unselected vertex groups. * INVERT_UNSELECTED Invert Unselected -- Apply the opposite of Lock/Unlock to unselected vertex groups.
    :type mask: typing.Union[str, int]
    '''

    pass


def vertex_group_mirror(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        mirror_weights: bool = True,
                        flip_group_names: bool = True,
                        all_groups: bool = False,
                        use_topology: bool = False):
    ''' Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mirror_weights: Mirror Weights, Mirror weights
    :type mirror_weights: bool
    :param flip_group_names: Flip Group Names, Flip vertex group names
    :type flip_group_names: bool
    :param all_groups: All Groups, Mirror all vertex groups weights
    :type all_groups: bool
    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
    :type use_topology: bool
    '''

    pass


def vertex_group_move(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      direction: typing.Union[str, int] = 'UP'):
    ''' Move the active vertex group up/down in the list

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param direction: Direction, Direction to move the active vertex group towards
    :type direction: typing.Union[str, int]
    '''

    pass


def vertex_group_normalize(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None):
    ''' Normalize weights of the active vertex group, so that the highest ones are now 1.0

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_normalize_all(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        group_select_mode: typing.Union[str, int] = '',
        lock_active: bool = True):
    ''' Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Union[str, int]
    :param lock_active: Lock Active, Keep the values of the active group while normalizing others
    :type lock_active: bool
    '''

    pass


def vertex_group_quantize(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          group_select_mode: typing.Union[str, int] = '',
                          steps: int = 4):
    ''' Set weights to a fixed number of steps

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Union[str, int]
    :param steps: Steps, Number of steps between 0 and 1
    :type steps: int
    '''

    pass


def vertex_group_remove(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        all: bool = False,
                        all_unlocked: bool = False):
    ''' Delete the active or all vertex groups from the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param all: All, Remove all vertex groups
    :type all: bool
    :param all_unlocked: All Unlocked, Remove all unlocked vertex groups
    :type all_unlocked: bool
    '''

    pass


def vertex_group_remove_from(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None,
                             *,
                             use_all_groups: bool = False,
                             use_all_verts: bool = False):
    ''' Remove the selected vertices from active or all vertex group(s)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_all_groups: All Groups, Remove from all groups
    :type use_all_groups: bool
    :param use_all_verts: All Vertices, Clear the active group
    :type use_all_verts: bool
    '''

    pass


def vertex_group_select(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Select all the vertices assigned to the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_group_set_active(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None,
                            *,
                            group: typing.Union[str, int] = ''):
    ''' Set the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param group: Group, Vertex group to set as active
    :type group: typing.Union[str, int]
    '''

    pass


def vertex_group_smooth(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        group_select_mode: typing.Union[str, int] = '',
                        factor: float = 0.5,
                        repeat: int = 1,
                        expand: float = 0.0):
    ''' Smooth weights for selected vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Union[str, int]
    :param factor: Factor
    :type factor: float
    :param repeat: Iterations
    :type repeat: int
    :param expand: Expand/Contract, Expand/contract weights
    :type expand: float
    '''

    pass


def vertex_group_sort(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      sort_type: typing.Union[str, int] = 'NAME'):
    ''' Sort vertex groups

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param sort_type: Sort Type, Sort type
    :type sort_type: typing.Union[str, int]
    '''

    pass


def vertex_parent_set(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Parent selected objects to the selected vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_weight_copy(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Copy weights from active to selected

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_weight_delete(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         weight_group: int = -1):
    ''' Delete this weight from the vertex (disabled if vertex group is locked)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: int
    '''

    pass


def vertex_weight_normalize_active_vertex(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Normalize active vertex's weights

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def vertex_weight_paste(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        weight_group: int = -1):
    ''' Copy this group's weight to other selected vertices (disabled if vertex group is locked)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: int
    '''

    pass


def vertex_weight_set_active(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None,
                             *,
                             weight_group: int = -1):
    ''' Set as active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: int
    '''

    pass


def visual_transform_apply(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None):
    ''' Apply the object's visual transformation to its data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def volume_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Add a volume object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def volume_import(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        filepath: str = "",
        directory: str = "",
        files: bpy.types.
        bpy_prop_collection['bpy.types.OperatorFileListElement'] = None,
        hide_props_region: bool = True,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_archive: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_usd: bool = False,
        filter_obj: bool = False,
        filter_volume: bool = True,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 9,
        relative_path: bool = True,
        display_type: typing.Union[str, int] = 'DEFAULT',
        sort_method: typing.Union[str, int] = '',
        use_sequence_detection: bool = True,
        align: typing.Union[str, int] = 'WORLD',
        location: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        rotation: typing.
        Union[typing.List[float], typing.
              Tuple[float, float, float], 'mathutils.Vector'] = (0.0, 0.0,
                                                                 0.0),
        scale: typing.Union[typing.List[float], typing.
                            Tuple[float, float, float], 'mathutils.Vector'] = (
                                0.0, 0.0, 0.0)):
    ''' Import OpenVDB volume file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param files: Files
    :type files: bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int]
    :param use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected volume files (based on file names)
    :type use_sequence_detection: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    :param scale: Scale, Scale for the newly added object
    :type scale: typing.Union[typing.List[float], typing.Tuple[float, float, float], 'mathutils.Vector']
    '''

    pass


def voxel_remesh(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Calculates a new manifold mesh based on the volume of the current mesh. All data layers will be lost

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def voxel_size_edit(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Modify the mesh voxel size interactively used in the voxel remesher

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
