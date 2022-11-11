import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def background_image_add(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: bool = None,
                         *,
                         name: str = "",
                         session_uuid: int = 0,
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
                         sort_method: typing.Union[str, int] = ''):
    ''' Add a new background image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
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
    '''

    pass


def background_image_remove(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None,
                            *,
                            index: int = 0):
    ''' Remove a background image from the 3D view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param index: Index, Background image index to remove
    :type index: int
    '''

    pass


def bone_select_menu(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     name: typing.Union[str, int] = '',
                     extend: bool = False,
                     deselect: bool = False,
                     toggle: bool = False):
    ''' Menu bone selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Bone Name
    :type name: typing.Union[str, int]
    :param extend: Extend
    :type extend: bool
    :param deselect: Deselect
    :type deselect: bool
    :param toggle: Toggle
    :type toggle: bool
    '''

    pass


def camera_to_view(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Set camera view to active view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def camera_to_view_selected(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None):
    ''' Move the camera so selected objects are framed

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def clear_render_border(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Clear the boundaries of the border render and disable border render

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def clip_border(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                xmin: int = 0,
                xmax: int = 0,
                ymin: int = 0,
                ymax: int = 0,
                wait_for_input: bool = True):
    ''' Set the view clipping region

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


def copybuffer(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Selected objects are copied to the clipboard

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def cursor3d(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             use_depth: bool = True,
             orientation: typing.Union[str, int] = 'VIEW'):
    ''' Set the location of the 3D cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_depth: Surface Project, Project onto the surface
    :type use_depth: bool
    :param orientation: Orientation, Preset viewpoint to use * NONE None -- Leave orientation unchanged. * VIEW View -- Orient to the viewport. * XFORM Transform -- Orient to the current transform setting. * GEOM Geometry -- Match the surface normal.
    :type orientation: typing.Union[str, int]
    '''

    pass


def dolly(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None,
          *,
          mx: int = 0,
          my: int = 0,
          delta: int = 0,
          use_cursor_init: bool = True):
    ''' Dolly in/out in the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mx: Region Position X
    :type mx: int
    :param my: Region Position Y
    :type my: int
    :param delta: Delta
    :type delta: int
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    :type use_cursor_init: bool
    '''

    pass


def drop_world(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               name: str = "",
               session_uuid: int = 0):
    ''' Drop a world into the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    '''

    pass


def edit_mesh_extrude_individual_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Extrude each individual face separately along local normals :file: startup/bl_operators/view3d.py\:21 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/view3d.py$21> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def edit_mesh_extrude_manifold_normal(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Extrude manifold region along normals :file: startup/bl_operators/view3d.py\:154 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/view3d.py$154> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def edit_mesh_extrude_move_normal(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        dissolve_and_intersect: bool = False):
    ''' Extrude region together along the average normal

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param dissolve_and_intersect: dissolve_and_intersect, Dissolves adjacent faces and intersects new geometry
    :type dissolve_and_intersect: bool
    '''

    pass


def edit_mesh_extrude_move_shrink_fatten(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Extrude region together along local normals :file: startup/bl_operators/view3d.py\:137 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/view3d.py$137> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def fly(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Interactively fly around the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def interactive_add(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    primitive_type: typing.Union[str, int] = 'CUBE',
                    plane_axis: typing.Union[int, str] = 'Z',
                    plane_axis_auto: bool = False,
                    plane_depth: typing.Union[str, int] = 'SURFACE',
                    plane_orientation: typing.Union[str, int] = 'SURFACE',
                    snap_target: typing.Union[str, int] = 'GEOMETRY',
                    plane_origin_base: typing.Union[str, int] = 'EDGE',
                    plane_origin_depth: typing.Union[str, int] = 'EDGE',
                    plane_aspect_base: typing.Union[str, int] = 'FREE',
                    plane_aspect_depth: typing.Union[str, int] = 'FREE',
                    wait_for_input: bool = True):
    ''' Interactively add an object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param primitive_type: Primitive
    :type primitive_type: typing.Union[str, int]
    :param plane_axis: Plane Axis, The axis used for placing the base region
    :type plane_axis: typing.Union[int, str]
    :param plane_axis_auto: Auto Axis, Select the closest axis when placing objects (surface overrides)
    :type plane_axis_auto: bool
    :param plane_depth: Position, The initial depth used when placing the cursor * SURFACE Surface -- Start placing on the surface, using the 3D cursor position as a fallback. * CURSOR_PLANE Cursor Plane -- Start placement using a point projected onto the orientation axis at the 3D cursor position. * CURSOR_VIEW Cursor View -- Start placement using a point projected onto the view plane at the 3D cursor position.
    :type plane_depth: typing.Union[str, int]
    :param plane_orientation: Orientation, The initial depth used when placing the cursor * SURFACE Surface -- Use the surface normal (using the transform orientation as a fallback). * DEFAULT Default -- Use the current transform orientation.
    :type plane_orientation: typing.Union[str, int]
    :param snap_target: Snap to, The target to use while snapping * GEOMETRY Geometry -- Snap to all geometry. * DEFAULT Default -- Use the current snap settings.
    :type snap_target: typing.Union[str, int]
    :param plane_origin_base: Origin, The initial position for placement * EDGE Edge -- Start placing the edge position. * CENTER Center -- Start placing the center position.
    :type plane_origin_base: typing.Union[str, int]
    :param plane_origin_depth: Origin, The initial position for placement * EDGE Edge -- Start placing the edge position. * CENTER Center -- Start placing the center position.
    :type plane_origin_depth: typing.Union[str, int]
    :param plane_aspect_base: Aspect, The initial aspect setting * FREE Free -- Use an unconstrained aspect. * FIXED Fixed -- Use a fixed 1:1 aspect.
    :type plane_aspect_base: typing.Union[str, int]
    :param plane_aspect_depth: Aspect, The initial aspect setting * FREE Free -- Use an unconstrained aspect. * FIXED Fixed -- Use a fixed 1:1 aspect.
    :type plane_aspect_depth: typing.Union[str, int]
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def localview(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              frame_selected: bool = True):
    ''' Toggle display of selected object(s) separately and centered in view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame_selected: Frame Selected, Move the view to frame the selected objects
    :type frame_selected: bool
    '''

    pass


def localview_remove_from(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Move selected objects out of local view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def move(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         use_cursor_init: bool = True):
    ''' Move the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    :type use_cursor_init: bool
    '''

    pass


def navigate(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None):
    ''' Interactively navigate around the scene (uses the mode (walk/fly) preference)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def ndof_all(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None):
    ''' Pan and rotate the view with the 3D mouse

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def ndof_orbit(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Orbit the view using the 3D mouse

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def ndof_orbit_zoom(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Orbit and zoom the view using the 3D mouse

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def ndof_pan(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None):
    ''' Pan the view with the 3D mouse

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def object_as_camera(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Set the active object as the active camera for this view or scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def object_mode_pie_or_toggle(override_context: typing.
                              Union[typing.Dict, 'bpy.types.Context'] = None,
                              execution_context: typing.Union[str, int] = None,
                              undo: bool = None):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def pastebuffer(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                autoselect: bool = True,
                active_collection: bool = True):
    ''' Objects from the clipboard are pasted

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param autoselect: Select, Select pasted objects
    :type autoselect: bool
    :param active_collection: Active Collection, Put pasted objects in the active collection
    :type active_collection: bool
    '''

    pass


def render_border(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  xmin: int = 0,
                  xmax: int = 0,
                  ymin: int = 0,
                  ymax: int = 0,
                  wait_for_input: bool = True):
    ''' Set the boundaries of the border render and enable border render

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


def rotate(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           use_cursor_init: bool = True):
    ''' Rotate the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    :type use_cursor_init: bool
    '''

    pass


def ruler_add(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None):
    ''' Add ruler

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def ruler_remove(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

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
           center: bool = False,
           enumerate: bool = False,
           object: bool = False,
           vert_without_handles: bool = False,
           location: typing.List[int] = (0, 0)):
    ''' Select and activate item(s)

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
    :param center: Center, Use the object center when selecting, in edit mode used to extend object selection
    :type center: bool
    :param enumerate: Enumerate, List objects under the mouse (object mode only)
    :type enumerate: bool
    :param object: Object, Use object selection (edit mode only)
    :type object: bool
    :param vert_without_handles: Control Point Without Handles, Only select the curve control point, not it's handles
    :type vert_without_handles: bool
    :param location: Location, Mouse location
    :type location: typing.List[int]
    '''

    pass


def select_box(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               xmin: int = 0,
               xmax: int = 0,
               ymin: int = 0,
               ymax: int = 0,
               wait_for_input: bool = True,
               mode: typing.Union[str, int] = 'SET'):
    ''' Select items using box selection

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
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection. * XOR Difference -- Invert existing selection. * AND Intersect -- Intersect existing selection.
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
    ''' Select items using circle selection

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


def select_lasso(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 path: bpy.types.
                 bpy_prop_collection['bpy.types.OperatorMousePath'] = None,
                 mode: typing.Union[str, int] = 'SET'):
    ''' Select items using lasso selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param path: Path
    :type path: bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection. * XOR Difference -- Invert existing selection. * AND Intersect -- Intersect existing selection.
    :type mode: typing.Union[str, int]
    '''

    pass


def select_menu(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                name: typing.Union[str, int] = '',
                extend: bool = False,
                deselect: bool = False,
                toggle: bool = False):
    ''' Menu object selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: Object Name
    :type name: typing.Union[str, int]
    :param extend: Extend
    :type extend: bool
    :param deselect: Deselect
    :type deselect: bool
    :param toggle: Toggle
    :type toggle: bool
    '''

    pass


def smoothview(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def snap_cursor_to_active(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Snap 3D cursor to the active item

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def snap_cursor_to_center(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Snap 3D cursor to the world origin

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def snap_cursor_to_grid(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Snap 3D cursor to the nearest grid division

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def snap_cursor_to_selected(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None):
    ''' Snap 3D cursor to the middle of the selected item(s)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def snap_selected_to_active(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None):
    ''' Snap selected item(s) to the active item

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def snap_selected_to_cursor(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None,
                            *,
                            use_offset: bool = True):
    ''' Snap selected item(s) to the 3D cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_offset: Offset, If the selection should be snapped as a whole or by each object center
    :type use_offset: bool
    '''

    pass


def snap_selected_to_grid(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Snap selected item(s) to their nearest grid division

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def toggle_matcap_flip(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Flip MatCap

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def toggle_shading(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None,
                   *,
                   type: typing.Union[str, int] = 'WIREFRAME'):
    ''' Toggle shading type in 3D viewport

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type, Shading type to toggle * WIREFRAME Wireframe -- Toggle wireframe shading. * SOLID Solid -- Toggle solid shading. * MATERIAL Material Preview -- Toggle material preview shading. * RENDERED Rendered -- Toggle rendered shading.
    :type type: typing.Union[str, int]
    '''

    pass


def toggle_xray(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Transparent scene display. Allow selecting through items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def transform_gizmo_set(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        extend: bool = False,
        type: typing.Union[typing.Set[str], typing.Set[int]] = {}):
    ''' Set the current transform gizmo

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param extend: Extend
    :type extend: bool
    :param type: Type
    :type type: typing.Union[typing.Set[str], typing.Set[int]]
    '''

    pass


def view_all(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             use_all_regions: bool = False,
             center: bool = False):
    ''' View all objects in scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_all_regions: All Regions, View selected for all regions
    :type use_all_regions: bool
    :param center: Center
    :type center: bool
    '''

    pass


def view_axis(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              type: typing.Union[str, int] = 'LEFT',
              align_active: bool = False,
              relative: bool = False):
    ''' Use a preset viewpoint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: View, Preset viewpoint to use * LEFT Left -- View from the left. * RIGHT Right -- View from the right. * BOTTOM Bottom -- View from the bottom. * TOP Top -- View from the top. * FRONT Front -- View from the front. * BACK Back -- View from the back.
    :type type: typing.Union[str, int]
    :param align_active: Align Active, Align to the active object's axis
    :type align_active: bool
    :param relative: Relative, Rotate relative to the current orientation
    :type relative: bool
    '''

    pass


def view_camera(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Toggle the camera view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_center_camera(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Center the camera view, resizing the view to fit its bounds

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_center_cursor(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Center the view so that the cursor is in the middle of the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_center_lock(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Center the view lock offset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_center_pick(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Center the view to the Z-depth position under the mouse cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_lock_clear(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Clear all view locking

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_lock_to_active(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Lock the view to the active object/bone

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_orbit(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               angle: float = 0.0,
               type: typing.Union[str, int] = 'ORBITLEFT'):
    ''' Orbit the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param angle: Roll
    :type angle: float
    :param type: Orbit, Direction of View Orbit * ORBITLEFT Orbit Left -- Orbit the view around to the left. * ORBITRIGHT Orbit Right -- Orbit the view around to the right. * ORBITUP Orbit Up -- Orbit the view up. * ORBITDOWN Orbit Down -- Orbit the view down.
    :type type: typing.Union[str, int]
    '''

    pass


def view_pan(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             type: typing.Union[str, int] = 'PANLEFT'):
    ''' Pan the view in a given direction

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Pan, Direction of View Pan * PANLEFT Pan Left -- Pan the view to the left. * PANRIGHT Pan Right -- Pan the view to the right. * PANUP Pan Up -- Pan the view up. * PANDOWN Pan Down -- Pan the view down.
    :type type: typing.Union[str, int]
    '''

    pass


def view_persportho(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Switch the current view from perspective/orthographic projection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_roll(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              angle: float = 0.0,
              type: typing.Union[str, int] = 'ANGLE'):
    ''' Roll the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param angle: Roll
    :type angle: float
    :param type: Roll Angle Source, How roll angle is calculated * ANGLE Roll Angle -- Roll the view using an angle value. * LEFT Roll Left -- Roll the view around to the left. * RIGHT Roll Right -- Roll the view around to the right.
    :type type: typing.Union[str, int]
    '''

    pass


def view_selected(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  use_all_regions: bool = False):
    ''' Move the view to the selection center

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param use_all_regions: All Regions, View selected for all regions
    :type use_all_regions: bool
    '''

    pass


def walk(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None):
    ''' Interactively walk around the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def zoom(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         mx: int = 0,
         my: int = 0,
         delta: int = 0,
         use_cursor_init: bool = True):
    ''' Zoom in/out in the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mx: Region Position X
    :type mx: int
    :param my: Region Position Y
    :type my: int
    :param delta: Delta
    :type delta: int
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    :type use_cursor_init: bool
    '''

    pass


def zoom_border(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                xmin: int = 0,
                xmax: int = 0,
                ymin: int = 0,
                ymax: int = 0,
                wait_for_input: bool = True,
                zoom_out: bool = False):
    ''' Zoom in the view to the nearest object contained in the border

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
    :param zoom_out: Zoom Out
    :type zoom_out: bool
    '''

    pass


def zoom_camera_1_to_1(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Match the camera to 1:1 to the render output

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
