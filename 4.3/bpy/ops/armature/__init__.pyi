import typing
import collections.abc
import typing_extensions
import bpy.ops.transform

def align(execution_context: int | str | None = None, undo: bool | None = None):
    """Align selected bones to the active bone (or to their parent)

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def assign_to_collection(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    collection_index: int | None = -1,
    new_collection_name: str = "",
):
    """Assign all selected bones to a collection, or unassign them, depending on whether the active bone is already assigned or not

    :type execution_context: int | str | None
    :type undo: bool | None
    :param collection_index: Collection Index, Index of the collection to assign selected bones to. When the operator should create a new bone collection, use new_collection_name to define the collection name, and set this parameter to the parent index of the new bone collection
    :type collection_index: int | None
    :param new_collection_name: Name, Name of a to-be-added bone collection. Only pass this if you want to create a new bone collection and assign the selected bones to it. To assign to an existing collection, do not include this parameter and use collection_index
    :type new_collection_name: str
    """

def autoside_names(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["XAXIS", "YAXIS", "ZAXIS"] | None = "XAXIS",
):
    """Automatically renames the selected bones according to which side of the target axis they fall on

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Axis, Axis to tag names with

    XAXIS
    X-Axis -- Left/Right.

    YAXIS
    Y-Axis -- Front/Back.

    ZAXIS
    Z-Axis -- Top/Bottom.
        :type type: typing.Literal['XAXIS','YAXIS','ZAXIS'] | None
    """

def bone_primitive_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
):
    """Add a new bone located at the 3D cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the newly created bone
    :type name: str
    """

def calculate_roll(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "POS_X",
        "POS_Z",
        "GLOBAL_POS_X",
        "GLOBAL_POS_Y",
        "GLOBAL_POS_Z",
        "NEG_X",
        "NEG_Z",
        "GLOBAL_NEG_X",
        "GLOBAL_NEG_Y",
        "GLOBAL_NEG_Z",
        "ACTIVE",
        "VIEW",
        "CURSOR",
    ]
    | None = "POS_X",
    axis_flip: bool | None = False,
    axis_only: bool | None = False,
):
    """Automatically fix alignment of select bones' axes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['POS_X','POS_Z','GLOBAL_POS_X','GLOBAL_POS_Y','GLOBAL_POS_Z','NEG_X','NEG_Z','GLOBAL_NEG_X','GLOBAL_NEG_Y','GLOBAL_NEG_Z','ACTIVE','VIEW','CURSOR'] | None
    :param axis_flip: Flip Axis, Negate the alignment axis
    :type axis_flip: bool | None
    :param axis_only: Shortest Rotation, Ignore the axis direction, use the shortest rotation to align
    :type axis_only: bool | None
    """

def click_extrude(execution_context: int | str | None = None, undo: bool | None = None):
    """Create a new bone going from the last selected joint to the mouse position

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add a new bone collection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_assign(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
):
    """Add selected bones to the chosen bone collection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Bone Collection, Name of the bone collection to assign this bone to; empty to assign to the active bone collection
    :type name: str
    """

def collection_create_and_assign(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
):
    """Create a new bone collection and assign all selected bones

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Bone Collection, Name of the bone collection to create
    :type name: str
    """

