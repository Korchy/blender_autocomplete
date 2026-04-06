import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bl_operators.node
import bpy.ops.transform
import bpy.stub_internal.rna_enums
import bpy.types

def add_collection(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
) -> None:
    """Add a collection info node to the current node editor

    :param name: Name, Name of the data-block to use by the operator
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    """

def add_color(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    color: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0, 0.0),
    gamma: bool | None = False,
    has_alpha: bool | None = False,
) -> None:
    """Add a color node to the current node editor

    :param color: Color, Source color
    :param gamma: Gamma Corrected, The source color is gamma corrected
    :param has_alpha: Has Alpha, The source color contains an Alpha component
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
        "ASSET_CATALOG",
    ]
    | None = "",
    name: str = "",
    session_uid: int | None = 0,
) -> None:
    """Add a file node to the current node editor

        :param filepath: File Path, Path to file
        :param directory: Directory, Directory of the file
        :param files: Files
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :param filter_blender: Filter .blend files
        :param filter_backup: Filter .blend files
        :param filter_image: Filter image files
        :param filter_movie: Filter movie files
        :param filter_python: Filter Python files
        :param filter_font: Filter font files
        :param filter_sound: Filter sound files
        :param filter_text: Filter text files
        :param filter_archive: Filter archive files
        :param filter_btx: Filter btx files
        :param filter_collada: Filter COLLADA files
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :param relative_path: Relative Path, Select the file relative to the blend file
        :param show_multiview: Enable Multi-View
        :param use_multiview: Use Multi-View
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
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

    ASSET_CATALOG
    Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
        :param name: Name, Name of the data-block to use by the operator
        :param session_uid: Session UID, Session UID of the data-block to use by the operator
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
) -> None:
    """Add a For Each Geometry Element zone that allows executing nodes e.g. for each vertex separately

    :param use_transform: Use Transform, Start transform operator after inserting the node
    :param settings: Settings, Settings to be applied on the newly created node
    :param offset: Offset, Offset of nodes from the cursor when added
    """

def add_group(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
    show_datablock_in_node: bool | None = True,
) -> None:
    """Add an existing node group to the current node editor

    :param name: Name, Name of the data-block to use by the operator
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :param show_datablock_in_node: Show the datablock selector in the node
    """

def add_group_asset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    asset_library_type: bpy.stub_internal.rna_enums.AssetLibraryTypeItems
    | None = "LOCAL",
    asset_library_identifier: str = "",
    relative_asset_identifier: str = "",
) -> None:
    """Add a node group asset to the active node tree

    :param asset_library_type: Asset Library Type
    :param asset_library_identifier: Asset Library Identifier
    :param relative_asset_identifier: Relative Asset Identifier
    """

def add_mask(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
) -> None:
    """Add a mask node to the current node editor

    :param name: Name, Name of the data-block to use by the operator
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    """

def add_material(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
) -> None:
    """Add a material node to the current node editor

    :param name: Name, Name of the data-block to use by the operator
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
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
) -> None:
    """Add a node to the active tree

    :param use_transform: Use Transform, Start transform operator after inserting the node
    :param settings: Settings, Settings to be applied on the newly created node
    :param type: Node Type, Node type
    """

def add_object(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    session_uid: int | None = 0,
) -> None:
    """Add an object info node to the current node editor

    :param name: Name, Name of the data-block to use by the operator
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
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
) -> None:
    """Add a repeat zone that allows executing nodes a dynamic number of times

    :param use_transform: Use Transform, Start transform operator after inserting the node
    :param settings: Settings, Settings to be applied on the newly created node
    :param offset: Offset, Offset of nodes from the cursor when added
    """

def add_reroute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    cursor: int | None = 11,
) -> None:
    """Add a reroute node

    :param path: Path
    :param cursor: Cursor
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
) -> None:
    """Add simulation zone input and output nodes to the active tree

    :param use_transform: Use Transform, Start transform operator after inserting the node
    :param settings: Settings, Settings to be applied on the newly created node
    :param offset: Offset, Offset of nodes from the cursor when added
    """

def attach(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Attach active node to a frame"""

