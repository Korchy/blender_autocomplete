import sys
import typing
import mathutils


class BVHTree:

    @classmethod
    def FromPolygons(
            cls, vertices, polygons, all_triangles: bool = False, epsilon: float = 0.0
    ):
        """BVH tree constructed geometry passed in as arguments.

        :param vertices: float triplets each representing (x, y, z)
        :param polygons: Sequence of polyugons, each containing indices to the vertices argument.
        :param all_triangles: Use when all polygons are triangles for more efficient conversion.
        :type all_triangles: bool
        :param epsilon: Increase the threshold for detecting overlap and raycast hits.
        :type epsilon: float
        """
        pass

    def find_nearest(self, origin, distance: float = 1.84467e+19):
        '''Find the nearest element (typically face index) to a point. 

        :param co: Find nearest element to this point. 
        :type co: 'mathutils.Vector'
        :param distance: Maximum distance threshold. 
        :type distance: float
        :return:  Returns a tuple (Vector location, Vector normal, int index, float distance), Values will all be None if no hit is found. 
        '''
        pass

    def find_nearest_range(self, origin,
                           distance: float = 1.84467e+19) -> list:
        '''Find the nearest elements (typically face index) to a point in the distance range. 

        :param co: Find nearest elements to this point. 
        :type co: 'mathutils.Vector'
        :param distance: Maximum distance threshold. 
        :type distance: float
        :rtype: list
        :return:  Returns a list of tuples (Vector location, Vector normal, int index, float distance), 
        '''
        pass

    def overlap(self, other_tree: 'BVHTree') -> list:
        '''Find overlapping indices between 2 trees. 

        :param other_tree: Other tree to preform overlap test on. 
        :type other_tree: 'BVHTree'
        :rtype: list
        :return:  Returns a list of unique index pairs, the first index referencing this tree, the second referencing the other_tree. 
        '''
        pass

    def ray_cast(self,
                 origin,
                 direction: 'mathutils.Vector',
                 distance: float = sys.float_info.max):
        '''Cast a ray onto the mesh. 

        :param co: Start location of the ray in object space. 
        :type co: 'mathutils.Vector'
        :param direction: Direction of the ray in object space. 
        :type direction: 'mathutils.Vector'
        :param distance: Maximum distance threshold. 
        :type distance: float
        :return:  Returns a tuple (Vector location, Vector normal, int index, float distance), Values will all be None if no hit is found. 
        '''
        pass

    def __init__(self, size):
        '''

        '''
        pass
