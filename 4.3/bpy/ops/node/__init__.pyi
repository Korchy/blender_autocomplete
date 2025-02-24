import typing
import collections.abc
import typing_extensions
import bl_operators.node
import bpy._typing.rna_enums
import bpy.ops.transform
import bpy.types

def add_collection(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
):
    """Add a collection info node to the current node editor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :type session_uid: int | None
    """

def add_file(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = True,
    filter_movie: bool | None = True,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_collada: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    relative_path: bool | None = True,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: typing.Literal[
        "DEFAULT",
        "FILE_SORT_ALPHA",
        "FILE_SORT_EXTENSION",
        "FILE_SORT_TIME",
        "FILE_SORT_SIZE",
    ]
    | None = "",
    name: str = "",
    session_uid: int | None = 0,
):
    """Add a file node to the current node editor

        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | None
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode

    DEFAULT
    Default -- Automatically determine sort method for files.

    FILE_SORT_ALPHA
    Name -- Sort the file list alphabetically.

    FILE_SORT_EXTENSION
    Extension -- Sort the file list by extension/type.

    FILE_SORT_TIME
    Modified Date -- Sort files by modification time.

    FILE_SORT_SIZE
    Size -- Sort files by size.
        :type sort_method: typing.Literal['DEFAULT','FILE_SORT_ALPHA','FILE_SORT_EXTENSION','FILE_SORT_TIME','FILE_SORT_SIZE'] | None
        :param name: Name, Name of the data-block to use by the operator
        :type name: str
        :param session_uid: Session UID, Session UID of the data-block to use by the operator
        :type session_uid: int | None
    """

def add_foreach_geometry_element_zone(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_transform: bool | None = False,
    settings: bpy.types.bpy_prop_collection[bl_operators.node.NodeSetting]
    | None = None,
    offset: collections.abc.Iterable[float] | None = (150.0, 0.0),
):
    """Add a For Each Geometry Element zone that allows executing nodes e.g. for each vertex separately

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_transform: Use Transform, Start transform operator after inserting the node
    :type use_transform: bool | None
    :param settings: Settings, Settings to be applied on the newly created node
    :type settings: bpy.types.bpy_prop_collection[bl_operators.node.NodeSetting] | None
    :param offset: Offset, Offset of nodes from the cursor when added
    :type offset: collections.abc.Iterable[float] | None
    """

def add_group(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
    show_datablock_in_node: bool | None = True,
):
    """Add an existing node group to the current node editor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :type session_uid: int | None
    :param show_datablock_in_node: Show the datablock selector in the node
    :type show_datablock_in_node: bool | None
    """

def add_group_asset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    asset_library_type: bpy._typing.rna_enums.AssetLibraryTypeItems | None = "LOCAL",
    asset_library_identifier: str = "",
    relative_asset_identifier: str = "",
):
    """Add a node group asset to the active node tree

    :type execution_context: int | str | None
    :type undo: bool | None
    :param asset_library_type: Asset Library Type
    :type asset_library_type: bpy._typing.rna_enums.AssetLibraryTypeItems | None
    :param asset_library_identifier: Asset Library Identifier
    :type asset_library_identifier: str
    :param relative_asset_identifier: Relative Asset Identifier
    :type relative_asset_identifier: str
    """

def add_mask(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
):
    """Add a mask node to the current node editor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :type session_uid: int | None
    """

def add_material(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
):
    """Add a material node to the current node editor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :type session_uid: int | None
    """

def add_node(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_transform: bool | None = False,
    settings: bpy.types.bpy_prop_collection[bl_operators.node.NodeSetting]
    | None = None,
    type: str = "",
):
    """Add a node to the active tree

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_transform: Use Transform, Start transform operator after inserting the node
    :type use_transform: bool | None
    :param settings: Settings, Settings to be applied on the newly created node
    :type settings: bpy.types.bpy_prop_collection[bl_operators.node.NodeSetting] | None
    :param type: Node Type, Node type
    :type type: str
    """

def add_object(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
):
    """Add an object info node to the current node editor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :type session_uid: int | None
    """

