import sys
import typing
import bpy


def background_image_add(name: str = "Image",
                         filepath: str = "",
                         filter_blender: bool = False,
                         filter_backup: bool = False,
                         filter_image: bool = True,
                         filter_movie: bool = True,
                         filter_python: bool = False,
                         filter_font: bool = False,
                         filter_sound: bool = False,
                         filter_text: bool = False,
                         filter_btx: bool = False,
                         filter_collada: bool = False,
                         filter_alembic: bool = False,
                         filter_folder: bool = True,
                         filter_blenlib: bool = False,
                         filemode: int = 9,
                         relative_path: bool = True,
                         show_multiview: bool = False,
                         use_multiview: bool = False,
                         display_type: int = 'DEFAULT',
                         sort_method: int = 'FILE_SORT_ALPHA'):
    '''Add a new background image (Ctrl for Empty Object) 

    :param name: Name, Image name to assign 
    :type name: str
    :param filepath: File Path, Path to file 
    :type filepath: str
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
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
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
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    '''

    pass


def background_image_remove(index: int = 0):
    '''Remove a background image from the 3D view 

    :param index: Index, Background image index to remove 
    :type index: int
    '''

    pass


def camera_to_view():
    '''Set camera view to active view 

    '''

    pass


def camera_to_view_selected():
    '''Move the camera so selected objects are framed 

    '''

    pass


def clear_render_border():
    '''Clear the boundaries of the border render and disable border render 

    '''

    pass


