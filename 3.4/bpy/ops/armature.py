import sys
import typing
import bpy.types
import bpy.ops.transform

GenericType = typing.TypeVar("GenericType")


def align(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: typing.Optional[bool] = None):
    ''' Align selected bones to the active bone (or to their parent)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def armature_layers(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        layers: typing.Union[typing.List[bool], typing.Any] = (
            False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False,
            False, False, False, False, False)):
    ''' Change the visible armature layers

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param layers: Layer, Armature layers to make visible
    :type layers: typing.Union[typing.List[bool], typing.Any]
    '''

    pass


def autoside_names(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   type: typing.Optional[typing.Any] = 'XAXIS'):
    ''' Automatically renames the selected bones according to which side of the target axis they fall on

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Axis, Axis tag names with * ``XAXIS`` X-Axis -- Left/Right. * ``YAXIS`` Y-Axis -- Front/Back. * ``ZAXIS`` Z-Axis -- Top/Bottom.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def bone_layers(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                layers: typing.Union[typing.List[bool], typing.Any] = (
                    False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False)):
    ''' Change the layers that the selected bones belong to

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param layers: Layer, Armature layers that bone belongs to
    :type layers: typing.Union[typing.List[bool], typing.Any]
    '''

    pass


def bone_primitive_add(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       name: typing.Union[str, typing.Any] = "Bone"):
    ''' Add a new bone located at the 3D cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the newly created bone
    :type name: typing.Union[str, typing.Any]
    '''

    pass


def calculate_roll(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   type: typing.Optional[typing.Any] = 'POS_X',
                   axis_flip: typing.Union[bool, typing.Any] = False,
                   axis_only: typing.Union[bool, typing.Any] = False):
    ''' Automatically fix alignment of select bones' axes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param axis_flip: Flip Axis, Negate the alignment axis
    :type axis_flip: typing.Union[bool, typing.Any]
    :param axis_only: Shortest Rotation, Ignore the axis direction, use the shortest rotation to align
    :type axis_only: typing.Union[bool, typing.Any]
    '''

    pass


def click_extrude(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None):
    ''' Create a new bone going from the last selected joint to the mouse position

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None):
    ''' Remove selected bones from the armature

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def dissolve(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None):
    ''' Dissolve selected bones from the armature

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def duplicate(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              do_flip_names: typing.Union[bool, typing.Any] = False):
    ''' Make copies of the selected bones within the same armature

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param do_flip_names: Flip Names, Try to flip names of the bones, if possible, instead of adding a number extension
    :type do_flip_names: typing.Union[bool, typing.Any]
    '''

    pass


def duplicate_move(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   ARMATURE_OT_duplicate: typing.Optional['duplicate'] = None,
                   TRANSFORM_OT_translate: typing.
                   Optional['bpy.ops.transform.translate'] = None):
    ''' Make copies of the selected bones within the same armature and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param ARMATURE_OT_duplicate: Duplicate Selected Bone(s), Make copies of the selected bones within the same armature
    :type ARMATURE_OT_duplicate: typing.Optional['duplicate']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def extrude(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: typing.Optional[bool] = None,
            *,
            forked: typing.Union[bool, typing.Any] = False):
    ''' Create new bones from the selected joints

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param forked: Forked
    :type forked: typing.Union[bool, typing.Any]
    '''

    pass


