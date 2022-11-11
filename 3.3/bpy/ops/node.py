import sys
import typing
import bpy.types
import bl_operators.node
import bpy.ops.transform
import mathutils

GenericType = typing.TypeVar("GenericType")


def add_and_link_node(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        type: str = "",
        use_transform: bool = False,
        settings: bpy.types.
        bpy_prop_collection['bl_operators.node.NodeSetting'] = None,
        link_socket_index: int = 0):
    ''' Add a node to the active tree and link to an existing socket

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Node Type, Node type
    :type type: str
    :param use_transform: Use Transform, Start transform operator after inserting the node
    :type use_transform: bool
    :param settings: Settings, Settings to be applied on the newly created node
    :type settings: bpy.types.bpy_prop_collection['bl_operators.node.NodeSetting']
    :param link_socket_index: Link Socket Index, Index of the socket to link
    :type link_socket_index: int
    '''

    pass


def add_collection(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   name: str = "",
                   session_uuid: int = 0):
    ''' Add an collection info node to the current node editor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    '''

    pass


def add_file(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             filepath: str = "",
             hide_props_region: bool = True,
             filter_blender: bool = False,
             filter_backup: bool = False,
             filter_image: bool = True,
             filter_movie: bool = True,
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
             filter_volume: bool = False,
             filter_folder: bool = True,
             filter_blenlib: bool = False,
             filemode: int = 9,
             relative_path: bool = True,
             show_multiview: bool = False,
             use_multiview: bool = False,
             display_type: typing.Union[str, int] = 'DEFAULT',
             sort_method: typing.Union[str, int] = '',
             name: str = "",
             session_uuid: int = 0):
    ''' Add a file node to the current node editor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Path to file
    :type filepath: str
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
    :param show_multiview: Enable Multi-View
    :type show_multiview: bool
    :param use_multiview: Use Multi-View
    :type use_multiview: bool
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int]
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    '''

    pass


def add_group(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              name: str = "",
              session_uuid: int = 0):
    ''' Add an existing node group to the current node editor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    '''

    pass


def add_mask(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             name: str = "",
             session_uuid: int = 0):
    ''' Add a mask node to the current node editor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    '''

    pass


def add_node(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             type: str = "",
             use_transform: bool = False,
             settings: bpy.types.
             bpy_prop_collection['bl_operators.node.NodeSetting'] = None):
    ''' Add a node to the active tree

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Node Type, Node type
    :type type: str
    :param use_transform: Use Transform, Start transform operator after inserting the node
    :type use_transform: bool
    :param settings: Settings, Settings to be applied on the newly created node
    :type settings: bpy.types.bpy_prop_collection['bl_operators.node.NodeSetting']
    '''

    pass


def add_object(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               name: str = "",
               session_uuid: int = 0):
    ''' Add an object info node to the current node editor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    '''

    pass


def add_reroute(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                path: bpy.types.
                bpy_prop_collection['bpy.types.OperatorMousePath'] = None,
                cursor: int = 8):
    ''' Add a reroute node

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param path: Path
    :type path: bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']
    :param cursor: Cursor
    :type cursor: int
    '''

    pass


def add_search(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               type: str = "",
               use_transform: bool = False,
               settings: bpy.types.
               bpy_prop_collection['bl_operators.node.NodeSetting'] = None,
               node_item: typing.Union[str, int] = ''):
    ''' Add a node to the active tree

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Node Type, Node type
    :type type: str
    :param use_transform: Use Transform, Start transform operator after inserting the node
    :type use_transform: bool
    :param settings: Settings, Settings to be applied on the newly created node
    :type settings: bpy.types.bpy_prop_collection['bl_operators.node.NodeSetting']
    :param node_item: Node Type, Node type
    :type node_item: typing.Union[str, int]
    '''

    pass