def backimage_fit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Fit the background image to the view"""

def backimage_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move node backdrop"""

def backimage_sample(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Use mouse to sample background image"""

def backimage_zoom(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 1.2,
) -> None:
    """Zoom in/out the background image

    :param factor: Factor
    """

def bake_node_item_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add item below active item"""

def bake_node_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move active item

    :param direction: Direction, Move direction
    """

def bake_node_item_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove active item"""

def capture_attribute_item_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add item below active item"""

def capture_attribute_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move active item

    :param direction: Direction, Move direction
    """

def capture_attribute_item_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove active item"""

def clear_viewer_border(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear the boundaries for viewer operations"""

def clipboard_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the selected nodes to the internal clipboard"""

def clipboard_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: collections.abc.Iterable[float] | None = (0.0, 0.0),
) -> None:
    """Paste nodes from the internal clipboard to the active node tree

    :param offset: Location, The 2D view location for the center of the new nodes, or unchanged if not set
    """

def collapse_hide_unused_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle collapsed nodes and hide unused sockets"""

def connect_to_output(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    run_in_geometry_nodes: bool | None = True,
) -> None:
    """Connect active node to the active output node of the node tree

    :param run_in_geometry_nodes: Run in Geometry Nodes Editor
    """

def cryptomatte_layer_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new input layer to a Cryptomatte node"""

def cryptomatte_layer_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove layer from a Cryptomatte node"""

def deactivate_viewer(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Deactivate selected viewer node in geometry nodes"""

def default_group_width_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set the width based on the parent group node in the current context"""

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove selected nodes"""

def delete_reconnect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove nodes and reconnect nodes as if deletion was muted"""

def detach(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Detach selected nodes from parents"""

def detach_translate_attach(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NODE_OT_detach: detach | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
    NODE_OT_attach: attach | None = None,
) -> None:
    """Detach nodes, move and attach to frame

    :param NODE_OT_detach: Detach Nodes, Detach selected nodes from parents
    :param TRANSFORM_OT_translate: Move, Move selected items
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame
    """

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keep_inputs: bool | None = False,
    linked: bool | None = True,
) -> None:
    """Duplicate selected nodes

    :param keep_inputs: Keep Inputs, Keep the input links to duplicated nodes
    :param linked: Linked, Duplicate node but not node trees, linking to the original data
    """

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NODE_OT_duplicate: duplicate | None = None,
    NODE_OT_translate_attach: translate_attach | None = None,
) -> None:
    """Duplicate selected nodes and move them

    :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    """

def duplicate_move_keep_inputs(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NODE_OT_duplicate: duplicate | None = None,
    NODE_OT_translate_attach: translate_attach | None = None,
) -> None:
    """Duplicate selected nodes keeping input links and move them

    :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    """

def duplicate_move_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NODE_OT_duplicate: duplicate | None = None,
    NODE_OT_translate_attach: translate_attach | None = None,
) -> None:
    """Duplicate selected nodes, but not their node trees, and move them

    :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    """

def enum_definition_item_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add item below active item"""

def enum_definition_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move active item

    :param direction: Direction, Move direction
    """

def enum_definition_item_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove active item"""

def find_node(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Search for a node by name and focus and select it"""

def foreach_geometry_element_zone_generation_item_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add item below active item"""

def foreach_geometry_element_zone_generation_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move active item

    :param direction: Direction, Move direction
    """

def foreach_geometry_element_zone_generation_item_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove active item"""

def foreach_geometry_element_zone_input_item_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add item below active item"""

def foreach_geometry_element_zone_input_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move active item

    :param direction: Direction, Move direction
    """

def foreach_geometry_element_zone_input_item_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove active item"""

def foreach_geometry_element_zone_main_item_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add item below active item"""

def foreach_geometry_element_zone_main_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move active item

    :param direction: Direction, Move direction
    """

def foreach_geometry_element_zone_main_item_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove active item"""

def gltf_settings_node_operator(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a node to the active tree for glTF export"""

def group_edit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    exit: bool | None = False,
) -> None:
    """Edit node group

    :param exit: Exit
    """

def group_insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Insert selected nodes into a node group"""

def group_make(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Make group from selected nodes"""

def group_separate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["COPY", "MOVE"] | None = "COPY",
) -> None:
    """Separate selected nodes from the node group

        :param type: Type

    COPY
    Copy -- Copy to parent node tree, keep group intact.

    MOVE
    Move -- Move to parent node tree, remove from group.
    """

def group_ungroup(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Ungroup selected nodes"""

def hide_socket_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle unused node socket display"""

def hide_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle hiding of selected nodes"""

def index_switch_item_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add bake item"""

def index_switch_item_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Remove an item from the index switch

    :param index: Index, Index to remove
    """

def insert_offset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Automatically offset nodes on insertion"""

def interface_item_duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a copy of the active item to the interface"""

def interface_item_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    item_type: typing.Literal["INPUT", "OUTPUT", "PANEL"] | None = "INPUT",
) -> None:
    """Add a new item to the interface

    :param item_type: Item Type, Type of the item to create
    """

def interface_item_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove active item from the interface"""

def join(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Attach selected nodes to a new common frame"""

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
) -> None:
    """Use the mouse to create a link between two nodes

    :param detach: Detach, Detach and redirect existing links
    :param drag_start: Drag Start, The position of the mouse cursor at the start of the operation
    :param inside_padding: Inside Padding, Inside distance in UI units from the edge of the region within which to start panning
    :param outside_padding: Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning
    :param speed_ramp: Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge
    :param max_speed: Max Speed, Maximum speed in UI units per second
    :param delay: Delay, Delay in seconds before maximum speed is reached
    :param zoom_influence: Zoom Influence, Influence of the zoom factor on scroll speed
    """

def link_make(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    replace: bool | None = False,
) -> None:
    """Make a link between selected output and input sockets

    :param replace: Replace, Replace socket connections with the new links
    """

def link_viewer(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Link to viewer node"""

def links_cut(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    cursor: int | None = 15,
) -> None:
    """Use the mouse to cut (remove) some links

    :param path: Path
    :param cursor: Cursor
    """

def links_detach(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove all links to selected nodes, and try to connect neighbor nodes together"""

def links_mute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    cursor: int | None = 38,
) -> None:
    """Use the mouse to mute links

    :param path: Path
    :param cursor: Cursor
    """

def move_detach_links(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NODE_OT_links_detach: links_detach | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Move a node to detach links

    :param NODE_OT_links_detach: Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def move_detach_links_release(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NODE_OT_links_detach: links_detach | None = None,
    NODE_OT_translate_attach: translate_attach | None = None,
) -> None:
    """Move a node to detach links

    :param NODE_OT_links_detach: Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    """

def mute_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle muting of selected nodes"""

def new_geometry_node_group_assign(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create a new geometry node group and assign it to the active modifier"""

def new_geometry_node_group_tool(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create a new geometry node group for a tool"""

def new_geometry_nodes_modifier(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create a new modifier with a new geometry node group"""

def new_node_tree(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "",
    name: str = "NodeTree",
) -> None:
    """Create a new node tree

    :param type: Tree Type
    :param name: Name
    """

def node_color_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add or remove a Node Color Preset

    :param name: Name, Name of the preset, used to make the path name
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

def node_copy_color(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy color to all selected nodes"""

def options_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle option buttons display for selected nodes"""

def output_file_add_socket(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    file_path: str = "Image",
) -> None:
    """Add a new input to a file output node

    :param file_path: File Path, Subpath of the output file
    """

def output_file_move_active_socket(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "DOWN",
) -> None:
    """Move the active input of a file output node up or down the list

    :param direction: Direction
    """

def output_file_remove_active_socket(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the active input from a file output node"""

def parent_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Attach selected nodes"""

def preview_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle preview display for selected nodes"""

def read_viewlayers(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Read all render layers of all used scenes"""

def render_changed(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Render current scene, when input nodes layer has been changed"""

def repeat_zone_item_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add item below active item"""

def repeat_zone_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move active item

    :param direction: Direction, Move direction
    """

def repeat_zone_item_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove active item"""

def resize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Resize a node"""

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
) -> None:
    """Select the node under the cursor

    :param extend: Extend, Extend selection instead of deselecting everything first
    :param deselect: Deselect, Remove from selection
    :param toggle: Toggle Selection, Toggle the selection
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :param location: Location, Mouse location
    :param socket_select: Socket Select
    :param clear_viewer: Clear Viewer, Deactivate geometry nodes viewer when clicking in empty space
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """(De)select all nodes

        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
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
) -> None:
    """Use box selection to select nodes

        :param tweak: Tweak, Only activate when mouse is not over a node (useful for tweak gesture)
        :param xmin: X Min
        :param xmax: X Max
        :param ymin: Y Min
        :param ymax: Y Max
        :param wait_for_input: Wait for Input
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
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
) -> None:
    """Use circle selection to select nodes

        :param x: X
        :param y: Y
        :param radius: Radius
        :param wait_for_input: Wait for Input
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
    """

def select_grouped(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    type: typing.Literal["TYPE", "COLOR", "PREFIX", "SUFFIX"] | None = "TYPE",
) -> None:
    """Select nodes with similar properties

    :param extend: Extend, Extend selection instead of deselecting everything first
    :param type: Type
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
) -> None:
    """Select nodes using lasso selection

        :param tweak: Tweak, Only activate when mouse is not over a node (useful for tweak gesture)
        :param path: Path
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
    """

def select_link_viewer(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NODE_OT_select: select | None = None,
    NODE_OT_link_viewer: link_viewer | None = None,
) -> None:
    """Select node and link it to a viewer node

    :param NODE_OT_select: Select, Select the node under the cursor
    :param NODE_OT_link_viewer: Link to Viewer Node, Link to viewer node
    """

def select_linked_from(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select nodes linked from the selected ones"""

def select_linked_to(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select nodes linked to the selected ones"""

def select_same_type_step(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    prev: bool | None = False,
) -> None:
    """Activate and view same node type, step by step

    :param prev: Previous
    """

def shader_script_update(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Update shader script node with new sockets and options from the script"""

def simulation_zone_item_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add item below active item"""

def simulation_zone_item_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move active item

    :param direction: Direction, Move direction
    """

def simulation_zone_item_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove active item"""

def translate_attach(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
    NODE_OT_attach: attach | None = None,
) -> None:
    """Move nodes and attach to frame

    :param TRANSFORM_OT_translate: Move, Move selected items
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame
    """

def translate_attach_remove_on_cancel(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
    NODE_OT_attach: attach | None = None,
) -> None:
    """Move nodes and attach to frame

    :param TRANSFORM_OT_translate: Move, Move selected items
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame
    """

def tree_path_parent(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Go to parent node tree"""

def view_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Resize view so you can see all nodes"""

def view_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Resize view so you can see selected nodes"""

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
) -> None:
    """Set the boundaries for viewer operations

    :param xmin: X Min
    :param xmax: X Max
    :param ymin: Y Min
    :param ymax: Y Max
    :param wait_for_input: Wait for Input
    """

def viewer_shortcut_get(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    viewer_index: int | None = 0,
) -> None:
    """Activate a specific compositor viewer node using 1,2,..,9 keys

    :param viewer_index: Viewer Index, Index corresponding to the shortcut, e.g. number key 1 corresponds to index 1 etc..
    """

def viewer_shortcut_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    viewer_index: int | None = 0,
) -> None:
    """Create a compositor viewer shortcut for the selected node by pressing ctrl+1,2,..9

    :param viewer_index: Viewer Index, Index corresponding to the shortcut, e.g. number key 1 corresponds to index 1 etc..
    """
