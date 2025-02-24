import typing
import collections.abc
import typing_extensions
import bpy._typing.rna_enums

def action_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: str | None = "",
):
    """Change the active action used

    :type execution_context: int | str | None
    :type undo: bool | None
    :param action: Action
    :type action: str | None
    """

def animdata_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "CLEAR_ANIMDATA", "SET_ACT", "CLEAR_ACT", "REFRESH_DRIVERS", "CLEAR_DRIVERS"
    ]
    | None = "CLEAR_ANIMDATA",
):
    """Undocumented, consider contributing.

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Animation Operation

    CLEAR_ANIMDATA
    Clear Animation Data -- Remove this animation data container.

    SET_ACT
    Set Action.

    CLEAR_ACT
    Unlink Action.

    REFRESH_DRIVERS
    Refresh Drivers.

    CLEAR_DRIVERS
    Clear Drivers.
        :type type: typing.Literal['CLEAR_ANIMDATA','SET_ACT','CLEAR_ACT','REFRESH_DRIVERS','CLEAR_DRIVERS'] | None
    """

def clear_filter(execution_context: int | str | None = None, undo: bool | None = None):
    """Clear the search filter

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_color_tag_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    color: bpy._typing.rna_enums.CollectionColorItems | None = "NONE",
):
    """Set a color tag for the selected collections

    :type execution_context: int | str | None
    :type undo: bool | None
    :param color: Color Tag
    :type color: bpy._typing.rna_enums.CollectionColorItems | None
    """

def collection_disable(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Disable viewport display in the view layers

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_disable_render(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Do not render this collection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_drop(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Drag to move to collection in Outliner

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_duplicate(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Recursively duplicate the collection, all its children, objects and object data

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_duplicate_linked(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Recursively duplicate the collection, all its children and objects, with linked object data

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_enable(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Enable viewport display in the view layers

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_enable_render(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Render the collection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_exclude_clear(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Include collection in the active view layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_exclude_set(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Exclude collection from the active view layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_hide(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Hide the collection in this view layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_hide_inside(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Hide all the objects and collections inside the collection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_hierarchy_delete(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Delete selected collection hierarchies

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_holdout_clear(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Clear masking of collection in the active view layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_holdout_set(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Mask collection in the active view layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_indirect_only_clear(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Clear collection contributing only indirectly in the view layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_indirect_only_set(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Set collection to only contribute indirectly (through shadows and reflections) in the view layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_instance(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Instance selected collections to active scene

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_isolate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
):
    """Hide all but this collection and its parents

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend current visible collections
    :type extend: bool | None
    """

def collection_link(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Link selected collections to active scene

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    nested: bool | None = True,
):
    """Add a new collection inside selected collection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param nested: Nested, Add as child of selected collection
    :type nested: bool | None
    """

def collection_objects_deselect(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Deselect objects in collection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_objects_select(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Select objects in collection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_show(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Show the collection in this view layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_show_inside(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Show all the objects and collections inside the collection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def constraint_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["ENABLE", "DISABLE", "DELETE"] | None = "ENABLE",
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Constraint Operation
    :type type: typing.Literal['ENABLE','DISABLE','DELETE'] | None
    """

def data_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "DEFAULT",
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Data Operation
    :type type: str | None
    """

def datastack_drop(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Copy or reorder modifiers, constraints, and effects

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    hierarchy: bool | None = False,
):
    """Delete selected objects and collections

    :type execution_context: int | str | None
    :type undo: bool | None
    :param hierarchy: Hierarchy, Delete child objects and collections
    :type hierarchy: bool | None
    """

def drivers_add_selected(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add drivers to selected items

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def drivers_delete_selected(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Delete drivers assigned to selected items

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def expanded_toggle(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Expand/Collapse all items

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def hide(execution_context: int | str | None = None, undo: bool | None = None):
    """Hide selected objects and collections

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def highlight_update(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Update the item highlight based on the current mouse position

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def id_copy(execution_context: int | str | None = None, undo: bool | None = None):
    """Copy the selected data-blocks to the internal clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def id_delete(execution_context: int | str | None = None, undo: bool | None = None):
    """Delete the ID under cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def id_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "UNLINK",
        "LOCAL",
        "SINGLE",
        "DELETE",
        "REMAP",
        "COPY",
        "PASTE",
        "ADD_FAKE",
        "CLEAR_FAKE",
        "RENAME",
        "SELECT_LINKED",
    ]
    | None = "UNLINK",
):
    """General data-block management operations

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: ID Data Operation

    UNLINK
    Unlink.

    LOCAL
    Make Local.

    SINGLE
    Make Single User.

    DELETE
    Delete.

    REMAP
    Remap Users -- Make all users of selected data-blocks to use instead current (clicked) one.

    COPY
    Copy.

    PASTE
    Paste.

    ADD_FAKE
    Add Fake User -- Ensure data-block gets saved even if it isn't in use (e.g. for motion and material libraries).

    CLEAR_FAKE
    Clear Fake User.

    RENAME
    Rename.

    SELECT_LINKED
    Select Linked.
        :type type: typing.Literal['UNLINK','LOCAL','SINGLE','DELETE','REMAP','COPY','PASTE','ADD_FAKE','CLEAR_FAKE','RENAME','SELECT_LINKED'] | None
    """

