import sys
import typing


def attribute_add(name: str = "Attribute",
                  domain: typing.Union[str, int] = 'POINT',
                  data_type: typing.Union[str, int] = 'FLOAT'):
    ''' Add attribute to geometry

    :param name: Name, Name of new attribute
    :type name: str
    :param domain: Domain, Type of element that attribute is stored on * POINT Point -- Attribute on point. * EDGE Edge -- Attribute on mesh edge. * FACE Face -- Attribute on mesh faces. * CORNER Face Corner -- Attribute on mesh face corner. * CURVE Spline -- Attribute on spline. * INSTANCE Instance -- Attribute on instance.
    :type domain: typing.Union[str, int]
    :param data_type: Data Type, Type of data stored in attribute * FLOAT Float -- Floating-point value. * INT Integer -- 32-bit integer. * FLOAT_VECTOR Vector -- 3D vector with floating-point values. * FLOAT_COLOR Color -- RGBA color with 32-bit floating-point values. * BYTE_COLOR Byte Color -- RGBA color with 8-bit positive integer values. * STRING String -- Text string. * BOOLEAN Boolean -- True or false. * FLOAT2 2D Vector -- 2D vector with floating-point values. * INT8 8-Bit Integer -- Smaller integer with a range from -128 to 127.
    :type data_type: typing.Union[str, int]
    '''

    pass


def attribute_convert(mode: typing.Union[str, int] = 'GENERIC',
                      domain: typing.Union[str, int] = 'POINT',
                      data_type: typing.Union[str, int] = 'FLOAT'):
    ''' Change how the attribute is stored

    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param domain: Domain, Which geometry element to move the attribute to * POINT Point -- Attribute on point. * EDGE Edge -- Attribute on mesh edge. * FACE Face -- Attribute on mesh faces. * CORNER Face Corner -- Attribute on mesh face corner. * CURVE Spline -- Attribute on spline. * INSTANCE Instance -- Attribute on instance.
    :type domain: typing.Union[str, int]
    :param data_type: Data Type * FLOAT Float -- Floating-point value. * INT Integer -- 32-bit integer. * FLOAT_VECTOR Vector -- 3D vector with floating-point values. * FLOAT_COLOR Color -- RGBA color with 32-bit floating-point values. * BYTE_COLOR Byte Color -- RGBA color with 8-bit positive integer values. * STRING String -- Text string. * BOOLEAN Boolean -- True or false. * FLOAT2 2D Vector -- 2D vector with floating-point values. * INT8 8-Bit Integer -- Smaller integer with a range from -128 to 127.
    :type data_type: typing.Union[str, int]
    '''

    pass


def attribute_remove():
    ''' Remove attribute from geometry

    '''

    pass


def color_attribute_add(name: str = "Color",
                        domain: typing.Union[str, int] = 'POINT',
                        data_type: typing.Union[str, int] = 'COLOR',
                        color: typing.List[float] = (0.0, 0.0, 0.0, 1.0)):
    ''' Add color attribute to geometry

    :param name: Name, Name of new color attribute
    :type name: str
    :param domain: Domain, Type of element that attribute is stored on
    :type domain: typing.Union[str, int]
    :param data_type: Data Type, Type of data stored in attribute
    :type data_type: typing.Union[str, int]
    :param color: Color, Default fill color
    :type color: typing.List[float]
    '''

    pass


def color_attribute_remove():
    ''' Remove color attribute from geometry

    '''

    pass


def color_attribute_render_set(name: str = "Color"):
    ''' Set default color attribute used for rendering

    :param name: Name, Name of color attribute
    :type name: str
    '''

    pass
