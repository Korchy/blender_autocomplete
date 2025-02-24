"""
The Blender geometry module

"""

import typing
import collections.abc
import typing_extensions
import mathutils

def area_tri(
    v1: collections.abc.Sequence[float] | mathutils.Vector,
    v2: collections.abc.Sequence[float] | mathutils.Vector,
    v3: collections.abc.Sequence[float] | mathutils.Vector,
) -> float:
    """Returns the area size of the 2D or 3D triangle defined.

    :param v1: Point1
    :type v1: collections.abc.Sequence[float] | mathutils.Vector
    :param v2: Point2
    :type v2: collections.abc.Sequence[float] | mathutils.Vector
    :param v3: Point3
    :type v3: collections.abc.Sequence[float] | mathutils.Vector
    :rtype: float
    """

def barycentric_transform(
    point: collections.abc.Sequence[float] | mathutils.Vector,
    tri_a1: collections.abc.Sequence[float] | mathutils.Vector,
    tri_a2: collections.abc.Sequence[float] | mathutils.Vector,
    tri_a3: collections.abc.Sequence[float] | mathutils.Vector,
    tri_b1: collections.abc.Sequence[float] | mathutils.Vector,
    tri_b2: collections.abc.Sequence[float] | mathutils.Vector,
    tri_b3: collections.abc.Sequence[float] | mathutils.Vector,
) -> mathutils.Vector:
    """Return a transformed point, the transformation is defined by 2 triangles.

    :param point: The point to transform.
    :type point: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_a1: source triangle vertex.
    :type tri_a1: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_a2: source triangle vertex.
    :type tri_a2: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_a3: source triangle vertex.
    :type tri_a3: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_b1: target triangle vertex.
    :type tri_b1: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_b2: target triangle vertex.
    :type tri_b2: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_b3: target triangle vertex.
    :type tri_b3: collections.abc.Sequence[float] | mathutils.Vector
    :return: The transformed point
    :rtype: mathutils.Vector
    """

def box_fit_2d(
    points: collections.abc.Sequence[collections.abc.Sequence[float]],
) -> float:
    """Returns an angle that best fits the points to an axis aligned rectangle

    :param points: Sequence of 2D points.
    :type points: collections.abc.Sequence[collections.abc.Sequence[float]]
    :return: angle
    :rtype: float
    """

def box_pack_2d(
    boxes: list[list[float, float, float, float, ...]],
) -> tuple[float, float]:
    """Returns a tuple with the width and height of the packed bounding box.

    :param boxes: list of boxes, each box is a list where the first 4 items are [X, Y, width, height, ...] other items are ignored. The X & Y values in this list are modified to set the packed positions.
    :type boxes: list[list[float, float, float, float, ...]]
    :return: The width and height of the packed bounding box.
    :rtype: tuple[float, float]
    """

def closest_point_on_tri(
    pt: collections.abc.Sequence[float] | mathutils.Vector,
    tri_p1: collections.abc.Sequence[float] | mathutils.Vector,
    tri_p2: collections.abc.Sequence[float] | mathutils.Vector,
    tri_p3: collections.abc.Sequence[float] | mathutils.Vector,
) -> mathutils.Vector:
    """Takes 4 vectors: one is the point and the next 3 define the triangle.

    :param pt: Point
    :type pt: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_p1: First point of the triangle
    :type tri_p1: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_p2: Second point of the triangle
    :type tri_p2: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_p3: Third point of the triangle
    :type tri_p3: collections.abc.Sequence[float] | mathutils.Vector
    :return: The closest point of the triangle.
    :rtype: mathutils.Vector
    """

def convex_hull_2d(
    points: collections.abc.Sequence[collections.abc.Sequence[float]],
) -> list[int]:
    """Returns a list of indices into the list given

    :param points: Sequence of 2D points.
    :type points: collections.abc.Sequence[collections.abc.Sequence[float]]
    :return: a list of indices
    :rtype: list[int]
    """

def delaunay_2d_cdt(
    vert_coords: collections.abc.Sequence[
        collections.abc.Sequence[float] | mathutils.Vector
    ],
    edges: collections.abc.Sequence[collections.abc.Sequence[int, int]],
    faces: collections.abc.Sequence[collections.abc.Sequence[int]],
    output_type: int,
    epsilon: float,
    need_ids=True,
) -> tuple[
    list[mathutils.Vector],
    list[tuple[int, int]],
    list[list[int]],
    list[list[int]],
    list[list[int]],
    list[list[int]],
]:
    """Computes the Constrained Delaunay Triangulation of a set of vertices,
    with edges and faces that must appear in the triangulation.
    Some triangles may be eaten away, or combined with other triangles,
    according to output type.
    The returned verts may be in a different order from input verts, may be moved
    slightly, and may be merged with other nearby verts.
    The three returned orig lists give, for each of verts, edges, and faces, the list of
    input element indices corresponding to the positionally same output element.
    For edges, the orig indices start with the input edges and then continue
    with the edges implied by each of the faces (n of them for an n-gon).
    If the need_ids argument is supplied, and False, then the code skips the preparation
    of the orig arrays, which may save some time.

        :param vert_coords: Vertex coordinates (2d)
        :type vert_coords: collections.abc.Sequence[collections.abc.Sequence[float] | mathutils.Vector]
        :param edges: Edges, as pairs of indices in vert_coords
        :type edges: collections.abc.Sequence[collections.abc.Sequence[int, int]]
        :param faces: Faces, each sublist is a face, as indices in vert_coords (CCW oriented)
        :type faces: collections.abc.Sequence[collections.abc.Sequence[int]]
        :param output_type: What output looks like. 0 => triangles with convex hull. 1 => triangles inside constraints. 2 => the input constraints, intersected. 3 => like 2 but detect holes and omit them from output. 4 => like 2 but with extra edges to make valid BMesh faces. 5 => like 4 but detect holes and omit them from output.
        :type output_type: int
        :param epsilon: For nearness tests; should not be zero
        :type epsilon: float
        :param need_ids: are the orig output arrays needed?
        :return: Output tuple, (vert_coords, edges, faces, orig_verts, orig_edges, orig_faces)
        :rtype: tuple[list[mathutils.Vector], list[tuple[int, int]], list[list[int]], list[list[int]], list[list[int]], list[list[int]]]
    """

def distance_point_to_plane(
    pt: collections.abc.Sequence[float] | mathutils.Vector,
    plane_co: collections.abc.Sequence[float] | mathutils.Vector,
    plane_no: collections.abc.Sequence[float] | mathutils.Vector,
) -> float:
    """Returns the signed distance between a point and a plane    (negative when below the normal).

    :param pt: Point
    :type pt: collections.abc.Sequence[float] | mathutils.Vector
    :param plane_co: A point on the plane
    :type plane_co: collections.abc.Sequence[float] | mathutils.Vector
    :param plane_no: The direction the plane is facing
    :type plane_no: collections.abc.Sequence[float] | mathutils.Vector
    :rtype: float
    """

def interpolate_bezier(
    knot1: collections.abc.Sequence[float] | mathutils.Vector,
    handle1: collections.abc.Sequence[float] | mathutils.Vector,
    handle2: collections.abc.Sequence[float] | mathutils.Vector,
    knot2: collections.abc.Sequence[float] | mathutils.Vector,
    resolution: int,
) -> list[mathutils.Vector]:
    """Interpolate a bezier spline segment.

    :param knot1: First bezier spline point.
    :type knot1: collections.abc.Sequence[float] | mathutils.Vector
    :param handle1: First bezier spline handle.
    :type handle1: collections.abc.Sequence[float] | mathutils.Vector
    :param handle2: Second bezier spline handle.
    :type handle2: collections.abc.Sequence[float] | mathutils.Vector
    :param knot2: Second bezier spline point.
    :type knot2: collections.abc.Sequence[float] | mathutils.Vector
    :param resolution: Number of points to return.
    :type resolution: int
    :return: The interpolated points.
    :rtype: list[mathutils.Vector]
    """

def intersect_line_line(
    v1: collections.abc.Sequence[float] | mathutils.Vector,
    v2: collections.abc.Sequence[float] | mathutils.Vector,
    v3: collections.abc.Sequence[float] | mathutils.Vector,
    v4: collections.abc.Sequence[float] | mathutils.Vector,
) -> None | tuple[mathutils.Vector, mathutils.Vector]:
    """Returns a tuple with the points on each line respectively closest to the other.

    :param v1: First point of the first line
    :type v1: collections.abc.Sequence[float] | mathutils.Vector
    :param v2: Second point of the first line
    :type v2: collections.abc.Sequence[float] | mathutils.Vector
    :param v3: First point of the second line
    :type v3: collections.abc.Sequence[float] | mathutils.Vector
    :param v4: Second point of the second line
    :type v4: collections.abc.Sequence[float] | mathutils.Vector
    :return: The intersection on each line or None when the lines are co-linear.
    :rtype: None | tuple[mathutils.Vector, mathutils.Vector]
    """

def intersect_line_line_2d(
    lineA_p1: collections.abc.Sequence[float] | mathutils.Vector,
    lineA_p2: collections.abc.Sequence[float] | mathutils.Vector,
    lineB_p1: collections.abc.Sequence[float] | mathutils.Vector,
    lineB_p2: collections.abc.Sequence[float] | mathutils.Vector,
) -> None | mathutils.Vector:
    """Takes 2 segments (defined by 4 vectors) and returns a vector for their point of intersection or None.

    :param lineA_p1: First point of the first line
    :type lineA_p1: collections.abc.Sequence[float] | mathutils.Vector
    :param lineA_p2: Second point of the first line
    :type lineA_p2: collections.abc.Sequence[float] | mathutils.Vector
    :param lineB_p1: First point of the second line
    :type lineB_p1: collections.abc.Sequence[float] | mathutils.Vector
    :param lineB_p2: Second point of the second line
    :type lineB_p2: collections.abc.Sequence[float] | mathutils.Vector
    :return: The point of intersection or None when not found
    :rtype: None | mathutils.Vector
    """

def intersect_line_plane(
    line_a: collections.abc.Sequence[float] | mathutils.Vector,
    line_b: collections.abc.Sequence[float] | mathutils.Vector,
    plane_co: collections.abc.Sequence[float] | mathutils.Vector,
    plane_no: collections.abc.Sequence[float] | mathutils.Vector,
    no_flip=False,
) -> None | mathutils.Vector:
    """Calculate the intersection between a line (as 2 vectors) and a plane.
    Returns a vector for the intersection or None.

        :param line_a: First point of the first line
        :type line_a: collections.abc.Sequence[float] | mathutils.Vector
        :param line_b: Second point of the first line
        :type line_b: collections.abc.Sequence[float] | mathutils.Vector
        :param plane_co: A point on the plane
        :type plane_co: collections.abc.Sequence[float] | mathutils.Vector
        :param plane_no: The direction the plane is facing
        :type plane_no: collections.abc.Sequence[float] | mathutils.Vector
        :return: The point of intersection or None when not found
        :rtype: None | mathutils.Vector
    """

def intersect_line_sphere(
    line_a: collections.abc.Sequence[float] | mathutils.Vector,
    line_b: collections.abc.Sequence[float] | mathutils.Vector,
    sphere_co: collections.abc.Sequence[float] | mathutils.Vector,
    sphere_radius: float,
    clip=True,
) -> tuple[mathutils.Vector | None, mathutils.Vector | None]:
    """Takes a line (as 2 points) and a sphere (as a point and a radius) and
    returns the intersection

        :param line_a: First point of the line
        :type line_a: collections.abc.Sequence[float] | mathutils.Vector
        :param line_b: Second point of the line
        :type line_b: collections.abc.Sequence[float] | mathutils.Vector
        :param sphere_co: The center of the sphere
        :type sphere_co: collections.abc.Sequence[float] | mathutils.Vector
        :param sphere_radius: Radius of the sphere
        :type sphere_radius: float
        :return: The intersection points as a pair of vectors or None when there is no intersection
        :rtype: tuple[mathutils.Vector | None, mathutils.Vector | None]
    """

def intersect_line_sphere_2d(
    line_a: collections.abc.Sequence[float] | mathutils.Vector,
    line_b: collections.abc.Sequence[float] | mathutils.Vector,
    sphere_co: collections.abc.Sequence[float] | mathutils.Vector,
    sphere_radius: float,
    clip=True,
) -> tuple[mathutils.Vector | None, mathutils.Vector | None]:
    """Takes a line (as 2 points) and a sphere (as a point and a radius) and
    returns the intersection

        :param line_a: First point of the line
        :type line_a: collections.abc.Sequence[float] | mathutils.Vector
        :param line_b: Second point of the line
        :type line_b: collections.abc.Sequence[float] | mathutils.Vector
        :param sphere_co: The center of the sphere
        :type sphere_co: collections.abc.Sequence[float] | mathutils.Vector
        :param sphere_radius: Radius of the sphere
        :type sphere_radius: float
        :return: The intersection points as a pair of vectors or None when there is no intersection
        :rtype: tuple[mathutils.Vector | None, mathutils.Vector | None]
    """