def attach(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Attach active node to a frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def backimage_fit(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Fit the background image to the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def backimage_move(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Move node backdrop

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def backimage_sample(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Use mouse to sample background image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def backimage_zoom(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   factor: float = 1.2):
    ''' Zoom in/out the background image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Factor
    :type factor: float
    '''

    pass


def clear_viewer_border(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Clear the boundaries for viewer operations

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def clipboard_copy(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Copies selected nodes to the clipboard

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def clipboard_paste(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Pastes nodes from the clipboard to the active node tree

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def collapse_hide_unused_toggle(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Toggle collapsed nodes and hide unused sockets :file: startup/bl_operators/node.py\:268 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/node.py$268> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def cryptomatte_layer_add(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Add a new input layer to a Cryptomatte node

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def cryptomatte_layer_remove(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None):
    ''' Remove layer from a Cryptomatte node

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Delete selected nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def delete_reconnect(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Delete nodes; will reconnect nodes as if deletion was muted

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def detach(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Detach selected nodes from parents

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def detach_translate_attach(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        NODE_OT_detach: 'detach' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None,
        NODE_OT_attach: 'attach' = None):
    ''' Detach nodes, move and attach to frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param NODE_OT_detach: Detach Nodes, Detach selected nodes from parents
    :type NODE_OT_detach: 'detach'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame
    :type NODE_OT_attach: 'attach'
    '''

    pass


def duplicate(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              keep_inputs: bool = False):
    ''' Duplicate selected nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param keep_inputs: Keep Inputs, Keep the input links to duplicated nodes
    :type keep_inputs: bool
    '''

    pass


def duplicate_move(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   NODE_OT_duplicate: 'duplicate' = None,
                   NODE_OT_translate_attach: 'translate_attach' = None):
    ''' Duplicate selected nodes and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes
    :type NODE_OT_duplicate: 'duplicate'
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    :type NODE_OT_translate_attach: 'translate_attach'
    '''

    pass


def duplicate_move_keep_inputs(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        NODE_OT_duplicate: 'duplicate' = None,
        NODE_OT_translate_attach: 'translate_attach' = None):
    ''' Duplicate selected nodes keeping input links and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes
    :type NODE_OT_duplicate: 'duplicate'
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    :type NODE_OT_translate_attach: 'translate_attach'
    '''

    pass


def find_node(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              prev: bool = False):
    ''' Search for a node by name and focus and select it

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param prev: Previous
    :type prev: bool
    '''

    pass


def gltf_settings_node_operator(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Add a node to the active tree for glTF export :file: addons/io_scene_gltf2/blender/com/gltf2_blender_ui.py\:29 <https://developer.blender.org/diffusion/BA/addons/io_scene_gltf2/blender/com/gltf2_blender_ui.py$29> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def group_edit(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               exit: bool = False):
    ''' Edit node group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param exit: Exit
    :type exit: bool
    '''

    pass


def group_insert(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Insert selected nodes into a node group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def group_make(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Make group from selected nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def group_separate(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   type: typing.Union[str, int] = 'COPY'):
    ''' Separate selected nodes from the node group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * COPY Copy -- Copy to parent node tree, keep group intact. * MOVE Move -- Move to parent node tree, remove from group.
    :type type: typing.Union[str, int]
    '''

    pass


def group_ungroup(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Ungroup selected nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def hide_socket_toggle(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Toggle unused node socket display

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def hide_toggle(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Toggle hiding of selected nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def insert_offset(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Automatically offset nodes on insertion

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def join(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None):
    ''' Attach selected nodes to a new common frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def link(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         detach: bool = False,
         has_link_picked: bool = False,
         drag_start: typing.Union[typing.List[float], typing.
                                  Tuple[float, float], 'mathutils.Vector'] = (
                                      0.0, 0.0),
         inside_padding: float = 2.0,
         outside_padding: float = 0.0,
         speed_ramp: float = 1.0,
         max_speed: float = 26.0,
         delay: float = 0.5,
         zoom_influence: float = 0.5):
    ''' Use the mouse to create a link between two nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param detach: Detach, Detach and redirect existing links
    :type detach: bool
    :param has_link_picked: Has Link Picked, The operation has placed a link. Only used for multi-input sockets, where the link is picked later
    :type has_link_picked: bool
    :param drag_start: Drag Start, The position of the mouse cursor at the start of the operation
    :type drag_start: typing.Union[typing.List[float], typing.Tuple[float, float], 'mathutils.Vector']
    :param inside_padding: Inside Padding, Inside distance in UI units from the edge of the region within which to start panning
    :type inside_padding: float
    :param outside_padding: Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning
    :type outside_padding: float
    :param speed_ramp: Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge
    :type speed_ramp: float
    :param max_speed: Max Speed, Maximum speed in UI units per second
    :type max_speed: float
    :param delay: Delay, Delay in seconds before maximum speed is reached
    :type delay: float
    :param zoom_influence: Zoom Influence, Influence of the zoom factor on scroll speed
    :type zoom_influence: float
    '''

    pass


def link_make(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              replace: bool = False):
    ''' Makes a link between selected output in input sockets

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param replace: Replace, Replace socket connections with the new links
    :type replace: bool
    '''

    pass


def link_viewer(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Link to viewer node

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def links_cut(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              path: bpy.types.
              bpy_prop_collection['bpy.types.OperatorMousePath'] = None,
              cursor: int = 12):
    ''' Use the mouse to cut (remove) some links

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param path: Path
    :type path: bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']
    :param cursor: Cursor
    :type cursor: int
    '''

    pass


def links_detach(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Remove all links to selected nodes, and try to connect neighbor nodes together

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def links_mute(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               path: bpy.types.
               bpy_prop_collection['bpy.types.OperatorMousePath'] = None,
               cursor: int = 35):
    ''' Use the mouse to mute links

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param path: Path
    :type path: bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']
    :param cursor: Cursor
    :type cursor: int
    '''

    pass


def move_detach_links(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        NODE_OT_links_detach: 'links_detach' = None,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None,
        NODE_OT_insert_offset: 'insert_offset' = None):
    ''' Move a node to detach links

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param NODE_OT_links_detach: Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together
    :type NODE_OT_links_detach: 'links_detach'
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    :param NODE_OT_insert_offset: Insert Offset, Automatically offset nodes on insertion
    :type NODE_OT_insert_offset: 'insert_offset'
    '''

    pass


def move_detach_links_release(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        NODE_OT_links_detach: 'links_detach' = None,
        NODE_OT_translate_attach: 'translate_attach' = None):
    ''' Move a node to detach links

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param NODE_OT_links_detach: Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together
    :type NODE_OT_links_detach: 'links_detach'
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    :type NODE_OT_translate_attach: 'translate_attach'
    '''

    pass


def mute_toggle(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Toggle muting of the nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def new_geometry_node_group_assign(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Create a new geometry node group and assign it to the active modifier :file: startup/bl_operators/geometry_nodes.py\:72 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/geometry_nodes.py$72> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def new_geometry_nodes_modifier(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Create a new modifier with a new geometry node group :file: startup/bl_operators/geometry_nodes.py\:49 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/geometry_nodes.py$49> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def new_node_tree(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  type: typing.Union[str, int] = '',
                  name: str = "NodeTree"):
    ''' Create a new node tree

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Tree Type
    :type type: typing.Union[str, int]
    :param name: Name
    :type name: str
    '''

    pass


def node_color_preset_add(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          name: str = "",
                          remove_name: bool = False,
                          remove_active: bool = False):
    ''' Add or remove a Node Color Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    '''

    pass


def node_copy_color(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Copy color to all selected nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def options_toggle(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Toggle option buttons display for selected nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def output_file_add_socket(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None,
                           *,
                           file_path: str = "Image"):
    ''' Add a new input to a file output node

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param file_path: File Path, Subpath of the output file
    :type file_path: str
    '''

    pass


def output_file_move_active_socket(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        direction: typing.Union[str, int] = 'DOWN'):
    ''' Move the active input of a file output node up or down the list

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param direction: Direction
    :type direction: typing.Union[str, int]
    '''

    pass


def output_file_remove_active_socket(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Remove active input from a file output node

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def parent_set(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Attach selected nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def preview_toggle(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Toggle preview display for selected nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def read_viewlayers(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Read all render layers of all used scenes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def render_changed(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Render current scene, when input node's layer has been changed

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def resize(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Resize a node

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           extend: bool = False,
           deselect: bool = False,
           toggle: bool = False,
           deselect_all: bool = False,
           select_passthrough: bool = False,
           location: typing.List[int] = (0, 0),
           socket_select: bool = False):
    ''' Select the node under the cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param deselect: Deselect, Remove from selection
    :type deselect: bool
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: bool
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: bool
    :param location: Location, Mouse location
    :type location: typing.List[int]
    :param socket_select: Socket Select
    :type socket_select: bool
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               action: typing.Union[str, int] = 'TOGGLE'):
    ''' (De)select all nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_box(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               tweak: bool = False,
               xmin: int = 0,
               xmax: int = 0,
               ymin: int = 0,
               ymax: int = 0,
               wait_for_input: bool = True,
               mode: typing.Union[str, int] = 'SET'):
    ''' Use box selection to select nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param tweak: Tweak, Only activate when mouse is not over a node (useful for tweak gesture)
    :type tweak: bool
    :param xmin: X Min
    :type xmin: int
    :param xmax: X Max
    :type xmax: int
    :param ymin: Y Min
    :type ymin: int
    :param ymax: Y Max
    :type ymax: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection.
    :type mode: typing.Union[str, int]
    '''

    pass


def select_circle(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  x: int = 0,
                  y: int = 0,
                  radius: int = 25,
                  wait_for_input: bool = True,
                  mode: typing.Union[str, int] = 'SET'):
    ''' Use circle selection to select nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param x: X
    :type x: int
    :param y: Y
    :type y: int
    :param radius: Radius
    :type radius: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection.
    :type mode: typing.Union[str, int]
    '''

    pass


def select_grouped(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   extend: bool = False,
                   type: typing.Union[str, int] = 'TYPE'):
    ''' Select nodes with similar properties

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def select_lasso(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 tweak: bool = False,
                 path: bpy.types.
                 bpy_prop_collection['bpy.types.OperatorMousePath'] = None,
                 mode: typing.Union[str, int] = 'SET'):
    ''' Select nodes using lasso selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param tweak: Tweak, Only activate when mouse is not over a node (useful for tweak gesture)
    :type tweak: bool
    :param path: Path
    :type path: bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection.
    :type mode: typing.Union[str, int]
    '''

    pass


def select_link_viewer(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       NODE_OT_select: 'select' = None,
                       NODE_OT_link_viewer: 'link_viewer' = None):
    ''' Select node and link it to a viewer node

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param NODE_OT_select: Select, Select the node under the cursor
    :type NODE_OT_select: 'select'
    :param NODE_OT_link_viewer: Link to Viewer Node, Link to viewer node
    :type NODE_OT_link_viewer: 'link_viewer'
    '''

    pass


def select_linked_from(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Select nodes linked from the selected ones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_linked_to(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Select nodes linked to the selected ones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_same_type_step(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          prev: bool = False):
    ''' Activate and view same node type, step by step

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param prev: Previous
    :type prev: bool
    '''

    pass


def shader_script_update(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None):
    ''' Update shader script node with new sockets and options from the script

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def switch_view_update(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Update views of selected node

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def translate_attach(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None,
        NODE_OT_attach: 'attach' = None,
        NODE_OT_insert_offset: 'insert_offset' = None):
    ''' Move nodes and attach to frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame
    :type NODE_OT_attach: 'attach'
    :param NODE_OT_insert_offset: Insert Offset, Automatically offset nodes on insertion
    :type NODE_OT_insert_offset: 'insert_offset'
    '''

    pass


def translate_attach_remove_on_cancel(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        TRANSFORM_OT_translate: 'bpy.ops.transform.translate' = None,
        NODE_OT_attach: 'attach' = None,
        NODE_OT_insert_offset: 'insert_offset' = None):
    ''' Move nodes and attach to frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: 'bpy.ops.transform.translate'
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame
    :type NODE_OT_attach: 'attach'
    :param NODE_OT_insert_offset: Insert Offset, Automatically offset nodes on insertion
    :type NODE_OT_insert_offset: 'insert_offset'
    '''

    pass


def tree_path_parent(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Go to parent node tree :file: startup/bl_operators/node.py\:298 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/node.py$298> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def tree_socket_add(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    in_out: typing.Union[int, str] = 'IN'):
    ''' Add an input or output socket to the current node tree

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param in_out: Socket Type
    :type in_out: typing.Union[int, str]
    '''

    pass


def tree_socket_change_type(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None,
                            *,
                            in_out: typing.Union[int, str] = 'IN',
                            socket_type: typing.Union[str, int] = 'DEFAULT'):
    ''' Change the type of a socket of the current node tree

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param in_out: Socket Type
    :type in_out: typing.Union[int, str]
    :param socket_type: Socket Type
    :type socket_type: typing.Union[str, int]
    '''

    pass


def tree_socket_move(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     direction: typing.Union[str, int] = 'UP',
                     in_out: typing.Union[int, str] = 'IN'):
    ''' Move a socket up or down in the current node tree's sockets stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param direction: Direction
    :type direction: typing.Union[str, int]
    :param in_out: Socket Type
    :type in_out: typing.Union[int, str]
    '''

    pass


def tree_socket_remove(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       in_out: typing.Union[int, str] = 'IN'):
    ''' Remove an input or output socket to the current node tree

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param in_out: Socket Type
    :type in_out: typing.Union[int, str]
    '''

    pass


def view_all(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None):
    ''' Resize view so you can see all nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_selected(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Resize view so you can see selected nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def viewer_border(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  xmin: int = 0,
                  xmax: int = 0,
                  ymin: int = 0,
                  ymax: int = 0,
                  wait_for_input: bool = True):
    ''' Set the boundaries for viewer operations

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param xmin: X Min
    :type xmin: int
    :param xmax: X Max
    :type xmax: int
    :param ymin: Y Min
    :type ymin: int
    :param ymax: Y Max
    :type ymax: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass
