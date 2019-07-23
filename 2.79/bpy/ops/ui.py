import sys
import typing


def copy_data_path_button(full_path: bool = False):
    '''Copy the RNA data path for this property to the clipboard 

    :param full_path: full_path, Copy full data path 
    :type full_path: bool
    '''

    pass


def copy_python_command_button():
    '''Copy the Python command matching this button 

    '''

    pass


def copy_to_selected_button(all: bool = True):
    '''Copy property from this object to selected objects or bones 

    :param all: All, Copy to selected all elements of the array 
    :type all: bool
    '''

    pass


def drop_color(color: float = (0.0, 0.0, 0.0), gamma: bool = False):
    '''Drop colors to buttons 

    :param color: Color, Source color 
    :type color: float
    :param gamma: Gamma Corrected, The source color is gamma corrected 
    :type gamma: bool
    '''

    pass


def editsource():
    '''Edit UI source code of the active button 

    '''

    pass


def edittranslation_init():
    '''Edit i18n in current language for the active button 

    '''

    pass


def eyedropper_color():
    '''Sample a color from the Blender Window to store in a property 

    '''

    pass


def eyedropper_depth():
    '''Sample depth from the 3D view 

    '''

    pass


def eyedropper_driver(mapping_type: int = 'SINGLE_MANY'):
    '''Pick a property to use as a driver target 

    :param mapping_type: Mapping Type, Method used to match target and driven propertiesSINGLE_MANY All from Target, Drive all components of this property using the target picked.DIRECT Single from Target, Drive this component of this property using the target picked.MATCH Match Indices, Create drivers for each pair of corresponding elements.NONE_ALL Manually Create Later, Create drivers for all properties without assigning any targets yet.NONE_SINGLE Manually Create Later (Single), Create driver for this property only and without assigning any targets yet. 
    :type mapping_type: int
    '''

    pass


def eyedropper_id():
    '''Sample a data-block from the 3D View to store in a property 

    '''

    pass


def reloadtranslation():
    '''Force a full reload of UI translation 

    '''

    pass


def reports_to_textblock():
    '''Write the reports 

    '''

    pass


def reset_default_button(all: bool = True):
    '''Reset this property’s value to its default value 

    :param all: All, Reset to default values all elements of the array 
    :type all: bool
    '''

    pass


def reset_default_theme():
    '''Reset to the default theme colors 

    '''

    pass


def unset_property_button():
    '''Clear the property and use default or generated value in operators 

    '''

    pass