def intersect_plane_plane(
    plane_a_co: collections.abc.Sequence[float] | mathutils.Vector,
    plane_a_no: collections.abc.Sequence[float] | mathutils.Vector,
    plane_b_co: collections.abc.Sequence[float] | mathutils.Vector,
    plane_b_no: collections.abc.Sequence[float] | mathutils.Vector,
) -> tuple[None, None] | tuple[mathutils.Vector, mathutils.Vector]:
    """Return the intersection between two planes

    :param plane_a_co: Point on the first plane
    :type plane_a_co: collections.abc.Sequence[float] | mathutils.Vector
    :param plane_a_no: Normal of the first plane
    :type plane_a_no: collections.abc.Sequence[float] | mathutils.Vector
    :param plane_b_co: Point on the second plane
    :type plane_b_co: collections.abc.Sequence[float] | mathutils.Vector
    :param plane_b_no: Normal of the second plane
    :type plane_b_no: collections.abc.Sequence[float] | mathutils.Vector
    :return: The line of the intersection represented as a point and a vector or None if the intersection can't be calculated
    :rtype: tuple[None, None] | tuple[mathutils.Vector, mathutils.Vector]
    """

def intersect_point_line(
    pt: collections.abc.Sequence[float] | mathutils.Vector,
    line_p1: collections.abc.Sequence[float] | mathutils.Vector,
    line_p2,
) -> tuple[mathutils.Vector, float]:
    """Takes a point and a line and returns a tuple with the closest point on the line and its distance from the first point of the line as a percentage of the length of the line.

    :param pt: Point
    :type pt: collections.abc.Sequence[float] | mathutils.Vector
    :param line_p1: First point of the lineSecond point of the line
    :type line_p1: collections.abc.Sequence[float] | mathutils.Vector
    :rtype: tuple[mathutils.Vector, float]
    """

def intersect_point_quad_2d(
    pt: collections.abc.Sequence[float] | mathutils.Vector,
    quad_p1: collections.abc.Sequence[float] | mathutils.Vector,
    quad_p2: collections.abc.Sequence[float] | mathutils.Vector,
    quad_p3: collections.abc.Sequence[float] | mathutils.Vector,
    quad_p4: collections.abc.Sequence[float] | mathutils.Vector,
) -> int:
    """Takes 5 vectors (using only the x and y coordinates): one is the point and the next 4 define the quad,
    only the x and y are used from the vectors. Returns 1 if the point is within the quad, otherwise 0.
    Works only with convex quads without singular edges.

        :param pt: Point
        :type pt: collections.abc.Sequence[float] | mathutils.Vector
        :param quad_p1: First point of the quad
        :type quad_p1: collections.abc.Sequence[float] | mathutils.Vector
        :param quad_p2: Second point of the quad
        :type quad_p2: collections.abc.Sequence[float] | mathutils.Vector
        :param quad_p3: Third point of the quad
        :type quad_p3: collections.abc.Sequence[float] | mathutils.Vector
        :param quad_p4: Fourth point of the quad
        :type quad_p4: collections.abc.Sequence[float] | mathutils.Vector
        :rtype: int
    """

def intersect_point_tri(
    pt: collections.abc.Sequence[float] | mathutils.Vector,
    tri_p1: collections.abc.Sequence[float] | mathutils.Vector,
    tri_p2: collections.abc.Sequence[float] | mathutils.Vector,
    tri_p3: collections.abc.Sequence[float] | mathutils.Vector,
) -> None | mathutils.Vector:
    """Takes 4 vectors: one is the point and the next 3 define the triangle. Projects the point onto the triangle plane and checks if it is within the triangle.

    :param pt: Point
    :type pt: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_p1: First point of the triangle
    :type tri_p1: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_p2: Second point of the triangle
    :type tri_p2: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_p3: Third point of the triangle
    :type tri_p3: collections.abc.Sequence[float] | mathutils.Vector
    :return: Point on the triangles plane or None if its outside the triangle
    :rtype: None | mathutils.Vector
    """

def intersect_point_tri_2d(
    pt: collections.abc.Sequence[float] | mathutils.Vector,
    tri_p1: collections.abc.Sequence[float] | mathutils.Vector,
    tri_p2: collections.abc.Sequence[float] | mathutils.Vector,
    tri_p3: collections.abc.Sequence[float] | mathutils.Vector,
) -> int:
    """Takes 4 vectors (using only the x and y coordinates): one is the point and the next 3 define the triangle. Returns 1 if the point is within the triangle, otherwise 0.

    :param pt: Point
    :type pt: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_p1: First point of the triangle
    :type tri_p1: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_p2: Second point of the triangle
    :type tri_p2: collections.abc.Sequence[float] | mathutils.Vector
    :param tri_p3: Third point of the triangle
    :type tri_p3: collections.abc.Sequence[float] | mathutils.Vector
    :rtype: int
    """

