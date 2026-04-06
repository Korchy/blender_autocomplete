import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums

def action_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: str | None = "",
) -> None:
    """Change the active action used

    :param action: Action
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
) -> None:
    """Undocumented, consider contributing.

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
    """

def clear_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear the search filter"""

def collection_color_tag_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    color: bpy.stub_internal.rna_enums.CollectionColorItems | None = "NONE",
) -> None:
    """Set a color tag for the selected collections

    :param color: Color Tag
    """

def collection_disable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Disable viewport display in the view layers"""

def collection_disable_render(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Do not render this collection"""

def collection_drop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Drag to move to collection in Outliner"""

def collection_duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Recursively duplicate the collection, all its children, objects and object data"""

def collection_duplicate_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Recursively duplicate the collection, all its children and objects, with linked object data"""

def collection_enable(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Enable viewport display in the view layers"""

def collection_enable_render(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Render the collection"""

def collection_exclude_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Include collection in the active view layer"""

def collection_exclude_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Exclude collection from the active view layer"""

def collection_hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Hide the collection in this view layer"""

def collection_hide_inside(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Hide all the objects and collections inside the collection"""

def collection_hierarchy_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete selected collection hierarchies"""

def collection_holdout_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear masking of collection in the active view layer"""

def collection_holdout_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Mask collection in the active view layer"""

def collection_indirect_only_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear collection contributing only indirectly in the view layer"""

def collection_indirect_only_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set collection to only contribute indirectly (through shadows and reflections) in the view layer"""

def collection_instance(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Instance selected collections to active scene"""

def collection_isolate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Hide all but this collection and its parents

    :param extend: Extend, Extend current visible collections
    """

def collection_link(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Link selected collections to active scene"""

def collection_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    nested: bool | None = True,
) -> None:
    """Add a new collection inside selected collection

    :param nested: Nested, Add as child of selected collection
    """

def collection_objects_deselect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Deselect objects in collection"""

def collection_objects_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select objects in collection"""

def collection_show(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Show the collection in this view layer"""

def collection_show_inside(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Show all the objects and collections inside the collection"""

def constraint_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["ENABLE", "DISABLE", "DELETE"] | None = "ENABLE",
) -> None:
    """Undocumented, consider contributing.

    :param type: Constraint Operation
    """

def data_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "DEFAULT",
) -> None:
    """Undocumented, consider contributing.

    :param type: Data Operation
    """

def datastack_drop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy or reorder modifiers, constraints, and effects"""

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    hierarchy: bool | None = False,
) -> None:
    """Delete selected objects and collections

    :param hierarchy: Hierarchy, Delete child objects and collections
    """

def drivers_add_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add drivers to selected items"""

def drivers_delete_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete drivers assigned to selected items"""

def expanded_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Expand/Collapse all items"""

def hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Hide selected objects and collections"""

def highlight_update(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Update the item highlight based on the current mouse position"""

def id_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the selected data-blocks to the internal clipboard"""

def id_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete the ID under cursor"""

def id_linked_relocate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Replace the active linked ID (and its dependencies if any) by another one, from the same or a different library"""

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
) -> None:
    """General data-block management operations

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
    Add Fake User -- Ensure data-block gets saved even if it isnt in use (e.g. for motion and material libraries).

    CLEAR_FAKE
    Clear Fake User.

    RENAME
    Rename.

    SELECT_LINKED
    Select Linked.
    """

def id_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Paste data-blocks from the internal clipboard"""

def id_remap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    id_type: bpy.stub_internal.rna_enums.IdTypeItems | None = "OBJECT",
    old_id: str | None = "",
    new_id: str | None = "",
) -> None:
    """Undocumented, consider contributing.

    :param id_type: ID Type
    :param old_id: Old ID, Old ID to replace
    :param new_id: New ID, New ID to remap all selected IDs users to
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
) -> None:
    """Handle mouse clicks to select and activate items

    :param extend: Extend, Extend selection for activation
    :param extend_range: Extend Range, Select a range from active element
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :param recurse: Recurse, Select objects recursively from active element
    """

def item_drag_drop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Drag and drop element to another place"""

def item_openclose(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
) -> None:
    """Toggle whether item under cursor is enabled or closed

    :param all: All, Close or open all items
    """

def item_rename(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_active: bool | None = False,
) -> None:
    """Rename the active element

    :param use_active: Use Active, Rename the active item, rather than the one the mouse is over
    """

def keyingset_add_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add selected items (blue-gray rows) to active Keying Set"""

def keyingset_remove_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove selected items (blue-gray rows) from active Keying Set"""

def lib_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["DELETE", "RELOCATE", "RELOAD"] | None = "DELETE",
) -> None:
    """Undocumented, consider contributing.

        :param type: Library Operation

    DELETE
    Delete -- Delete this library and all its items.

    RELOCATE
    Relocate -- Select a new path for this library, and reload all its data.

    RELOAD
    Reload -- Reload all data from this library.
    """

def lib_relocate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Relocate the library under cursor"""

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
) -> None:
    """Create, reset or clear library override hierarchies

        :param type: Library Override Operation

    OVERRIDE_LIBRARY_CREATE_HIERARCHY
    Make -- Create a local override of the selected linked data-blocks, and their hierarchy of dependencies.

    OVERRIDE_LIBRARY_RESET
    Reset -- Reset the selected local overrides to their linked references values.

    OVERRIDE_LIBRARY_CLEAR_SINGLE
    Clear -- Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable.
        :param selection_set: Selection Set, Over which part of the tree items to apply the operation

    SELECTED
    Selected -- Apply the operation over selected data-blocks only.

    CONTENT
    Content -- Apply the operation over content of the selected items only (the data-blocks in their sub-tree).

    SELECTED_AND_CONTENT
    Selected & Content -- Apply the operation over selected data-blocks and all their dependencies.
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
) -> None:
    """Advanced operations over library override to help fix broken hierarchies

        :param type: Library Override Troubleshoot Operation

    OVERRIDE_LIBRARY_RESYNC_HIERARCHY
    Resync -- Rebuild the selected local overrides from their linked references, as well as their hierarchies of dependencies.

    OVERRIDE_LIBRARY_RESYNC_HIERARCHY_ENFORCE
    Resync Enforce -- Rebuild the selected local overrides from their linked references, as well as their hierarchies of dependencies, enforcing these hierarchies to match the linked data (i.e. ignoring existing overrides on data-blocks pointer properties).

    OVERRIDE_LIBRARY_DELETE_HIERARCHY
    Delete -- Delete the selected local overrides (including their hierarchies of override dependencies) and relink their usages to the linked data-blocks.
        :param selection_set: Selection Set, Over which part of the tree items to apply the operation

    SELECTED
    Selected -- Apply the operation over selected data-blocks only.

    CONTENT
    Content -- Apply the operation over content of the selected items only (the data-blocks in their sub-tree).

    SELECTED_AND_CONTENT
    Selected & Content -- Apply the operation over selected data-blocks and all their dependencies.
    """

def material_drop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Drag material to object in Outliner"""

def modifier_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["APPLY", "DELETE", "TOGVIS", "TOGREN"] | None = "APPLY",
) -> None:
    """Undocumented, consider contributing.

    :param type: Modifier Operation
    """

def object_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["SELECT", "DESELECT", "SELECT_HIERARCHY", "REMAP", "RENAME"]
    | None = "SELECT",
) -> None:
    """Undocumented, consider contributing.

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
    """

def operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Context menu for item operations"""

def orphans_manage(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Open a window to manage unused data"""

def orphans_purge(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    do_local_ids: bool | None = True,
    do_linked_ids: bool | None = True,
    do_recursive: bool | None = True,
) -> None:
    """Clear all orphaned data-blocks without any users from the file

    :param do_local_ids: Local Data-blocks, Include unused local data-blocks into deletion
    :param do_linked_ids: Linked Data-blocks, Include unused linked data-blocks into deletion
    :param do_recursive: Recursive Delete, Recursively check for indirectly unused data-blocks, ensuring that no orphaned data-blocks remain after execution
    """

def parent_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Drag to clear parent in Outliner"""

def parent_drop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Drag to parent in Outliner"""

def scene_drop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Drag object to scene in Outliner"""

def scene_operation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["DELETE"] | None = "DELETE",
) -> None:
    """Context menu for scene operations

    :param type: Scene Operation
    """

def scroll_page(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    up: bool | None = False,
) -> None:
    """Scroll page up or down

    :param up: Up, Scroll up one page
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Toggle the Outliner selection of items

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
    """Use box selection to select tree elements

        :param tweak: Tweak, Tweak gesture from empty space for box selection
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

def select_walk(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN", "LEFT", "RIGHT"] | None = "UP",
    extend: bool | None = False,
    toggle_all: bool | None = False,
) -> None:
    """Use walk navigation to select tree elements

    :param direction: Walk Direction, Select/Deselect element in this direction
    :param extend: Extend, Extend selection on walk
    :param toggle_all: Toggle All, Toggle open/close hierarchy
    """

def show_active(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Open up the tree and adjust the view so that the active object is shown centered"""

def show_hierarchy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Open all object entries and close all others"""

def show_one_level(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    open: bool | None = True,
) -> None:
    """Expand/collapse all entries by one level

    :param open: Open, Expand all entries one level deep
    """

def start_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Start entering filter text"""

def unhide_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Unhide all objects and collections"""