def add_repeat_zone(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_transform: bool | None = False,
    settings: bpy.types.bpy_prop_collection[bl_operators.node.NodeSetting]
    | None = None,
    offset: collections.abc.Iterable[float] | None = (150.0, 0.0),
):
    """Add a repeat zone that allows executing nodes a dynamic number of times

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_transform: Use Transform, Start transform operator after inserting the node
    :type use_transform: bool | None
    :param settings: Settings, Settings to be applied on the newly created node
    :type settings: bpy.types.bpy_prop_collection[bl_operators.node.NodeSetting] | None
    :param offset: Offset, Offset of nodes from the cursor when added
    :type offset: collections.abc.Iterable[float] | None
    """

def add_reroute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    cursor: int | None = 11,
):
    """Add a reroute node

    :type execution_context: int | str | None
    :type undo: bool | None
    :param path: Path
    :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
    :param cursor: Cursor
    :type cursor: int | None
    """

def add_simulation_zone(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_transform: bool | None = False,
    settings: bpy.types.bpy_prop_collection[bl_operators.node.NodeSetting]
    | None = None,
    offset: collections.abc.Iterable[float] | None = (150.0, 0.0),
):
    """Add simulation zone input and output nodes to the active tree

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_transform: Use Transform, Start transform operator after inserting the node
    :type use_transform: bool | None
    :param settings: Settings, Settings to be applied on the newly created node
    :type settings: bpy.types.bpy_prop_collection[bl_operators.node.NodeSetting] | None
    :param offset: Offset, Offset of nodes from the cursor when added
    :type offset: collections.abc.Iterable[float] | None
    """