def clip_border(xmin: int = 0, xmax: int = 0, ymin: int = 0, ymax: int = 0):
    '''Set the view clipping border 

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


def copybuffer():
    '''Selected objects are saved in a temp file 

    '''

    pass


def cursor3d():
    '''Set the location of the 3D cursor 

    '''

    pass


def dolly(delta: int = 0, mx: int = 0, my: int = 0):
    '''Dolly in/out in the view 

    :param delta: Delta 
    :type delta: int
    :param mx: Zoom Position X 
    :type mx: int
    :param my: Zoom Position Y 
    :type my: int
    '''

    pass


def edit_mesh_extrude_individual_move():
    '''Extrude individual elements and move 

    '''

    pass


def edit_mesh_extrude_move_normal():
    '''Extrude and move along normals 

    '''

    pass


def edit_mesh_extrude_move_shrink_fatten():
    '''Extrude and move along individual normals 

    '''

    pass


def enable_manipulator(translate: bool = False,
                       rotate: bool = False,
                       scale: bool = False):
    '''Enable the transform manipulator for use 

    :param translate: Translate, Enable the translate manipulator 
    :type translate: bool
    :param rotate: Rotate, Enable the rotate manipulator 
    :type rotate: bool
    :param scale: Scale, Enable the scale manipulator 
    :type scale: bool
    '''

    pass


def fly():
    '''Interactively fly around the scene 

    '''

    pass


def game_start():
    '''Start game engine 

    '''

    pass


def layers(nr: int = 1, extend: bool = False, toggle: bool = True):
    '''Toggle layer(s) visibility 

    :param nr: Number, The layer number to set, zero for all layers 
    :type nr: int
    :param extend: Extend, Add this layer to the current view layers 
    :type extend: bool
    :param toggle: Toggle, Toggle the layer 
    :type toggle: bool
    '''

    pass


def localview():
    '''Toggle display of selected object(s) separately and centered in view 

    '''

    pass


def manipulator(constraint_axis: bool = (False, False, False),
                constraint_orientation: int = 'GLOBAL',
                release_confirm: bool = False,
                use_accurate: bool = False,
                use_planar_constraint: bool = False):
    '''Manipulate selected item by axis 

    :param constraint_axis: Constraint Axis 
    :type constraint_axis: bool
    :param constraint_orientation: Orientation, Transformation orientation 
    :type constraint_orientation: int
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: bool
    :param use_planar_constraint: Planar Constraint, Limit the transformation to the two axes that have not been clicked (translate/scale only) 
    :type use_planar_constraint: bool
    '''

    pass


def move():
    '''Move the view 

    '''

    pass


def navigate():
    '''Interactively navigate around the scene (uses the mode (walk/fly) preference) 

    '''

    pass


def ndof_all():
    '''Pan and rotate the view with the 3D mouse 

    '''

    pass


def ndof_orbit():
    '''Orbit the view using the 3D mouse 

    '''

    pass


def ndof_orbit_zoom():
    '''Orbit and zoom the view using the 3D mouse 

    '''

    pass


def ndof_pan():
    '''Pan the view with the 3D mouse 

    '''

    pass


def object_as_camera():
    '''Set the active object as the active camera for this view or scene 

    '''

    pass


def pastebuffer(autoselect: bool = True, active_layer: bool = True):
    '''Contents of copy buffer gets pasted 

    :param autoselect: Select, Select pasted objects 
    :type autoselect: bool
    :param active_layer: Active Layer, Put pasted objects on the active layer 
    :type active_layer: bool
    '''

    pass


def properties():
    '''Toggle the properties region visibility 

    '''

    pass


def render_border(xmin: int = 0,
                  xmax: int = 0,
                  ymin: int = 0,
                  ymax: int = 0,
                  camera_only: bool = False):
    '''Set the boundaries of the border render and enable border render 

    :param xmin: X Min 
    :type xmin: int
    :param xmax: X Max 
    :type xmax: int
    :param ymin: Y Min 
    :type ymin: int
    :param ymax: Y Max 
    :type ymax: int
    :param camera_only: Camera Only, Set render border for camera view and final render only 
    :type camera_only: bool
    '''

    pass


def rotate():
    '''Rotate the view 

    '''

    pass


def ruler():
    '''Interactive ruler 

    '''

    pass


def select(extend: bool = False,
           deselect: bool = False,
           toggle: bool = False,
           center: bool = False,
           enumerate: bool = False,
           object: bool = False,
           location: int = (0, 0)):
    '''Activate/select item(s) 

    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: bool
    :param deselect: Deselect, Remove from selection 
    :type deselect: bool
    :param toggle: Toggle Selection, Toggle the selection 
    :type toggle: bool
    :param center: Center, Use the object center when selecting, in editmode used to extend object selection 
    :type center: bool
    :param enumerate: Enumerate, List objects under the mouse (object mode only) 
    :type enumerate: bool
    :param object: Object, Use object selection (editmode only) 
    :type object: bool
    :param location: Location, Mouse location 
    :type location: int
    '''

    pass


def select_border(gesture_mode: int = 0,
                  xmin: int = 0,
                  xmax: int = 0,
                  ymin: int = 0,
                  ymax: int = 0,
                  extend: bool = True):
    '''Select items using border selection 

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
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: bool
    '''

    pass


def select_circle(x: int = 0,
                  y: int = 0,
                  radius: int = 1,
                  gesture_mode: int = 0):
    '''Select items using circle selection 

    :param x: X 
    :type x: int
    :param y: Y 
    :type y: int
    :param radius: Radius 
    :type radius: int
    :param gesture_mode: Event Type 
    :type gesture_mode: int
    '''

    pass


def select_lasso(path: typing.List['bpy.types.OperatorMousePath'] = None,
                 deselect: bool = False,
                 extend: bool = True):
    '''Select items using lasso selection 

    :param path: Path 
    :type path: typing.List['bpy.types.OperatorMousePath']
    :param deselect: Deselect, Deselect rather than select items 
    :type deselect: bool
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: bool
    '''

    pass


def select_menu(name: int = '', toggle: bool = False):
    '''Menu object selection 

    :param name: Object Name 
    :type name: int
    :param toggle: Toggle, Toggle selection instead of deselecting everything first 
    :type toggle: bool
    '''

    pass


def select_or_deselect_all(extend: bool = False,
                           toggle: bool = False,
                           deselect: bool = False,
                           center: bool = False,
                           enumerate: bool = False,
                           object: bool = False):
    '''Select element under the mouse, deselect everything is there’s nothing under the mouse 

    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: bool
    :param toggle: Toggle, Toggle the selection 
    :type toggle: bool
    :param deselect: Deselect, Remove from selection 
    :type deselect: bool
    :param center: Center, Use the object center when selecting, in editmode used to extend object selection 
    :type center: bool
    :param enumerate: Enumerate, List objects under the mouse (object mode only) 
    :type enumerate: bool
    :param object: Object, Use object selection (editmode only) 
    :type object: bool
    '''

    pass


def smoothview():
    '''Undocumented 

    '''

    pass


def snap_cursor_to_active():
    '''Snap cursor to active item 

    '''

    pass


def snap_cursor_to_center():
    '''Snap cursor to the Center 

    '''

    pass


def snap_cursor_to_grid():
    '''Snap cursor to nearest grid division 

    '''

    pass


def snap_cursor_to_selected():
    '''Snap cursor to center of selected item(s) 

    '''

    pass


def snap_selected_to_active():
    '''Snap selected item(s) to the active item 

    '''

    pass


def snap_selected_to_cursor(use_offset: bool = True):
    '''Snap selected item(s) to cursor 

    :param use_offset: Offset 
    :type use_offset: bool
    '''

    pass


def snap_selected_to_grid():
    '''Snap selected item(s) to nearest grid division 

    '''

    pass


def toggle_render():
    '''Toggle rendered shading mode of the viewport 

    '''

    pass


def toolshelf():
    '''Toggles tool shelf display 

    '''

    pass


def view_all(use_all_regions: bool = False, center: bool = False):
    '''View all objects in scene 

    :param use_all_regions: All Regions, View selected for all regions 
    :type use_all_regions: bool
    :param center: Center 
    :type center: bool
    '''

    pass


def view_center_camera():
    '''Center the camera view 

    '''

    pass


def view_center_cursor():
    '''Center the view so that the cursor is in the middle of the view 

    '''

    pass


def view_center_lock():
    '''Center the view lock offset 

    '''

    pass


def view_center_pick():
    '''Center the view to the Z-depth position under the mouse cursor 

    '''

    pass


def view_lock_clear():
    '''Clear all view locking 

    '''

    pass


def view_lock_to_active():
    '''Lock the view to the active object/bone 

    '''

    pass


def view_orbit(angle: float = 0.0, type: int = 'ORBITLEFT'):
    '''Orbit the view 

    :param angle: Roll 
    :type angle: float
    :param type: Orbit, Direction of View OrbitORBITLEFT Orbit Left, Orbit the view around to the Left.ORBITRIGHT Orbit Right, Orbit the view around to the Right.ORBITUP Orbit Up, Orbit the view Up.ORBITDOWN Orbit Down, Orbit the view Down. 
    :type type: int
    '''

    pass


def view_pan(type: int = 'PANLEFT'):
    '''Pan the view 

    :param type: Pan, Direction of View PanPANLEFT Pan Left, Pan the view to the Left.PANRIGHT Pan Right, Pan the view to the Right.PANUP Pan Up, Pan the view Up.PANDOWN Pan Down, Pan the view Down. 
    :type type: int
    '''

    pass


def view_persportho():
    '''Switch the current view from perspective/orthographic projection 

    '''

    pass


def view_roll(angle: float = 0.0, type: int = 'ANGLE'):
    '''Roll the view 

    :param angle: Roll 
    :type angle: float
    :param type: Roll Angle Source, How roll angle is calculatedANGLE Roll Angle, Roll the view using an angle value.LEFT Roll Left, Roll the view around to the Left.RIGHT Roll Right, Roll the view around to the Right. 
    :type type: int
    '''

    pass


def view_selected(use_all_regions: bool = False):
    '''Move the view to the selection center 

    :param use_all_regions: All Regions, View selected for all regions 
    :type use_all_regions: bool
    '''

    pass


def viewnumpad(type: int = 'LEFT', align_active: bool = False):
    '''Use a preset viewpoint 

    :param type: View, Preset viewpoint to useLEFT Left, View From the Left.RIGHT Right, View From the Right.BOTTOM Bottom, View From the Bottom.TOP Top, View From the Top.FRONT Front, View From the Front.BACK Back, View From the Back.CAMERA Camera, View From the Active Camera. 
    :type type: int
    :param align_active: Align Active, Align to the active object’s axis 
    :type align_active: bool
    '''

    pass


def walk():
    '''Interactively walk around the scene 

    '''

    pass


def zoom(delta: int = 0, mx: int = 0, my: int = 0):
    '''Zoom in/out in the view 

    :param delta: Delta 
    :type delta: int
    :param mx: Zoom Position X 
    :type mx: int
    :param my: Zoom Position Y 
    :type my: int
    '''

    pass


def zoom_border(gesture_mode: int = 0,
                xmin: int = 0,
                xmax: int = 0,
                ymin: int = 0,
                ymax: int = 0):
    '''Zoom in the view to the nearest object contained in the border 

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


def zoom_camera_1_to_1():
    '''Match the camera to 1:1 to the render output 

    '''

    pass