def extrude_forked(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   ARMATURE_OT_extrude: typing.Optional['extrude'] = None,
                   TRANSFORM_OT_translate: typing.
                   Optional['bpy.ops.transform.translate'] = None):
    ''' Create new bones from the selected joints and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param ARMATURE_OT_extrude: Extrude, Create new bones from the selected joints
    :type ARMATURE_OT_extrude: typing.Optional['extrude']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def extrude_move(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 ARMATURE_OT_extrude: typing.Optional['extrude'] = None,
                 TRANSFORM_OT_translate: typing.
                 Optional['bpy.ops.transform.translate'] = None):
    ''' Create new bones from the selected joints and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param ARMATURE_OT_extrude: Extrude, Create new bones from the selected joints
    :type ARMATURE_OT_extrude: typing.Optional['extrude']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def fill(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None):
    ''' Add bone between selected joint(s) and/or 3D cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def flip_names(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               do_strip_numbers: typing.Union[bool, typing.Any] = False):
    ''' Flips (and corrects) the axis suffixes of the names of selected bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param do_strip_numbers: May result in incoherent naming in some cases
    :type do_strip_numbers: typing.Union[bool, typing.Any]
    '''

    pass


def hide(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         unselected: typing.Union[bool, typing.Any] = False):
    ''' Tag selected bones to not be visible in Edit Mode

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: typing.Union[bool, typing.Any]
    '''

    pass


def layers_show_all(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    all: typing.Union[bool, typing.Any] = True):
    ''' Make all armature layers visible

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param all: All Layers, Enable all layers or just the first 16 (top row)
    :type all: typing.Union[bool, typing.Any]
    '''

    pass


def parent_clear(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 type: typing.Optional[typing.Any] = 'CLEAR'):
    ''' Remove the parent-child relationship between selected bones and their parents

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Clear Type, What way to clear parenting
    :type type: typing.Optional[typing.Any]
    '''

    pass


def parent_set(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               type: typing.Optional[typing.Any] = 'CONNECTED'):
    ''' Set the active bone as the parent of the selected bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Parent Type, Type of parenting
    :type type: typing.Optional[typing.Any]
    '''

    pass


def reveal(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           select: typing.Union[bool, typing.Any] = True):
    ''' Reveal all bones hidden in Edit Mode

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param select: Select
    :type select: typing.Union[bool, typing.Any]
    '''

    pass


def roll_clear(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               roll: typing.Optional[typing.Any] = 0.0):
    ''' Clear roll for selected bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param roll: Roll
    :type roll: typing.Optional[typing.Any]
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Toggle selection status of all bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param action: Action, Selection action to execute * ``TOGGLE`` Toggle -- Toggle selection for all elements. * ``SELECT`` Select -- Select all elements. * ``DESELECT`` Deselect -- Deselect all elements. * ``INVERT`` Invert -- Invert selection of all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_hierarchy(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     direction: typing.Optional[typing.Any] = 'PARENT',
                     extend: typing.Union[bool, typing.Any] = False):
    ''' Select immediate parent/children of selected bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param direction: Direction
    :type direction: typing.Optional[typing.Any]
    :param extend: Extend, Extend the selection
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass


def select_less(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Deselect those bones at the boundary of each selection region

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_linked(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  all_forks: typing.Union[bool, typing.Any] = False):
    ''' Select all bones linked by parent/child connections to the current selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param all_forks: All Forks, Follow forks in the parents chain
    :type all_forks: typing.Union[bool, typing.Any]
    '''

    pass


def select_linked_pick(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       deselect: typing.Union[bool, typing.Any] = False,
                       all_forks: typing.Union[bool, typing.Any] = False):
    ''' (De)select bones linked by parent/child connections under the mouse cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param deselect: Deselect
    :type deselect: typing.Union[bool, typing.Any]
    :param all_forks: All Forks, Follow forks in the parents chain
    :type all_forks: typing.Union[bool, typing.Any]
    '''

    pass


def select_mirror(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  only_active: typing.Union[bool, typing.Any] = False,
                  extend: typing.Union[bool, typing.Any] = False):
    ''' Mirror the bone selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param only_active: Active Only, Only operate on the active bone
    :type only_active: typing.Union[bool, typing.Any]
    :param extend: Extend, Extend the selection
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass


def select_more(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Select those bones connected to the initial selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_similar(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   type: typing.Optional[typing.Any] = 'LENGTH',
                   threshold: typing.Optional[typing.Any] = 0.1):
    ''' Select similar bones by property types

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param threshold: Threshold
    :type threshold: typing.Optional[typing.Any]
    '''

    pass


def separate(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None):
    ''' Isolate selected bones into a separate armature

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def shortest_path_pick(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None):
    ''' Select shortest path between two bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def split(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: typing.Optional[bool] = None):
    ''' Split off selected bones from connected unselected bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def subdivide(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              number_cuts: typing.Optional[typing.Any] = 1):
    ''' Break selected bones into chains of smaller bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param number_cuts: Number of Cuts
    :type number_cuts: typing.Optional[typing.Any]
    '''

    pass


def switch_direction(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None):
    ''' Change the direction that a chain of bones points in (head and tail swap)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def symmetrize(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               direction: typing.Optional[typing.Any] = 'NEGATIVE_X'):
    ''' Enforce symmetry, make copies of the selection or use existing

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Which sides to copy from and to (when both are selected)
    :type direction: typing.Optional[typing.Any]
    '''

    pass
