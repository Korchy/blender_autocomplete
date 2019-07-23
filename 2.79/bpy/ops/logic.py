import sys
import typing
import bpy


def actuator_add(type: int = '', name: str = "", object: str = ""):
    '''Add an actuator to the active object 

    :param type: Type, Type of actuator to add 
    :type type: int
    :param name: Name, Name of the Actuator to add 
    :type name: str
    :param object: Object, Name of the Object to add the Actuator to 
    :type object: str
    '''

    pass


def actuator_move(actuator: str = "", object: str = "", direction: int = 'UP'):
    '''Move Actuator 

    :param actuator: Actuator, Name of the actuator to edit 
    :type actuator: str
    :param object: Object, Name of the object the actuator belongs to 
    :type object: str
    :param direction: Direction, Move Up or Down 
    :type direction: int
    '''

    pass


def actuator_remove(actuator: str = "", object: str = ""):
    '''Remove an actuator from the active object 

    :param actuator: Actuator, Name of the actuator to edit 
    :type actuator: str
    :param object: Object, Name of the object the actuator belongs to 
    :type object: str
    '''

    pass


def controller_add(type: int = 'LOGIC_AND', name: str = "", object: str = ""):
    '''Add a controller to the active object 

    :param type: Type, Type of controller to addLOGIC_AND And, Logic And.LOGIC_OR Or, Logic Or.LOGIC_NAND Nand, Logic Nand.LOGIC_NOR Nor, Logic Nor.LOGIC_XOR Xor, Logic Xor.LOGIC_XNOR Xnor, Logic Xnor.EXPRESSION Expression.PYTHON Python. 
    :type type: int
    :param name: Name, Name of the Controller to add 
    :type name: str
    :param object: Object, Name of the Object to add the Controller to 
    :type object: str
    '''

    pass


def controller_move(controller: str = "",
                    object: str = "",
                    direction: int = 'UP'):
    '''Move Controller 

    :param controller: Controller, Name of the controller to edit 
    :type controller: str
    :param object: Object, Name of the object the controller belongs to 
    :type object: str
    :param direction: Direction, Move Up or Down 
    :type direction: int
    '''

    pass


def controller_remove(controller: str = "", object: str = ""):
    '''Remove a controller from the active object 

    :param controller: Controller, Name of the controller to edit 
    :type controller: str
    :param object: Object, Name of the object the controller belongs to 
    :type object: str
    '''

    pass


def links_cut(path: typing.List['bpy.types.OperatorMousePath'] = None,
              cursor: int = 9):
    '''Remove logic brick connections 

    :param path: path 
    :type path: typing.List['bpy.types.OperatorMousePath']
    :param cursor: Cursor 
    :type cursor: int
    '''

    pass


def properties():
    '''Toggle the properties region visibility 

    '''

    pass


def sensor_add(type: int = '', name: str = "", object: str = ""):
    '''Add a sensor to the active object 

    :param type: Type, Type of sensor to add 
    :type type: int
    :param name: Name, Name of the Sensor to add 
    :type name: str
    :param object: Object, Name of the Object to add the Sensor to 
    :type object: str
    '''

    pass


def sensor_move(sensor: str = "", object: str = "", direction: int = 'UP'):
    '''Move Sensor 

    :param sensor: Sensor, Name of the sensor to edit 
    :type sensor: str
    :param object: Object, Name of the object the sensor belongs to 
    :type object: str
    :param direction: Direction, Move Up or Down 
    :type direction: int
    '''

    pass


def sensor_remove(sensor: str = "", object: str = ""):
    '''Remove a sensor from the active object 

    :param sensor: Sensor, Name of the sensor to edit 
    :type sensor: str
    :param object: Object, Name of the object the sensor belongs to 
    :type object: str
    '''

    pass


def view_all():
    '''Resize view so you can see all logic bricks 

    '''

    pass