def attach(execution_context: int | str | None = None, undo: bool | None = None):
    """Attach active node to a frame

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def backimage_fit(execution_context: int | str | None = None, undo: bool | None = None):
    """Fit the background image to the view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def backimage_move(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Move node backdrop

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def backimage_sample(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Use mouse to sample background image

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def backimage_zoom(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 1.2,
):
    """Zoom in/out the background image

    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor
    :type factor: float | None
    """

def bake_node_item_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add bake item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def bake_node_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move active bake item

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Move direction
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def bake_node_item_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove active bake item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def capture_attribute_item_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add capture attribute item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def capture_attribute_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move active capture attribute item

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Move direction
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def capture_attribute_item_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove active capture attribute item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def clear_viewer_border(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Clear the boundaries for viewer operations

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def clipboard_copy(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Copy the selected nodes to the internal clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def clipboard_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: collections.abc.Iterable[float] | None = (0.0, 0.0),
):
    """Paste nodes from the internal clipboard to the active node tree

    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Location, The 2D view location for the center of the new nodes, or unchanged if not set
    :type offset: collections.abc.Iterable[float] | None
    """

def collapse_hide_unused_toggle(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Toggle collapsed nodes and hide unused sockets

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def connect_to_output(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    run_in_geometry_nodes: bool | None = True,
):
    """Connect active node to the active output node of the node tree

    :type execution_context: int | str | None
    :type undo: bool | None
    :param run_in_geometry_nodes: Run in Geometry Nodes Editor
    :type run_in_geometry_nodes: bool | None
    """

def cryptomatte_layer_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add a new input layer to a Cryptomatte node

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def cryptomatte_layer_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove layer from a Cryptomatte node

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def deactivate_viewer(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Deactivate selected viewer node in geometry nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def default_group_width_set(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Set the width based on the parent group node in the current context

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def delete(execution_context: int | str | None = None, undo: bool | None = None):
    """Remove selected nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def delete_reconnect(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove nodes and reconnect nodes as if deletion was muted

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def detach(execution_context: int | str | None = None, undo: bool | None = None):
    """Detach selected nodes from parents

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def detach_translate_attach(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NODE_OT_detach: detach | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
    NODE_OT_attach: attach | None = None,
):
    """Detach nodes, move and attach to frame

    :type execution_context: int | str | None
    :type undo: bool | None
    :param NODE_OT_detach: Detach Nodes, Detach selected nodes from parents
    :type NODE_OT_detach: detach | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame
    :type NODE_OT_attach: attach | None
    """

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keep_inputs: bool | None = False,
    linked: bool | None = True,
):
    """Duplicate selected nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param keep_inputs: Keep Inputs, Keep the input links to duplicated nodes
    :type keep_inputs: bool | None
    :param linked: Linked, Duplicate node but not node trees, linking to the original data
    :type linked: bool | None
    """

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NODE_OT_duplicate: duplicate | None = None,
    NODE_OT_translate_attach: translate_attach | None = None,
):
    """Duplicate selected nodes and move them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes
    :type NODE_OT_duplicate: duplicate | None
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    :type NODE_OT_translate_attach: translate_attach | None
    """

def duplicate_move_keep_inputs(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NODE_OT_duplicate: duplicate | None = None,
    NODE_OT_translate_attach: translate_attach | None = None,
):
    """Duplicate selected nodes keeping input links and move them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes
    :type NODE_OT_duplicate: duplicate | None
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    :type NODE_OT_translate_attach: translate_attach | None
    """

def duplicate_move_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NODE_OT_duplicate: duplicate | None = None,
    NODE_OT_translate_attach: translate_attach | None = None,
):
    """Duplicate selected nodes, but not their node trees, and move them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes
    :type NODE_OT_duplicate: duplicate | None
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    :type NODE_OT_translate_attach: translate_attach | None
    """

def enum_definition_item_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add menu item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def enum_definition_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move active menu item

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Move direction
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def enum_definition_item_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove active menu item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def find_node(execution_context: int | str | None = None, undo: bool | None = None):
    """Search for a node by name and focus and select it

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def foreach_geometry_element_zone_generation_item_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add for-each generation item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def foreach_geometry_element_zone_generation_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move active for-each generation item

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Move direction
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def foreach_geometry_element_zone_generation_item_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove active for-each generation item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def foreach_geometry_element_zone_input_item_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add for-each input item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def foreach_geometry_element_zone_input_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move active for-each input item

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Move direction
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def foreach_geometry_element_zone_input_item_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove active for-each input item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def foreach_geometry_element_zone_main_item_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add for-each main item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def foreach_geometry_element_zone_main_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move active for-each main item

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Move direction
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def foreach_geometry_element_zone_main_item_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove active for-each main item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def gltf_settings_node_operator(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add a node to the active tree for glTF export

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def group_edit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    exit: bool | None = False,
):
    """Edit node group

    :type execution_context: int | str | None
    :type undo: bool | None
    :param exit: Exit
    :type exit: bool | None
    """

def group_insert(execution_context: int | str | None = None, undo: bool | None = None):
    """Insert selected nodes into a node group

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def group_make(execution_context: int | str | None = None, undo: bool | None = None):
    """Make group from selected nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def group_separate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["COPY", "MOVE"] | None = "COPY",
):
    """Separate selected nodes from the node group

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    COPY
    Copy -- Copy to parent node tree, keep group intact.

    MOVE
    Move -- Move to parent node tree, remove from group.
        :type type: typing.Literal['COPY','MOVE'] | None
    """

def group_ungroup(execution_context: int | str | None = None, undo: bool | None = None):
    """Ungroup selected nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def hide_socket_toggle(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Toggle unused node socket display

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def hide_toggle(execution_context: int | str | None = None, undo: bool | None = None):
    """Toggle hiding of selected nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def index_switch_item_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add bake item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def index_switch_item_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
):
    """Remove an item from the index switch

    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index, Index to remove
    :type index: int | None
    """

def insert_offset(execution_context: int | str | None = None, undo: bool | None = None):
    """Automatically offset nodes on insertion

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def interface_item_duplicate(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add a copy of the active item to the interface

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def interface_item_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    item_type: typing.Literal["INPUT", "OUTPUT", "PANEL"] | None = "INPUT",
):
    """Add a new item to the interface

    :type execution_context: int | str | None
    :type undo: bool | None
    :param item_type: Item Type, Type of the item to create
    :type item_type: typing.Literal['INPUT','OUTPUT','PANEL'] | None
    """

def interface_item_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove active item from the interface

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def join(execution_context: int | str | None = None, undo: bool | None = None):
    """Attach selected nodes to a new common frame

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def link(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    detach: bool | None = False,
    drag_start: collections.abc.Iterable[float] | None = (0.0, 0.0),
    inside_padding: float | None = 2.0,
    outside_padding: float | None = 0.0,
    speed_ramp: float | None = 1.0,
    max_speed: float | None = 26.0,
    delay: float | None = 0.5,
    zoom_influence: float | None = 0.5,
):
    """Use the mouse to create a link between two nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param detach: Detach, Detach and redirect existing links
    :type detach: bool | None
    :param drag_start: Drag Start, The position of the mouse cursor at the start of the operation
    :type drag_start: collections.abc.Iterable[float] | None
    :param inside_padding: Inside Padding, Inside distance in UI units from the edge of the region within which to start panning
    :type inside_padding: float | None
    :param outside_padding: Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning
    :type outside_padding: float | None
    :param speed_ramp: Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge
    :type speed_ramp: float | None
    :param max_speed: Max Speed, Maximum speed in UI units per second
    :type max_speed: float | None
    :param delay: Delay, Delay in seconds before maximum speed is reached
    :type delay: float | None
    :param zoom_influence: Zoom Influence, Influence of the zoom factor on scroll speed
    :type zoom_influence: float | None
    """

def link_make(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    replace: bool | None = False,
):
    """Make a link between selected output and input sockets

    :type execution_context: int | str | None
    :type undo: bool | None
    :param replace: Replace, Replace socket connections with the new links
    :type replace: bool | None
    """

def link_viewer(execution_context: int | str | None = None, undo: bool | None = None):
    """Link to viewer node

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def links_cut(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    cursor: int | None = 15,
):
    """Use the mouse to cut (remove) some links

    :type execution_context: int | str | None
    :type undo: bool | None
    :param path: Path
    :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
    :param cursor: Cursor
    :type cursor: int | None
    """

def links_detach(execution_context: int | str | None = None, undo: bool | None = None):
    """Remove all links to selected nodes, and try to connect neighbor nodes together

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def links_mute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    cursor: int | None = 38,
):
    """Use the mouse to mute links

    :type execution_context: int | str | None
    :type undo: bool | None
    :param path: Path
    :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
    :param cursor: Cursor
    :type cursor: int | None
    """

def move_detach_links(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NODE_OT_links_detach: links_detach | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Move a node to detach links

    :type execution_context: int | str | None
    :type undo: bool | None
    :param NODE_OT_links_detach: Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together
    :type NODE_OT_links_detach: links_detach | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def move_detach_links_release(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NODE_OT_links_detach: links_detach | None = None,
    NODE_OT_translate_attach: translate_attach | None = None,
):
    """Move a node to detach links

    :type execution_context: int | str | None
    :type undo: bool | None
    :param NODE_OT_links_detach: Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together
    :type NODE_OT_links_detach: links_detach | None
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    :type NODE_OT_translate_attach: translate_attach | None
    """

def mute_toggle(execution_context: int | str | None = None, undo: bool | None = None):
    """Toggle muting of selected nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def new_geometry_node_group_assign(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create a new geometry node group and assign it to the active modifier

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def new_geometry_node_group_tool(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create a new geometry node group for a tool

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def new_geometry_nodes_modifier(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create a new modifier with a new geometry node group

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def new_node_tree(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "",
    name: str = "NodeTree",
):
    """Create a new node tree

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Tree Type
    :type type: str | None
    :param name: Name
    :type name: str
    """

def node_color_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
):
    """Add or remove a Node Color Preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def node_copy_color(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Copy color to all selected nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def options_toggle(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Toggle option buttons display for selected nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def output_file_add_socket(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    file_path: str = "Image",
):
    """Add a new input to a file output node

    :type execution_context: int | str | None
    :type undo: bool | None
    :param file_path: File Path, Subpath of the output file
    :type file_path: str
    """

def output_file_move_active_socket(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "DOWN",
):
    """Move the active input of a file output node up or down the list

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def output_file_remove_active_socket(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove the active input from a file output node

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def parent_set(execution_context: int | str | None = None, undo: bool | None = None):
    """Attach selected nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def preview_toggle(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Toggle preview display for selected nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def read_viewlayers(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Read all render layers of all used scenes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def render_changed(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Render current scene, when input node's layer has been changed

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def repeat_zone_item_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add repeat zone item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def repeat_zone_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move active repeat zone item

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Move direction
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def repeat_zone_item_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove active repeat zone item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def resize(execution_context: int | str | None = None, undo: bool | None = None):
    """Resize a node

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
    deselect_all: bool | None = False,
    select_passthrough: bool | None = False,
    location: collections.abc.Iterable[int] | None = (0, 0),
    socket_select: bool | None = False,
    clear_viewer: bool | None = False,
):
    """Select the node under the cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
    :param deselect: Deselect, Remove from selection
    :type deselect: bool | None
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: bool | None
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool | None
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: bool | None
    :param location: Location, Mouse location
    :type location: collections.abc.Iterable[int] | None
    :param socket_select: Socket Select
    :type socket_select: bool | None
    :param clear_viewer: Clear Viewer, Deactivate geometry nodes viewer when clicking in empty space
    :type clear_viewer: bool | None
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """(De)select all nodes

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
        :type action: typing.Literal['TOGGLE','SELECT','DESELECT','INVERT'] | None
    """

def select_box(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    tweak: bool | None = False,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
):
    """Use box selection to select nodes

        :type execution_context: int | str | None
        :type undo: bool | None
        :param tweak: Tweak, Only activate when mouse is not over a node (useful for tweak gesture)
        :type tweak: bool | None
        :param xmin: X Min
        :type xmin: int | None
        :param xmax: X Max
        :type xmax: int | None
        :param ymin: Y Min
        :type ymin: int | None
        :param ymax: Y Max
        :type ymax: int | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
    """

def select_circle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    x: int | None = 0,
    y: int | None = 0,
    radius: int | None = 25,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
):
    """Use circle selection to select nodes

        :type execution_context: int | str | None
        :type undo: bool | None
        :param x: X
        :type x: int | None
        :param y: Y
        :type y: int | None
        :param radius: Radius
        :type radius: int | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
    """

def select_grouped(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    type: typing.Literal["TYPE", "COLOR", "PREFIX", "SUFFIX"] | None = "TYPE",
):
    """Select nodes with similar properties

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
    :param type: Type
    :type type: typing.Literal['TYPE','COLOR','PREFIX','SUFFIX'] | None
    """

def select_lasso(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    tweak: bool | None = False,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_smooth_stroke: bool | None = False,
    smooth_stroke_factor: float | None = 0.75,
    smooth_stroke_radius: int | None = 35,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
):
    """Select nodes using lasso selection

        :type execution_context: int | str | None
        :type undo: bool | None
        :param tweak: Tweak, Only activate when mouse is not over a node (useful for tweak gesture)
        :type tweak: bool | None
        :param path: Path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
        :type use_smooth_stroke: bool | None
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
        :type smooth_stroke_factor: float | None
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
        :type smooth_stroke_radius: int | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
    """

def select_link_viewer(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NODE_OT_select: select | None = None,
    NODE_OT_link_viewer: link_viewer | None = None,
):
    """Select node and link it to a viewer node

    :type execution_context: int | str | None
    :type undo: bool | None
    :param NODE_OT_select: Select, Select the node under the cursor
    :type NODE_OT_select: select | None
    :param NODE_OT_link_viewer: Link to Viewer Node, Link to viewer node
    :type NODE_OT_link_viewer: link_viewer | None
    """

def select_linked_from(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Select nodes linked from the selected ones

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked_to(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Select nodes linked to the selected ones

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_same_type_step(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    prev: bool | None = False,
):
    """Activate and view same node type, step by step

    :type execution_context: int | str | None
    :type undo: bool | None
    :param prev: Previous
    :type prev: bool | None
    """

def shader_script_update(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Update shader script node with new sockets and options from the script

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def simulation_zone_item_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add simulation zone item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def simulation_zone_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move active simulation zone item

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Move direction
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def simulation_zone_item_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove active simulation zone item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def translate_attach(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
    NODE_OT_attach: attach | None = None,
):
    """Move nodes and attach to frame

    :type execution_context: int | str | None
    :type undo: bool | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame
    :type NODE_OT_attach: attach | None
    """

def translate_attach_remove_on_cancel(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
    NODE_OT_attach: attach | None = None,
):
    """Move nodes and attach to frame

    :type execution_context: int | str | None
    :type undo: bool | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame
    :type NODE_OT_attach: attach | None
    """

def tree_path_parent(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Go to parent node tree

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_all(execution_context: int | str | None = None, undo: bool | None = None):
    """Resize view so you can see all nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_selected(execution_context: int | str | None = None, undo: bool | None = None):
    """Resize view so you can see selected nodes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def viewer_border(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
):
    """Set the boundaries for viewer operations

    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: int | None
    :param xmax: X Max
    :type xmax: int | None
    :param ymin: Y Min
    :type ymin: int | None
    :param ymax: Y Max
    :type ymax: int | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    """
