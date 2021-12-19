import sys
import typing


def attribute_add(name: str = "Attribute",
                  domain: typing.Union[int, str] = 'POINT',
                  data_type: typing.Union[int, str] = 'FLOAT'):
    ''' Add attribute to geometry

    :param name: Name, Name of new attribute
    :type name: str
    :param domain: Domain, Type of element that attribute is stored on * POINT Point -- Attribute on point. * EDGE Edge -- Attribute on mesh edge. * FACE Face -- Attribute on mesh faces. * CORNER Face Corner -- Attribute on mesh face corner. * CURVE Spline -- Attribute on spline.
    :type domain: typing.Union[int, str]
    :param data_type: Data Type, Type of data stored in attribute * FLOAT Float -- Floating-point value. * INT Integer -- 32-bit integer. * FLOAT_VECTOR Vector -- 3D vector with floating-point values. * FLOAT_COLOR Color -- RGBA color with floating-point values. * BYTE_COLOR Byte Color -- RGBA color with 8-bit values. * STRING String -- Text string. * BOOLEAN Boolean -- True or false. * FLOAT2 2D Vector -- 2D vector with floating-point values.
    :type data_type: typing.Union[int, str]
    '''

    pass


def attribute_remove():
    ''' Remove attribute from geometry

    '''

    pass
