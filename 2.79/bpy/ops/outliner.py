import sys
import typing


def action_set(action: int = ''):
    '''Change the active action used 

    :param action: Action 
    :type action: int
    '''

    pass


def animdata_operation(type: int = 'CLEAR_ANIMDATA'):
    '''Undocumented 

    :param type: Animation OperationCLEAR_ANIMDATA Clear Animation Data, Remove this animation data container.SET_ACT Set Action.CLEAR_ACT Unlink Action.REFRESH_DRIVERS Refresh Drivers.CLEAR_DRIVERS Clear Drivers. 
    :type type: int
    '''

    pass


def constraint_operation(type: int = 'ENABLE'):
    '''Undocumented 

    :param type: Constraint Operation 
    :type type: int
    '''

    pass


def data_operation(type: int = 'SELECT'):
    '''Undocumented 

    :param type: Data Operation 
    :type type: int
    '''

    pass


def drivers_add_selected():
    '''Add drivers to selected items 

    '''

    pass


def drivers_delete_selected():
    '''Delete drivers assigned to selected items 

    '''

    pass


def expanded_toggle():
    '''Expand/Collapse all items 

    '''

    pass


def group_link(object: str = "Object"):
    '''Link Object to Group in Outliner 

    :param object: Object, Target Object 
    :type object: str
    '''

    pass


def group_operation(type: int = 'UNLINK'):
    '''Undocumented 

    :param type: Group OperationUNLINK Unlink Group.LOCAL Make Local Group.LINK Link Group Objects to Scene.DELETE Delete Group.REMAP Remap Users, Make all users of selected data-blocks to use instead current (clicked) one.INSTANCE Instance Groups in Scene.TOGVIS Toggle Visible Group.TOGSEL Toggle Selectable.TOGREN Toggle Renderable.RENAME Rename. 
    :type type: int
    '''

    pass


def id_delete():
    '''Delete the ID under cursor 

    '''

    pass


def id_operation(type: int = 'UNLINK'):
    '''Undocumented 

    :param type: ID data OperationUNLINK Unlink.LOCAL Make Local.SINGLE Make Single User.DELETE Delete, WARNING: no undo.REMAP Remap Users, Make all users of selected data-blocks to use instead current (clicked) one.ADD_FAKE Add Fake User, Ensure data-block gets saved even if it isn’t in use (e.g. for motion and material libraries).CLEAR_FAKE Clear Fake User.RENAME Rename.SELECT_LINKED Select Linked. 
    :type type: int
    '''

    pass


def id_remap(id_type: int = 'OBJECT', old_id: int = '', new_id: int = ''):
    '''Undocumented 

    :param id_type: ID Type 
    :type id_type: int
    :param old_id: Old ID, Old ID to replace 
    :type old_id: int
    :param new_id: New ID, New ID to remap all selected IDs’ users to 
    :type new_id: int
    '''

    pass


def item_activate(extend: bool = True, recursive: bool = False):
    '''Handle mouse clicks to activate/select items 

    :param extend: Extend, Extend selection for activation 
    :type extend: bool
    :param recursive: Recursive, Select Objects and their children 
    :type recursive: bool
    '''

    pass


def item_openclose(all: bool = True):
    '''Toggle whether item under cursor is enabled or closed 

    :param all: All, Close or open all items 
    :type all: bool
    '''

    pass


def item_rename():
    '''Rename item under cursor 

    '''

    pass


def keyingset_add_selected():
    '''Add selected items (blue-gray rows) to active Keying Set 

    '''

    pass


def keyingset_remove_selected():
    '''Remove selected items (blue-gray rows) from active Keying Set 

    '''

    pass


def lib_operation(type: int = 'RENAME'):
    '''Undocumented 

    :param type: Library OperationRENAME Rename.DELETE Delete, Delete this library and all its item from Blender - WARNING: no undo.RELOCATE Relocate, Select a new path for this library, and reload all its data.RELOAD Reload, Reload all data from this library. 
    :type type: int
    '''

    pass