def collection_deselect(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Deselect bones of active Bone Collection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Change position of active Bone Collection in list of Bone collections

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to move the active Bone Collection towards
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def collection_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove the active bone collection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_remove_unused(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove all bone collections that have neither bones nor children. This is done recursively, so bone collections that only have unused children are also removed

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_select(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Select bones in active Bone Collection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_show_all(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Show all bone collections

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def collection_unassign(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
):
    """Remove selected bones from the active bone collection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Bone Collection, Name of the bone collection to unassign this bone from; empty to unassign from the active bone collection
    :type name: str
    """

def collection_unassign_named(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    bone_name: str = "",
):
    """Unassign the named bone from this bone collection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Bone Collection, Name of the bone collection to unassign this bone from; empty to unassign from the active bone collection
    :type name: str
    :param bone_name: Bone Name, Name of the bone to unassign from the collection; empty to use the active bone
    :type bone_name: str
    """

def collection_unsolo_all(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Clear the 'solo' setting on all bone collections

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def copy_bone_color_to_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    bone_type: typing.Literal["EDIT", "POSE"] | None = "EDIT",
):
    """Copy the bone color of the active bone to all selected bones

        :type execution_context: int | str | None
        :type undo: bool | None
        :param bone_type: Type

    EDIT
    Bone -- Copy Bone colors from the active bone to all selected bones.

    POSE
    Pose Bone -- Copy Pose Bone colors from the active pose bone to all selected pose bones.
        :type bone_type: typing.Literal['EDIT','POSE'] | None
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
):
    """Remove selected bones from the armature

    :type execution_context: int | str | None
    :type undo: bool | None
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool | None
    """

def dissolve(execution_context: int | str | None = None, undo: bool | None = None):
    """Dissolve selected bones from the armature

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    do_flip_names: bool | None = False,
):
    """Make copies of the selected bones within the same armature

    :type execution_context: int | str | None
    :type undo: bool | None
    :param do_flip_names: Flip Names, Try to flip names of the bones, if possible, instead of adding a number extension
    :type do_flip_names: bool | None
    """

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ARMATURE_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Make copies of the selected bones within the same armature and move them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param ARMATURE_OT_duplicate: Duplicate Selected Bone(s), Make copies of the selected bones within the same armature
    :type ARMATURE_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def extrude(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    forked: bool | None = False,
):
    """Create new bones from the selected joints

    :type execution_context: int | str | None
    :type undo: bool | None
    :param forked: Forked
    :type forked: bool | None
    """

def extrude_forked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ARMATURE_OT_extrude: extrude | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Create new bones from the selected joints and move them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param ARMATURE_OT_extrude: Extrude, Create new bones from the selected joints
    :type ARMATURE_OT_extrude: extrude | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def extrude_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ARMATURE_OT_extrude: extrude | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Create new bones from the selected joints and move them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param ARMATURE_OT_extrude: Extrude, Create new bones from the selected joints
    :type ARMATURE_OT_extrude: extrude | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def fill(execution_context: int | str | None = None, undo: bool | None = None):
    """Add bone between selected joint(s) and/or 3D cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def flip_names(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    do_strip_numbers: bool | None = False,
):
    """Flips (and corrects) the axis suffixes of the names of selected bones

    :type execution_context: int | str | None
    :type undo: bool | None
    :param do_strip_numbers: Strip Numbers, Try to remove right-most dot-number from flipped names.Warning: May result in incoherent naming in some cases
    :type do_strip_numbers: bool | None
    """

def hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
):
    """Tag selected bones to not be visible in Edit Mode

    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: bool | None
    """

def move_to_collection(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    collection_index: int | None = -1,
    new_collection_name: str = "",
):
    """Move bones to a collection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param collection_index: Collection Index, Index of the collection to move selected bones to. When the operator should create a new bone collection, do not include this parameter and pass new_collection_name
    :type collection_index: int | None
    :param new_collection_name: Name, Name of a to-be-added bone collection. Only pass this if you want to create a new bone collection and move the selected bones to it. To move to an existing collection, do not include this parameter and use collection_index
    :type new_collection_name: str
    """

def parent_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CLEAR", "DISCONNECT"] | None = "CLEAR",
):
    """Remove the parent-child relationship between selected bones and their parents

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Clear Type, What way to clear parenting
    :type type: typing.Literal['CLEAR','DISCONNECT'] | None
    """

def parent_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CONNECTED", "OFFSET"] | None = "CONNECTED",
):
    """Set the active bone as the parent of the selected bones

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Parent Type, Type of parenting
    :type type: typing.Literal['CONNECTED','OFFSET'] | None
    """

def reveal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
):
    """Reveal all bones hidden in Edit Mode

    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | None
    """

def roll_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    roll: float | None = 0.0,
):
    """Clear roll for selected bones

    :type execution_context: int | str | None
    :type undo: bool | None
    :param roll: Roll
    :type roll: float | None
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Toggle selection status of all bones

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

def select_hierarchy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["PARENT", "CHILD"] | None = "PARENT",
    extend: bool | None = False,
):
    """Select immediate parent/children of selected bones

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction
    :type direction: typing.Literal['PARENT','CHILD'] | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def select_less(execution_context: int | str | None = None, undo: bool | None = None):
    """Deselect those bones at the boundary of each selection region

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all_forks: bool | None = False,
):
    """Select all bones linked by parent/child connections to the current selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all_forks: All Forks, Follow forks in the parents chain
    :type all_forks: bool | None
    """

def select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deselect: bool | None = False,
    all_forks: bool | None = False,
):
    """(De)select bones linked by parent/child connections under the mouse cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param deselect: Deselect
    :type deselect: bool | None
    :param all_forks: All Forks, Follow forks in the parents chain
    :type all_forks: bool | None
    """

def select_mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_active: bool | None = False,
    extend: bool | None = False,
):
    """Mirror the bone selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_active: Active Only, Only operate on the active bone
    :type only_active: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def select_more(execution_context: int | str | None = None, undo: bool | None = None):
    """Select those bones connected to the initial selection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_similar(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "CHILDREN",
        "CHILDREN_IMMEDIATE",
        "SIBLINGS",
        "LENGTH",
        "DIRECTION",
        "PREFIX",
        "SUFFIX",
        "BONE_COLLECTION",
        "COLOR",
        "SHAPE",
    ]
    | None = "LENGTH",
    threshold: float | None = 0.1,
):
    """Select similar bones by property types

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['CHILDREN','CHILDREN_IMMEDIATE','SIBLINGS','LENGTH','DIRECTION','PREFIX','SUFFIX','BONE_COLLECTION','COLOR','SHAPE'] | None
    :param threshold: Threshold
    :type threshold: float | None
    """

def separate(execution_context: int | str | None = None, undo: bool | None = None):
    """Isolate selected bones into a separate armature

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def shortest_path_pick(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Select shortest path between two bones

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def split(execution_context: int | str | None = None, undo: bool | None = None):
    """Split off selected bones from connected unselected bones

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def subdivide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number_cuts: int | None = 1,
):
    """Break selected bones into chains of smaller bones

    :type execution_context: int | str | None
    :type undo: bool | None
    :param number_cuts: Number of Cuts
    :type number_cuts: int | None
    """

def switch_direction(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Change the direction that a chain of bones points in (head and tail swap)

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def symmetrize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["NEGATIVE_X", "POSITIVE_X"] | None = "NEGATIVE_X",
):
    """Enforce symmetry, make copies of the selection or use existing

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Which sides to copy from and to (when both are selected)
    :type direction: typing.Literal['NEGATIVE_X','POSITIVE_X'] | None
    """
