import sys
import typing


def attribute_add(name: str = "Attribute",
                  data_type: typing.Union[str, int] = 'FLOAT',
                  domain: typing.Union[str, int] = 'POINT'):
    ''' Add attribute to geometry

    :param name: Name, Name of new attribute
    :type name: str
    :param data_type: Data Type, Type of data stored in attribute * FLOAT Float, Floating point value. * INT Integer, 32 bit integer. * FLOAT_VECTOR Vector, 3D vector with floating point values. * FLOAT_COLOR Float Color, RGBA color with floating point precisions. * BYTE_COLOR Byte Color, RGBA color with 8-bit precision. * STRING String, Text string.
    :type data_type: typing.Union[str, int]
    :param domain: Domain, Type of element that attribute is stored on * VERTEX Vertex, Attribute on mesh vertex. * EDGE Edge, Attribute on mesh edge. * CORNER Corner, Attribute on mesh polygon corner. * POLYGON Polygon, Attribute on mesh polygons. * POINT Point, Attribute on point. * CURVE Curve, Attribute on hair curve.
    :type domain: typing.Union[str, int]
    '''

    pass


def attribute_remove():
    ''' Remove attribute from geometry

    '''

    pass