def id_paste(execution_context: int | str | None = None, undo: bool | None = None):
    """Paste data-blocks from the internal clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def id_remap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    id_type: bpy._typing.rna_enums.IdTypeItems | None = "OBJECT",
    old_id: str | None = "",
    new_id: str | None = "",
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param id_type: ID Type
    :type id_type: bpy._typing.rna_enums.IdTypeItems | None
    :param old_id: Old ID, Old ID to replace
    :type old_id: str | None
    :param new_id: New ID, New ID to remap all selected IDs' users to
    :type new_id: str | None
    """

def item_activate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    extend_range: bool | None = False,
    deselect_all: bool | None = False,
    recurse: bool | None = False,
):
    """Handle mouse clicks to select and activate items

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection for activation
    :type extend: bool | None
    :param extend_range: Extend Range, Select a range from active element
    :type extend_range: bool | None
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool | None
    :param recurse: Recurse, Select objects recursively from active element
    :type recurse: bool | None
    """

def item_drag_drop(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Drag and drop element to another place

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def item_openclose(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
):
    """Toggle whether item under cursor is enabled or closed

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Close or open all items
    :type all: bool | None
    """

def item_rename(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_active: bool | None = False,
):
    """Rename the active element

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_active: Use Active, Rename the active item, rather than the one the mouse is over
    :type use_active: bool | None
    """

def keyingset_add_selected(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add selected items (blue-gray rows) to active Keying Set

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def keyingset_remove_selected(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove selected items (blue-gray rows) from active Keying Set

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def lib_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["DELETE", "RELOCATE", "RELOAD"] | None = "DELETE",
):
    """Undocumented, consider contributing.

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Library Operation

    DELETE
    Delete -- Delete this library and all its items.

    RELOCATE
    Relocate -- Select a new path for this library, and reload all its data.

    RELOAD
    Reload -- Reload all data from this library.
        :type type: typing.Literal['DELETE','RELOCATE','RELOAD'] | None
    """

def lib_relocate(execution_context: int | str | None = None, undo: bool | None = None):
    """Relocate the library under cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def liboverride_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "OVERRIDE_LIBRARY_CREATE_HIERARCHY",
        "OVERRIDE_LIBRARY_RESET",
        "OVERRIDE_LIBRARY_CLEAR_SINGLE",
    ]
    | None = "OVERRIDE_LIBRARY_CREATE_HIERARCHY",
    selection_set: typing.Literal["SELECTED", "CONTENT", "SELECTED_AND_CONTENT"]
    | None = "SELECTED",
):
    """Create, reset or clear library override hierarchies

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Library Override Operation

    OVERRIDE_LIBRARY_CREATE_HIERARCHY
    Make -- Create a local override of the selected linked data-blocks, and their hierarchy of dependencies.

    OVERRIDE_LIBRARY_RESET
    Reset -- Reset the selected local overrides to their linked references values.

    OVERRIDE_LIBRARY_CLEAR_SINGLE
    Clear -- Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable.
        :type type: typing.Literal['OVERRIDE_LIBRARY_CREATE_HIERARCHY','OVERRIDE_LIBRARY_RESET','OVERRIDE_LIBRARY_CLEAR_SINGLE'] | None
        :param selection_set: Selection Set, Over which part of the tree items to apply the operation

    SELECTED
    Selected -- Apply the operation over selected data-blocks only.

    CONTENT
    Content -- Apply the operation over content of the selected items only (the data-blocks in their sub-tree).

    SELECTED_AND_CONTENT
    Selected & Content -- Apply the operation over selected data-blocks and all their dependencies.
        :type selection_set: typing.Literal['SELECTED','CONTENT','SELECTED_AND_CONTENT'] | None
    """

def liboverride_troubleshoot_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "OVERRIDE_LIBRARY_RESYNC_HIERARCHY",
        "OVERRIDE_LIBRARY_RESYNC_HIERARCHY_ENFORCE",
        "OVERRIDE_LIBRARY_DELETE_HIERARCHY",
    ]
    | None = "OVERRIDE_LIBRARY_RESYNC_HIERARCHY",
    selection_set: typing.Literal["SELECTED", "CONTENT", "SELECTED_AND_CONTENT"]
    | None = "SELECTED",
):
    """Advanced operations over library override to help fix broken hierarchies

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Library Override Troubleshoot Operation

    OVERRIDE_LIBRARY_RESYNC_HIERARCHY
    Resync -- Rebuild the selected local overrides from their linked references, as well as their hierarchies of dependencies.

    OVERRIDE_LIBRARY_RESYNC_HIERARCHY_ENFORCE
    Resync Enforce -- Rebuild the selected local overrides from their linked references, as well as their hierarchies of dependencies, enforcing these hierarchies to match the linked data (i.e. ignoring existing overrides on data-blocks pointer properties).

    OVERRIDE_LIBRARY_DELETE_HIERARCHY
    Delete -- Delete the selected local overrides (including their hierarchies of override dependencies) and relink their usages to the linked data-blocks.
        :type type: typing.Literal['OVERRIDE_LIBRARY_RESYNC_HIERARCHY','OVERRIDE_LIBRARY_RESYNC_HIERARCHY_ENFORCE','OVERRIDE_LIBRARY_DELETE_HIERARCHY'] | None
        :param selection_set: Selection Set, Over which part of the tree items to apply the operation

    SELECTED
    Selected -- Apply the operation over selected data-blocks only.

    CONTENT
    Content -- Apply the operation over content of the selected items only (the data-blocks in their sub-tree).

    SELECTED_AND_CONTENT
    Selected & Content -- Apply the operation over selected data-blocks and all their dependencies.
        :type selection_set: typing.Literal['SELECTED','CONTENT','SELECTED_AND_CONTENT'] | None
    """

def material_drop(execution_context: int | str | None = None, undo: bool | None = None):
    """Drag material to object in Outliner

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def modifier_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["APPLY", "DELETE", "TOGVIS", "TOGREN"] | None = "APPLY",
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Modifier Operation
    :type type: typing.Literal['APPLY','DELETE','TOGVIS','TOGREN'] | None
    """

def object_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["SELECT", "DESELECT", "SELECT_HIERARCHY", "REMAP", "RENAME"]
    | None = "SELECT",
):
    """Undocumented, consider contributing.

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Object Operation

    SELECT
    Select.

    DESELECT
    Deselect.

    SELECT_HIERARCHY
    Select Hierarchy.

    REMAP
    Remap Users -- Make all users of selected data-blocks to use instead a new chosen one.

    RENAME
    Rename.
        :type type: typing.Literal['SELECT','DESELECT','SELECT_HIERARCHY','REMAP','RENAME'] | None
    """

def operation(execution_context: int | str | None = None, undo: bool | None = None):
    """Context menu for item operations

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def orphans_manage(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Open a window to manage unused data

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def orphans_purge(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    do_local_ids: bool | None = True,
    do_linked_ids: bool | None = True,
    do_recursive: bool | None = True,
):
    """Clear all orphaned data-blocks without any users from the file

    :type execution_context: int | str | None
    :type undo: bool | None
    :param do_local_ids: Local Data-blocks, Include unused local data-blocks into deletion
    :type do_local_ids: bool | None
    :param do_linked_ids: Linked Data-blocks, Include unused linked data-blocks into deletion
    :type do_linked_ids: bool | None
    :param do_recursive: Recursive Delete, Recursively check for indirectly unused data-blocks, ensuring that no orphaned data-blocks remain after execution
    :type do_recursive: bool | None
    """

def parent_clear(execution_context: int | str | None = None, undo: bool | None = None):
    """Drag to clear parent in Outliner

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def parent_drop(execution_context: int | str | None = None, undo: bool | None = None):
    """Drag to parent in Outliner

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def scene_drop(execution_context: int | str | None = None, undo: bool | None = None):
    """Drag object to scene in Outliner

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def scene_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["DELETE"] | None = "DELETE",
):
    """Context menu for scene operations

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Scene Operation
    :type type: typing.Literal['DELETE'] | None
    """

def scroll_page(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    up: bool | None = False,
):
    """Scroll page up or down

    :type execution_context: int | str | None
    :type undo: bool | None
    :param up: Up, Scroll up one page
    :type up: bool | None
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Toggle the Outliner selection of items

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
    """Use box selection to select tree elements

        :type execution_context: int | str | None
        :type undo: bool | None
        :param tweak: Tweak, Tweak gesture from empty space for box selection
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

def select_walk(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN", "LEFT", "RIGHT"] | None = "UP",
    extend: bool | None = False,
    toggle_all: bool | None = False,
):
    """Use walk navigation to select tree elements

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Walk Direction, Select/Deselect element in this direction
    :type direction: typing.Literal['UP','DOWN','LEFT','RIGHT'] | None
    :param extend: Extend, Extend selection on walk
    :type extend: bool | None
    :param toggle_all: Toggle All, Toggle open/close hierarchy
    :type toggle_all: bool | None
    """

def show_active(execution_context: int | str | None = None, undo: bool | None = None):
    """Open up the tree and adjust the view so that the active object is shown centered

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def show_hierarchy(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Open all object entries and close all others

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def show_one_level(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    open: bool | None = True,
):
    """Expand/collapse all entries by one level

    :type execution_context: int | str | None
    :type undo: bool | None
    :param open: Open, Expand all entries one level deep
    :type open: bool | None
    """

def start_filter(execution_context: int | str | None = None, undo: bool | None = None):
    """Start entering filter text

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def unhide_all(execution_context: int | str | None = None, undo: bool | None = None):
    """Unhide all objects and collections

    :type execution_context: int | str | None
    :type undo: bool | None
    """
