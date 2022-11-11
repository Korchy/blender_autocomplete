import sys
import typing

GenericType = typing.TypeVar("GenericType")


class KDTree:
    ''' KdTree(size) -> new kd-tree initialized to hold size items.
    '''

    def balance(self):
        ''' Balance the tree.

        '''
        pass

    def find(self, co: typing.Tuple[float], filter=None) -> typing.Tuple:
        ''' Find nearest point to co .

        :param co: 3d coordinates.
        :type co: typing.Tuple[float]
        :param filter: function which takes an index and returns True for indices to include in the search.
        :type filter: 
        :rtype: typing.Tuple
        :return: Vector , index, distance).
        '''
        pass

    def find_n(self, co: typing.Tuple[float], n: int) -> typing.List:
        ''' Find nearest n points to co .

        :param co: 3d coordinates.
        :type co: typing.Tuple[float]
        :param n: Number of points to find.
        :type n: int
        :rtype: typing.List
        :return: Vector , index, distance).
        '''
        pass

    def find_range(self, co: typing.Tuple[float],
                   radius: float) -> typing.List:
        ''' Find all points within radius of co .

        :param co: 3d coordinates.
        :type co: typing.Tuple[float]
        :param radius: Distance to search for points.
        :type radius: float
        :rtype: typing.List
        :return: Vector , index, distance).
        '''
        pass

    def insert(self, co: typing.Tuple[float], index: int):
        ''' Insert a point into the KDTree.

        :param co: Point 3d position.
        :type co: typing.Tuple[float]
        :param index: The index of the point.
        :type index: int
        '''
        pass

    def __init__(self, size):
        ''' 

        '''
        pass