def lib_relocate():
    '''Relocate the library under cursor 

    '''

    pass


def material_drop(object: str = "Object", material: str = "Material"):
    '''Drag material to object in Outliner 

    :param object: Object, Target Object 
    :type object: str
    :param material: Material, Target Material 
    :type material: str
    '''

    pass


def modifier_operation(type: int = 'TOGVIS'):
    '''Undocumented 

    :param type: Modifier Operation 
    :type type: int
    '''

    pass


def object_operation(type: int = 'SELECT'):
    '''Undocumented 

    :param type: Object OperationSELECT Select.DESELECT Deselect.SELECT_HIERARCHY Select Hierarchy.DELETE Delete.DELETE_HIERARCHY Delete Hierarchy.REMAP Remap Users, Make all users of selected data-blocks to use instead a new chosen one.TOGVIS Toggle Visible.TOGSEL Toggle Selectable.TOGREN Toggle Renderable.RENAME Rename. 
    :type type: int
    '''

    pass


def operation():
    '''Context menu for item operations 

    '''

    pass


def orphans_purge():
    '''Clear all orphaned data-blocks without any users from the file (cannot be undone, saves to current .blend file) 

    '''

    pass


def parent_clear(dragged_obj: str = "Object", type: int = 'CLEAR'):
    '''Drag to clear parent in Outliner 

    :param dragged_obj: Child, Child Object 
    :type dragged_obj: str
    :param type: TypeCLEAR Clear Parent, Completely clear the parenting relationship, including involved modifiers if any.CLEAR_KEEP_TRANSFORM Clear and Keep Transformation, As ‘Clear Parent’, but keep the current visual transformations of the object.CLEAR_INVERSE Clear Parent Inverse, Reset the transform corrections applied to the parenting relationship, does not remove parenting itself. 
    :type type: int
    '''

    pass


def parent_drop(child: str = "Object",
                parent: str = "Object",
                type: int = 'OBJECT'):
    '''Drag to parent in Outliner 

    :param child: Child, Child Object 
    :type child: str
    :param parent: Parent, Parent Object 
    :type parent: str
    :param type: Type 
    :type type: int
    '''

    pass


def renderability_toggle():
    '''Toggle the renderability of selected items 

    '''

    pass


def scene_drop(object: str = "Object", scene: str = "Scene"):
    '''Drag object to scene in Outliner 

    :param object: Object, Target Object 
    :type object: str
    :param scene: Scene, Target Scene 
    :type scene: str
    '''

    pass


def scene_operation(type: int = 'DELETE'):
    '''Context menu for scene operations 

    :param type: Scene Operation 
    :type type: int
    '''

    pass


def scroll_page(up: bool = False):
    '''Scroll page up or down 

    :param up: Up, Scroll up one page 
    :type up: bool
    '''

    pass


def select_border(gesture_mode: int = 0,
                  xmin: int = 0,
                  xmax: int = 0,
                  ymin: int = 0,
                  ymax: int = 0):
    '''Use box selection to select tree elements 

    :param gesture_mode: Gesture Mode 
    :type gesture_mode: int
    :param xmin: X Min 
    :type xmin: int
    :param xmax: X Max 
    :type xmax: int
    :param ymin: Y Min 
    :type ymin: int
    :param ymax: Y Max 
    :type ymax: int
    '''

    pass


def selectability_toggle():
    '''Toggle the selectability 

    '''

    pass


def selected_toggle():
    '''Toggle the Outliner selection of items 

    '''

    pass


def show_active():
    '''Open up the tree and adjust the view so that the active Object is shown centered 

    '''

    pass


def show_hierarchy():
    '''Open all object entries and close all others 

    '''

    pass


def show_one_level(open: bool = True):
    '''Expand/collapse all entries by one level 

    :param open: Open, Expand all entries one level deep 
    :type open: bool
    '''

    pass


def visibility_toggle():
    '''Toggle the visibility of selected items 

    '''

    pass