def intersect_ray_tri(
    v1: collections.abc.Sequence[float] | mathutils.Vector,
    v2: collections.abc.Sequence[float] | mathutils.Vector,
    v3: collections.abc.Sequence[float] | mathutils.Vector,
    ray: collections.abc.Sequence[float] | mathutils.Vector,
    orig: collections.abc.Sequence[float] | mathutils.Vector,
    clip: bool = True,
) -> None | mathutils.Vector:
    """Returns the intersection between a ray and a triangle, if possible, returns None otherwise.

    :param v1: Point1
    :type v1: collections.abc.Sequence[float] | mathutils.Vector
    :param v2: Point2
    :type v2: collections.abc.Sequence[float] | mathutils.Vector
    :param v3: Point3
    :type v3: collections.abc.Sequence[float] | mathutils.Vector
    :param ray: Direction of the projection
    :type ray: collections.abc.Sequence[float] | mathutils.Vector
    :param orig: Origin
    :type orig: collections.abc.Sequence[float] | mathutils.Vector
    :param clip: When False, don't restrict the intersection to the area of the triangle, use the infinite plane defined by the triangle.
    :type clip: bool
    :return: The point of intersection or None if no intersection is found
    :rtype: None | mathutils.Vector
    """

def intersect_sphere_sphere_2d(
    p_a: collections.abc.Sequence[float] | mathutils.Vector,
    radius_a: float,
    p_b: collections.abc.Sequence[float] | mathutils.Vector,
    radius_b: float,
) -> tuple[None, None] | tuple[mathutils.Vector, mathutils.Vector]:
    """Returns 2 points on between intersecting circles.

    :param p_a: Center of the first circle
    :type p_a: collections.abc.Sequence[float] | mathutils.Vector
    :param radius_a: Radius of the first circle
    :type radius_a: float
    :param p_b: Center of the second circle
    :type p_b: collections.abc.Sequence[float] | mathutils.Vector
    :param radius_b: Radius of the second circle
    :type radius_b: float
    :return: 2 points on between intersecting circles or None when there is no intersection.
    :rtype: tuple[None, None] | tuple[mathutils.Vector, mathutils.Vector]
    """

def intersect_tri_tri_2d(tri_a1, tri_a2, tri_a3, tri_b1, tri_b2, tri_b3) -> bool:
    """Check if two 2D triangles intersect.

    :rtype: bool
    """

def normal(
    vectors: collections.abc.Sequence[collections.abc.Sequence[float]],
) -> mathutils.Vector:
    """Returns the normal of a 3D polygon.

    :param vectors: 3 or more vectors to calculate normals.
    :type vectors: collections.abc.Sequence[collections.abc.Sequence[float]]
    :rtype: mathutils.Vector
    """

def points_in_planes(
    planes: list[collections.abc.Sequence[float] | mathutils.Vector],
    epsilon_coplanar: float = 0.0001,
    epsilon_isect: float = 1e-06,
) -> tuple[list[mathutils.Vector], list[int]]:
    """Returns a list of points inside all planes given and a list of index values for the planes used.

    :param planes: List of planes (4D vectors).
    :type planes: list[collections.abc.Sequence[float] | mathutils.Vector]
    :param epsilon_coplanar: Epsilon value for interpreting plane pairs as co-plannar.
    :type epsilon_coplanar: float
    :param epsilon_isect: Epsilon value for intersection.
    :type epsilon_isect: float
    :return: Two lists, once containing the 3D coordinates inside the planes, another containing the plane indices used.
    :rtype: tuple[list[mathutils.Vector], list[int]]
    """

def tessellate_polygon(polylines) -> list[tuple[int, int, int]]:
    """Takes a list of polylines (each point a pair or triplet of numbers) and returns the point indices for a polyline filled with triangles. Does not handle degenerate geometry (such as zero-length lines due to consecutive identical points).

    :param polylines: Polygons where each polygon is a sequence of 2D or 3D points.
    :rtype: list[tuple[int, int, int]]
    """

def volume_tetrahedron(
    v1: collections.abc.Sequence[float] | mathutils.Vector,
    v2: collections.abc.Sequence[float] | mathutils.Vector,
    v3: collections.abc.Sequence[float] | mathutils.Vector,
    v4: collections.abc.Sequence[float] | mathutils.Vector,
) -> float:
    """Return the volume formed by a tetrahedron (points can be in any order).

    :param v1: Point1
    :type v1: collections.abc.Sequence[float] | mathutils.Vector
    :param v2: Point2
    :type v2: collections.abc.Sequence[float] | mathutils.Vector
    :param v3: Point3
    :type v3: collections.abc.Sequence[float] | mathutils.Vector
    :param v4: Point4
    :type v4: collections.abc.Sequence[float] | mathutils.Vector
    :rtype: float
    """
