import sys
import typing


def delete():
    '''Delete active scene 

    '''

    pass


def freestyle_add_edge_marks_to_keying_set():
    '''Add the data paths to the Freestyle Edge Mark property of selected edges to the active keying set 

    '''

    pass


def freestyle_add_face_marks_to_keying_set():
    '''Add the data paths to the Freestyle Face Mark property of selected polygons to the active keying set 

    '''

    pass


def freestyle_alpha_modifier_add(type: int = 'ALONG_STROKE'):
    '''Add an alpha transparency modifier to the line style associated with the active lineset 

    :param type: Type 
    :type type: int
    '''

    pass


def freestyle_color_modifier_add(type: int = 'ALONG_STROKE'):
    '''Add a line color modifier to the line style associated with the active lineset 

    :param type: Type 
    :type type: int
    '''

    pass


def freestyle_fill_range_by_selection(type: int = 'COLOR', name: str = ""):
    '''Fill the Range Min/Max entries by the min/max distance between selected mesh objects and the source object 

    :param type: Type, Type of the modifier to work onCOLOR Color, Color modifier type.ALPHA Alpha, Alpha modifier type.THICKNESS Thickness, Thickness modifier type. 
    :type type: int
    :param name: Name, Name of the modifier to work on 
    :type name: str
    '''

    pass


def freestyle_geometry_modifier_add(type: int = '2D_OFFSET'):
    '''Add a stroke geometry modifier to the line style associated with the active lineset 

    :param type: Type 
    :type type: int
    '''

    pass


def freestyle_lineset_add():
    '''Add a line set into the list of line sets 

    '''

    pass


def freestyle_lineset_copy():
    '''Copy the active line set to a buffer 

    '''

    pass


def freestyle_lineset_move(direction: int = 'UP'):
    '''Change the position of the active line set within the list of line sets 

    :param direction: Direction, Direction to move the active line set towards 
    :type direction: int
    '''

    pass


def freestyle_lineset_paste():
    '''Paste the buffer content to the active line set 

    '''

    pass


def freestyle_lineset_remove():
    '''Remove the active line set from the list of line sets 

    '''

    pass


def freestyle_linestyle_new():
    '''Create a new line style, reusable by multiple line sets 

    '''

    pass


def freestyle_modifier_copy():
    '''Duplicate the modifier within the list of modifiers 

    '''

    pass


def freestyle_modifier_move(direction: int = 'UP'):
    '''Move the modifier within the list of modifiers 

    :param direction: Direction, Direction to move the chosen modifier towards 
    :type direction: int
    '''

    pass


def freestyle_modifier_remove():
    '''Remove the modifier from the list of modifiers 

    '''

    pass


def freestyle_module_add():
    '''Add a style module into the list of modules 

    '''

    pass


def freestyle_module_move(direction: int = 'UP'):
    '''Change the position of the style module within in the list of style modules 

    :param direction: Direction, Direction to move the chosen style module towards 
    :type direction: int
    '''

    pass


def freestyle_module_open(filepath: str = "", make_internal: bool = True):
    '''Open a style module file 

    :param filepath: filepath 
    :type filepath: str
    :param make_internal: Make internal, Make module file internal after loading 
    :type make_internal: bool
    '''

    pass


def freestyle_module_remove():
    '''Remove the style module from the stack 

    '''

    pass


def freestyle_stroke_material_create():
    '''Create Freestyle stroke material for testing 

    '''

    pass


def freestyle_thickness_modifier_add(type: int = 'ALONG_STROKE'):
    '''Add a line thickness modifier to the line style associated with the active lineset 

    :param type: Type 
    :type type: int
    '''

    pass


def new(type: int = 'NEW'):
    '''Add new scene by type 

    :param type: TypeNEW New, Add new scene.EMPTY Copy Settings, Make a copy without any objects.LINK_OBJECTS Link Objects, Link to the objects from the current scene.LINK_OBJECT_DATA Link Object Data, Copy objects linked to data from the current scene.FULL_COPY Full Copy, Make a full copy of the current scene. 
    :type type: int
    '''

    pass


def render_layer_add():
    '''Add a render layer 

    '''

    pass


def render_layer_remove():
    '''Remove the selected render layer 

    '''

    pass


def render_view_add():
    '''Add a render view 

    '''

    pass


def render_view_remove():
    '''Remove the selected render view 

    '''

    pass


def units_length_preset_add(name: str = "", remove_active: bool = False):
    '''Add or remove length units preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: str
    :param remove_active: remove_active 
    :type remove_active: bool
    '''

    pass
