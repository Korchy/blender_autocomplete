"""

--------------------


--------------------


--------------------


--------------------


--------------------


--------------------

"""

import typing
import collections.abc
import bpy.types
import mathutils

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class BMDeformVert:
    def clear(self):
        """Clears all weights."""
        ...

    def get(self, key: int, default=None):
        """Returns the deform weight matching the key or default
        when not found (matches Python's dictionary function of the same name).

                :param key: The key associated with deform weight.
                :type key: int
                :param default: Optional argument for the value to return if
        key is not found.
        """
        ...

    def items(self):
        """Return (group, weight) pairs for this vertex
        (matching Python's dict.items() functionality).

                :return: (key, value) pairs for each deform weight of this vertex.
        """
        ...

    def keys(self) -> list[int]:
        """Return the group indices used by this vertex
        (matching Python's dict.keys() functionality).

                :return: the deform group this vertex uses
                :rtype: list[int]
        """
        ...

    def values(self) -> list[float]:
        """Return the weights of the deform vertex
        (matching Python's dict.values() functionality).

                :return: The weights that influence this vertex
                :rtype: list[float]
        """
        ...

class BMEdge:
    """The BMesh edge connecting 2 verts"""

    hide: bool
    """ Hidden state of this element.

    :type: bool
    """

    index: int
    """ Index of this element.

    :type: int
    """

    is_boundary: bool
    """ True when this edge is at the boundary of a face (read-only).

    :type: bool
    """

    is_contiguous: bool
    """ True when this edge is manifold, between two faces with the same winding (read-only).

    :type: bool
    """

    is_convex: bool
    """ True when this edge joins two convex faces, depends on a valid face normal (read-only).

    :type: bool
    """

    is_manifold: bool
    """ True when this edge is manifold (read-only).

    :type: bool
    """

    is_valid: bool
    """ True when this element is valid (hasn't been removed).

    :type: bool
    """

    is_wire: bool
    """ True when this edge is not connected to any faces (read-only).

    :type: bool
    """

    link_faces: BMElemSeq | list[BMFace]
    """ Faces connected to this edge, (read-only).

    :type: BMElemSeq | list[BMFace]
    """

    link_loops: BMElemSeq | list[BMLoop]
    """ Loops connected to this edge, (read-only).

    :type: BMElemSeq | list[BMLoop]
    """

    seam: bool
    """ Seam for UV unwrapping.

    :type: bool
    """

    select: bool
    """ Selected state of this element.

    :type: bool
    """

    smooth: bool
    """ Smooth state of this element.

    :type: bool
    """

    tag: bool
    """ Generic attribute scripts can use for own logic

    :type: bool
    """

    verts: BMElemSeq | list[BMVert]
    """ Verts this edge uses (always 2), (read-only).

    :type: BMElemSeq | list[BMVert]
    """

    def calc_face_angle(self, fallback: typing.Any = None) -> float:
        """

                :param fallback: return this when the edge doesn't have 2 faces
        (instead of raising a `ValueError`).
                :type fallback: typing.Any
                :return: The angle between 2 connected faces in radians.
                :rtype: float
        """
        ...

    def calc_face_angle_signed(self, fallback: typing.Any = None) -> float:
        """

                :param fallback: return this when the edge doesn't have 2 faces
        (instead of raising a `ValueError`).
                :type fallback: typing.Any
                :return: The angle between 2 connected faces in radians (negative for concave join).
                :rtype: float
        """
        ...

    def calc_length(self) -> float:
        """

        :return: The length between both verts.
        :rtype: float
        """
        ...

    def calc_tangent(self, loop: BMLoop) -> mathutils.Vector:
        """Return the tangent at this edge relative to a face (pointing inward into the face).
        This uses the face normal for calculation.

                :param loop: The loop used for tangent calculation.
                :type loop: BMLoop
                :return: a normalized vector.
                :rtype: mathutils.Vector
        """
        ...

    def copy_from(self, other: BMEdge):
        """Copy values from another element of matching type.

        :param other:
        :type other: BMEdge
        """
        ...

    def hide_set(self, hide: bool):
        """Set the hide state.
        This is different from the hide attribute because it updates the selection and hide state of associated geometry.

                :param hide: Hidden or visible.
                :type hide: bool
        """
        ...

    def normal_update(self):
        """Update normals of all connected faces and the edge verts."""
        ...

    def other_vert(self, vert: BMVert) -> BMVert:
        """Return the other vertex on this edge or None if the vertex is not used by this edge.

        :param vert: a vert in this edge.
        :type vert: BMVert
        :return: The edges other vert.
        :rtype: BMVert
        """
        ...

    def select_set(self, select: bool):
        """Set the selection.
        This is different from the select attribute because it updates the selection state of associated geometry.

                :param select: Select or de-select.
                :type select: bool
        """
        ...

    def __getitem__(self, key: BMLayerItem) -> typing.Any:
        """

        :param key:
        :type key: BMLayerItem
        :return:
        :rtype: typing.Any
        """
        ...

    def __setitem__(self, key: BMLayerItem, value: typing.Any):
        """

        :param key:
        :type key: BMLayerItem
        :param value:
        :type value: typing.Any
        """
        ...

    def __delitem__(self, key: BMLayerItem):
        """

        :param key:
        :type key: BMLayerItem
        """
        ...

class BMEdgeSeq:
    layers: BMLayerAccessEdge
    """ custom-data layers (read-only).

    :type: BMLayerAccessEdge
    """

    def ensure_lookup_table(self):
        """Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg bm.verts[index].This needs to be called again after adding/removing data in this sequence."""
        ...

    def get(self, verts: BMVert, fallback=None) -> BMEdge:
        """Return an edge which uses the verts passed.

        :param verts: Sequence of verts.
        :type verts: BMVert
        :param fallback: Return this value if nothing is found.
        :return: The edge found or None
        :rtype: BMEdge
        """
        ...

    def index_update(self):
        """Initialize the index values of this sequence.This is the equivalent of looping over all elements and assigning the index values."""
        ...

    def new(self, verts, example: BMEdge | None = None) -> BMEdge:
        """Create a new edge from a given pair of verts.

        :param verts: Vertex pair.
        :param example: Existing edge to initialize settings (optional argument).
        :type example: BMEdge | None
        :return: The newly created edge.
        :rtype: BMEdge
        """
        ...

    def remove(self, edge):
        """Remove an edge.

        :param edge:
        """
        ...

    def sort(self, key=None, reverse: bool = False):
        """Sort the elements of this sequence, using an optional custom sort key.
        Indices of elements are not changed, BMElemeSeq.index_update() can be used for that.

                :param key: The key that sets the ordering of the elements.
                :param reverse: Reverse the order of the elements
                :type reverse: bool
        """
        ...

    def __getitem__(self, key: int) -> BMEdge:
        """

        :param key:
        :type key: int
        :return:
        :rtype: BMEdge
        """
        ...

    def __iter__(self) -> BMIter[BMEdge]:
        """

        :return:
        :rtype: BMIter[BMEdge]
        """
        ...

    def __len__(self) -> int:
        """

        :return:
        :rtype: int
        """
        ...

class BMEditSelIter: ...

class BMEditSelSeq:
    active: BMEdge | BMFace | BMVert
    """ The last selected element or None (read-only).

    :type: BMEdge | BMFace | BMVert
    """

    def add(self, element):
        """Add an element to the selection history (no action taken if its already added).

        :param element:
        """
        ...

    def clear(self):
        """Empties the selection history."""
        ...

    def discard(self, element):
        """Discard an element from the selection history.Like remove but doesn't raise an error when the elements not in the selection list.

        :param element:
        """
        ...

    def remove(self, element):
        """Remove an element from the selection history.

        :param element:
        """
        ...

    def validate(self):
        """Ensures all elements in the selection history are selected."""
        ...

class BMElemSeq(typing.Generic[GenericType1]):
    """General sequence type used for accessing any sequence of
    `BMVert`, `BMEdge`, `BMFace`, `BMLoop`.When accessed via `BMesh.verts`, `BMesh.edges`, `BMesh.faces`
    there are also functions to create/remove items.
    """

    def index_update(self):
        """Initialize the index values of this sequence.This is the equivalent of looping over all elements and assigning the index values."""
        ...

    def __getitem__(self, key: int) -> GenericType1:
        """

        :param key:
        :type key: int
        :return:
        :rtype: GenericType1
        """
        ...

    def __iter__(self) -> BMIter[GenericType1]:
        """

        :return:
        :rtype: BMIter[GenericType1]
        """
        ...

    def __len__(self) -> int:
        """

        :return:
        :rtype: int
        """
        ...

class BMFace:
    """The BMesh face with 3 or more sides"""

    edges: BMElemSeq | list[BMEdge]
    """ Edges of this face, (read-only).

    :type: BMElemSeq | list[BMEdge]
    """

    hide: bool
    """ Hidden state of this element.

    :type: bool
    """

    index: int
    """ Index of this element.

    :type: int
    """

    is_valid: bool
    """ True when this element is valid (hasn't been removed).

    :type: bool
    """

    loops: BMElemSeq | list[BMLoop]
    """ Loops of this face, (read-only).

    :type: BMElemSeq | list[BMLoop]
    """

    material_index: int
    """ The face's material index.

    :type: int
    """

    normal: mathutils.Vector
    """ The normal for this face as a 3D, wrapped vector.

    :type: mathutils.Vector
    """

    select: bool
    """ Selected state of this element.

    :type: bool
    """

    smooth: bool
    """ Smooth state of this element.

    :type: bool
    """

    tag: bool
    """ Generic attribute scripts can use for own logic

    :type: bool
    """

    verts: BMElemSeq | list[BMVert]
    """ Verts of this face, (read-only).

    :type: BMElemSeq | list[BMVert]
    """

    def calc_area(self) -> float:
        """Return the area of the face.

        :return: Return the area of the face.
        :rtype: float
        """
        ...

    def calc_center_bounds(self) -> mathutils.Vector:
        """Return bounds center of the face.

        :return: a 3D vector.
        :rtype: mathutils.Vector
        """
        ...

    def calc_center_median(self) -> mathutils.Vector:
        """Return median center of the face.

        :return: a 3D vector.
        :rtype: mathutils.Vector
        """
        ...

    def calc_center_median_weighted(self) -> mathutils.Vector:
        """Return median center of the face weighted by edge lengths.

        :return: a 3D vector.
        :rtype: mathutils.Vector
        """
        ...

    def calc_perimeter(self) -> float:
        """Return the perimeter of the face.

        :return: Return the perimeter of the face.
        :rtype: float
        """
        ...

    def calc_tangent_edge(self) -> mathutils.Vector:
        """Return face tangent based on longest edge.

        :return: a normalized vector.
        :rtype: mathutils.Vector
        """
        ...

    def calc_tangent_edge_diagonal(self) -> mathutils.Vector:
        """Return face tangent based on the edge farthest from any vertex.

        :return: a normalized vector.
        :rtype: mathutils.Vector
        """
        ...

    def calc_tangent_edge_pair(self) -> mathutils.Vector:
        """Return face tangent based on the two longest disconnected edges.

        :return: a normalized vector.
        :rtype: mathutils.Vector
        """
        ...

    def calc_tangent_vert_diagonal(self) -> mathutils.Vector:
        """Return face tangent based on the two most distant vertices.

        :return: a normalized vector.
        :rtype: mathutils.Vector
        """
        ...

    def copy(self, verts: bool = True, edges: bool = True) -> BMFace:
        """Make a copy of this face.

        :param verts: When set, the faces verts will be duplicated too.
        :type verts: bool
        :param edges: When set, the faces edges will be duplicated too.
        :type edges: bool
        :return: The newly created face.
        :rtype: BMFace
        """
        ...

    def copy_from(self, other: BMFace):
        """Copy values from another element of matching type.

        :param other:
        :type other: BMFace
        """
        ...

    def copy_from_face_interp(self, face: BMFace, vert: bool = True):
        """Interpolate the customdata from another face onto this one (faces should overlap).

        :param face: The face to interpolate data from.
        :type face: BMFace
        :param vert: When True, also copy vertex data.
        :type vert: bool
        """
        ...

    def hide_set(self, hide: bool):
        """Set the hide state.
        This is different from the hide attribute because it updates the selection and hide state of associated geometry.

                :param hide: Hidden or visible.
                :type hide: bool
        """
        ...

    def normal_flip(self):
        """Reverses winding of a face, which flips its normal."""
        ...

    def normal_update(self):
        """Update face normal based on the positions of the face verts.
        This does not update the normals of face verts.

        """
        ...

    def select_set(self, select: bool):
        """Set the selection.
        This is different from the select attribute because it updates the selection state of associated geometry.

                :param select: Select or de-select.
                :type select: bool
        """
        ...

    def __getitem__(self, key: BMLayerItem) -> typing.Any:
        """

        :param key:
        :type key: BMLayerItem
        :return:
        :rtype: typing.Any
        """
        ...

    def __setitem__(self, key: BMLayerItem, value: typing.Any):
        """

        :param key:
        :type key: BMLayerItem
        :param value:
        :type value: typing.Any
        """
        ...

    def __delitem__(self, key: BMLayerItem):
        """

        :param key:
        :type key: BMLayerItem
        """
        ...

class BMFaceSeq:
    active: BMFace
    """ active face.

    :type: BMFace
    """

    layers: BMLayerAccessFace
    """ custom-data layers (read-only).

    :type: BMLayerAccessFace
    """

    def ensure_lookup_table(self):
        """Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg bm.verts[index].This needs to be called again after adding/removing data in this sequence."""
        ...

    def get(self, verts: BMVert, fallback=None) -> BMFace:
        """Return a face which uses the verts passed.

        :param verts: Sequence of verts.
        :type verts: BMVert
        :param fallback: Return this value if nothing is found.
        :return: The face found or None
        :rtype: BMFace
        """
        ...

    def index_update(self):
        """Initialize the index values of this sequence.This is the equivalent of looping over all elements and assigning the index values."""
        ...

    def new(self, verts: list[BMVert], example: BMFace | None = None) -> BMFace:
        """Create a new face from a given set of verts.

        :param verts: Sequence of 3 or more verts.
        :type verts: list[BMVert]
        :param example: Existing face to initialize settings (optional argument).
        :type example: BMFace | None
        :return: The newly created face.
        :rtype: BMFace
        """
        ...

    def remove(self, face):
        """Remove a face.

        :param face:
        """
        ...

    def sort(self, key=None, reverse: bool = False):
        """Sort the elements of this sequence, using an optional custom sort key.
        Indices of elements are not changed, BMElemeSeq.index_update() can be used for that.

                :param key: The key that sets the ordering of the elements.
                :param reverse: Reverse the order of the elements
                :type reverse: bool
        """
        ...

    def __getitem__(self, key: int) -> BMFace:
        """

        :param key:
        :type key: int
        :return:
        :rtype: BMFace
        """
        ...

    def __iter__(self) -> BMIter[BMFace]:
        """

        :return:
        :rtype: BMIter[BMFace]
        """
        ...

    def __len__(self) -> int:
        """

        :return:
        :rtype: int
        """
        ...

class BMIter(typing.Generic[GenericType1]):
    """Internal BMesh type for looping over verts/faces/edges,
    used for iterating over `BMElemSeq` types.
    """

    def __iter__(self) -> BMIter[GenericType1]:
        """

        :return:
        :rtype: BMIter[GenericType1]
        """
        ...

    def __next__(self) -> GenericType1:
        """

        :return:
        :rtype: GenericType1
        """
        ...

class BMLayerAccessEdge:
    """Exposes custom-data layer attributes."""

    color: typing.Any
    """ Generic RGBA color with 8-bit precision custom-data layer.type: `BMLayerCollection`"""

    float: typing.Any
    """ Generic float custom-data layer.type: `BMLayerCollection`"""

    float_color: typing.Any
    """ Generic RGBA color with float precision custom-data layer.type: `BMLayerCollection`"""

    float_vector: typing.Any
    """ Generic 3D vector with float precision custom-data layer.type: `BMLayerCollection`"""

    freestyle: typing.Any
    """ Accessor for Freestyle edge layer.type: `BMLayerCollection`"""

    int: typing.Any
    """ Generic int custom-data layer.type: `BMLayerCollection`"""

    string: typing.Any
    """ Generic string custom-data layer (exposed as bytes, 255 max length).type: `BMLayerCollection`"""

class BMLayerAccessFace:
    """Exposes custom-data layer attributes."""

    color: typing.Any
    """ Generic RGBA color with 8-bit precision custom-data layer.type: `BMLayerCollection`"""

    float: typing.Any
    """ Generic float custom-data layer.type: `BMLayerCollection`"""

    float_color: typing.Any
    """ Generic RGBA color with float precision custom-data layer.type: `BMLayerCollection`"""

    float_vector: typing.Any
    """ Generic 3D vector with float precision custom-data layer.type: `BMLayerCollection`"""

    freestyle: typing.Any
    """ Accessor for Freestyle face layer.type: `BMLayerCollection`"""

    int: typing.Any
    """ Generic int custom-data layer.type: `BMLayerCollection`"""

    string: typing.Any
    """ Generic string custom-data layer (exposed as bytes, 255 max length).type: `BMLayerCollection`"""

class BMLayerAccessLoop:
    """Exposes custom-data layer attributes."""

    color: typing.Any
    """ Generic RGBA color with 8-bit precision custom-data layer.type: `BMLayerCollection`"""

    float: typing.Any
    """ Generic float custom-data layer.type: `BMLayerCollection`"""

    float_color: typing.Any
    """ Generic RGBA color with float precision custom-data layer.type: `BMLayerCollection`"""

    float_vector: typing.Any
    """ Generic 3D vector with float precision custom-data layer.type: `BMLayerCollection`"""

    int: typing.Any
    """ Generic int custom-data layer.type: `BMLayerCollection`"""

    string: typing.Any
    """ Generic string custom-data layer (exposed as bytes, 255 max length).type: `BMLayerCollection`"""

    uv: typing.Any
    """ Accessor for `BMLoopUV` UV (as a 2D Vector).type: `BMLayerCollection`"""

class BMLayerAccessVert:
    """Exposes custom-data layer attributes."""

    color: typing.Any
    """ Generic RGBA color with 8-bit precision custom-data layer.type: `BMLayerCollection`"""

    deform: typing.Any
    """ Vertex deform weight `BMDeformVert` (TODO).type: `BMLayerCollection`"""

    float: typing.Any
    """ Generic float custom-data layer.type: `BMLayerCollection`"""

    float_color: typing.Any
    """ Generic RGBA color with float precision custom-data layer.type: `BMLayerCollection`"""

    float_vector: typing.Any
    """ Generic 3D vector with float precision custom-data layer.type: `BMLayerCollection`"""

    int: typing.Any
    """ Generic int custom-data layer.type: `BMLayerCollection`"""

    shape: BMLayerCollection
    """ Vertex shapekey absolute location (as a 3D Vector).

    :type: BMLayerCollection
    """

    skin: typing.Any
    """ Accessor for skin layer.type: `BMLayerCollection`"""

    string: typing.Any
    """ Generic string custom-data layer (exposed as bytes, 255 max length).type: `BMLayerCollection`"""

class BMLayerCollection:
    """Gives access to a collection of custom-data layers of the same type and behaves like Python dictionaries, except for the ability to do list like index access."""

    active: BMLayerItem
    """ The active layer of this type (read-only).

    :type: BMLayerItem
    """

    is_singleton: bool
    """ True if there can exists only one layer of this type (read-only).

    :type: bool
    """

    def get(self, key: str, default: GenericType2 = None) -> BMLayerItem | GenericType2:
        """Returns the value of the layer matching the key or default
        when not found (matches Python's dictionary function of the same name).

                :param key: The key associated with the layer.
                :type key: str
                :param default: Optional argument for the value to return if
        key is not found.
                :type default: GenericType2
                :return:
                :rtype: BMLayerItem | GenericType2
        """
        ...

    def items(self):
        """Return the identifiers of collection members
        (matching Python's dict.items() functionality).

                :return: (key, value) pairs for each member of this collection.
        """
        ...

    def keys(self) -> list[str]:
        """Return the identifiers of collection members
        (matching Python's dict.keys() functionality).

                :return: the identifiers for each member of this collection.
                :rtype: list[str]
        """
        ...

    def new(self, name: str | None) -> BMLayerItem:
        """Create a new layer

        :param name: Optional name argument (will be made unique).
        :type name: str | None
        :return: The newly created layer.
        :rtype: BMLayerItem
        """
        ...

    def remove(self, layer: BMLayerItem):
        """Remove a layer

        :param layer: The layer to remove.
        :type layer: BMLayerItem
        """
        ...

    def values(self) -> list:
        """Return the values of collection
        (matching Python's dict.values() functionality).

                :return: the members of this collection.
                :rtype: list
        """
        ...

    def verify(self) -> BMLayerItem:
        """Create a new layer or return an existing active layer

        :return: The newly verified layer.
        :rtype: BMLayerItem
        """
        ...

class BMLayerItem:
    """Exposes a single custom data layer, their main purpose is for use as item accessors to custom-data when used with vert/edge/face/loop data."""

    name: str
    """ The layers unique name (read-only).

    :type: str
    """

    def copy_from(self, other):
        """Return a copy of the layer

        :param other: Another layer to copy from.`BMLayerItem`
        """
        ...

class BMLoop:
    """This is normally accessed from `BMFace.loops` where each face loop represents a corner of the face."""

    edge: BMEdge
    """ The loop's edge (between this loop and the next), (read-only).

    :type: BMEdge
    """

    face: BMFace
    """ The face this loop makes (read-only).

    :type: BMFace
    """

    index: int
    """ Index of this element.

    :type: int
    """

    is_convex: bool
    """ True when this loop is at the convex corner of a face, depends on a valid face normal (read-only).

    :type: bool
    """

    is_valid: bool
    """ True when this element is valid (hasn't been removed).

    :type: bool
    """

    link_loop_next: BMLoop
    """ The next face corner (read-only).

    :type: BMLoop
    """

    link_loop_prev: BMLoop
    """ The previous face corner (read-only).

    :type: BMLoop
    """

    link_loop_radial_next: BMLoop
    """ The next loop around the edge (read-only).

    :type: BMLoop
    """

    link_loop_radial_prev: BMLoop
    """ The previous loop around the edge (read-only).

    :type: BMLoop
    """

    link_loops: BMElemSeq | list[BMLoop]
    """ Loops connected to this loop, (read-only).

    :type: BMElemSeq | list[BMLoop]
    """

    tag: bool
    """ Generic attribute scripts can use for own logic

    :type: bool
    """

    vert: BMVert
    """ The loop's vertex (read-only).

    :type: BMVert
    """

    def calc_angle(self) -> float:
        """Return the angle at this loops corner of the face.
        This is calculated so sharper corners give lower angles.

                :return: The angle in radians.
                :rtype: float
        """
        ...

    def calc_normal(self) -> mathutils.Vector:
        """Return normal at this loops corner of the face.
        Falls back to the face normal for straight lines.

                :return: a normalized vector.
                :rtype: mathutils.Vector
        """
        ...

    def calc_tangent(self) -> mathutils.Vector:
        """Return the tangent at this loops corner of the face (pointing inward into the face).
        Falls back to the face normal for straight lines.

                :return: a normalized vector.
                :rtype: mathutils.Vector
        """
        ...

    def copy_from(self, other: BMLoop):
        """Copy values from another element of matching type.

        :param other:
        :type other: BMLoop
        """
        ...

    def copy_from_face_interp(
        self, face: BMFace, vert: bool | None = True, multires: bool | None = True
    ):
        """Interpolate the customdata from a face onto this loop (the loops vert should overlap the face).

        :param face: The face to interpolate data from.
        :type face: BMFace
        :param vert: When enabled, interpolate the loops vertex data (optional).
        :type vert: bool | None
        :param multires: When enabled, interpolate the loops multires data (optional).
        :type multires: bool | None
        """
        ...

    def __getitem__(self, key: BMLayerItem) -> typing.Any:
        """

        :param key:
        :type key: BMLayerItem
        :return:
        :rtype: typing.Any
        """
        ...

    def __setitem__(self, key: BMLayerItem, value: typing.Any):
        """

        :param key:
        :type key: BMLayerItem
        :param value:
        :type value: typing.Any
        """
        ...

    def __delitem__(self, key: BMLayerItem):
        """

        :param key:
        :type key: BMLayerItem
        """
        ...

class BMLoopSeq:
    layers: BMLayerAccessLoop
    """ custom-data layers (read-only).

    :type: BMLayerAccessLoop
    """

class BMLoopUV:
    pin_uv: bool
    """ UV pin state.

    :type: bool
    """

    select: bool
    """ UV select state.

    :type: bool
    """

    select_edge: bool
    """ UV edge select state.

    :type: bool
    """

    uv: mathutils.Vector
    """ Loops UV (as a 2D Vector).

    :type: mathutils.Vector
    """

class BMVert:
    """The BMesh vertex type"""

    co: mathutils.Vector
    """ The coordinates for this vertex as a 3D, wrapped vector.

    :type: mathutils.Vector
    """

    hide: bool
    """ Hidden state of this element.

    :type: bool
    """

    index: int
    """ Index of this element.

    :type: int
    """

    is_boundary: bool
    """ True when this vertex is connected to boundary edges (read-only).

    :type: bool
    """

    is_manifold: bool
    """ True when this vertex is manifold (read-only).

    :type: bool
    """

    is_valid: bool
    """ True when this element is valid (hasn't been removed).

    :type: bool
    """

    is_wire: bool
    """ True when this vertex is not connected to any faces (read-only).

    :type: bool
    """

    link_edges: BMElemSeq | list[BMEdge]
    """ Edges connected to this vertex (read-only).

    :type: BMElemSeq | list[BMEdge]
    """

    link_faces: BMElemSeq | list[BMFace]
    """ Faces connected to this vertex (read-only).

    :type: BMElemSeq | list[BMFace]
    """

    link_loops: BMElemSeq | list[BMLoop]
    """ Loops that use this vertex (read-only).

    :type: BMElemSeq | list[BMLoop]
    """

    normal: mathutils.Vector
    """ The normal for this vertex as a 3D, wrapped vector.

    :type: mathutils.Vector
    """

    select: bool
    """ Selected state of this element.

    :type: bool
    """

    tag: bool
    """ Generic attribute scripts can use for own logic

    :type: bool
    """

    def calc_edge_angle(self, fallback: typing.Any = None) -> float:
        """Return the angle between this vert's two connected edges.

                :param fallback: return this when the vert doesn't have 2 edges
        (instead of raising a `ValueError`).
                :type fallback: typing.Any
                :return: Angle between edges in radians.
                :rtype: float
        """
        ...

    def calc_shell_factor(self) -> float:
        """Return a multiplier calculated based on the sharpness of the vertex.
        Where a flat surface gives 1.0, and higher values sharper edges.
        This is used to maintain shell thickness when offsetting verts along their normals.

                :return: offset multiplier
                :rtype: float
        """
        ...

    def copy_from(self, other: BMVert):
        """Copy values from another element of matching type.

        :param other:
        :type other: BMVert
        """
        ...

    def copy_from_face_interp(self, face: BMFace):
        """Interpolate the customdata from a face onto this loop (the loops vert should overlap the face).

        :param face: The face to interpolate data from.
        :type face: BMFace
        """
        ...

    def copy_from_vert_interp(self, vert_pair: BMVert, fac):
        """Interpolate the customdata from a vert between 2 other verts.

        :param vert_pair: The vert to interpolate data from.
        :type vert_pair: BMVert
        :param fac:
        """
        ...

    def hide_set(self, hide: bool):
        """Set the hide state.
        This is different from the hide attribute because it updates the selection and hide state of associated geometry.

                :param hide: Hidden or visible.
                :type hide: bool
        """
        ...

    def normal_update(self):
        """Update vertex normal.
        This does not update the normals of adjoining faces.

        """
        ...

    def select_set(self, select: bool):
        """Set the selection.
        This is different from the select attribute because it updates the selection state of associated geometry.

                :param select: Select or de-select.
                :type select: bool
        """
        ...

    def __getitem__(self, key: BMLayerItem) -> typing.Any:
        """

        :param key:
        :type key: BMLayerItem
        :return:
        :rtype: typing.Any
        """
        ...

    def __setitem__(self, key: BMLayerItem, value: typing.Any):
        """

        :param key:
        :type key: BMLayerItem
        :param value:
        :type value: typing.Any
        """
        ...

    def __delitem__(self, key: BMLayerItem):
        """

        :param key:
        :type key: BMLayerItem
        """
        ...

class BMVertSeq:
    layers: BMLayerAccessVert
    """ custom-data layers (read-only).

    :type: BMLayerAccessVert
    """

    def ensure_lookup_table(self):
        """Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg bm.verts[index].This needs to be called again after adding/removing data in this sequence."""
        ...

    def index_update(self):
        """Initialize the index values of this sequence.This is the equivalent of looping over all elements and assigning the index values."""
        ...

    def new(
        self,
        co: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0, 0.0),
        example: BMVert = None,
    ) -> BMVert:
        """Create a new vertex.

        :param co: The initial location of the vertex (optional argument).
        :type co: collections.abc.Sequence[float] | mathutils.Vector | None
        :param example: Existing vert to initialize settings.
        :type example: BMVert
        :return: The newly created vertex.
        :rtype: BMVert
        """
        ...

    def remove(self, vert):
        """Remove a vert.

        :param vert:
        """
        ...

    def sort(self, key=None, reverse: bool = False):
        """Sort the elements of this sequence, using an optional custom sort key.
        Indices of elements are not changed, BMElemeSeq.index_update() can be used for that.

                :param key: The key that sets the ordering of the elements.
                :param reverse: Reverse the order of the elements
                :type reverse: bool
        """
        ...

    def __getitem__(self, key: int) -> BMVert:
        """

        :param key:
        :type key: int
        :return:
        :rtype: BMVert
        """
        ...

    def __iter__(self) -> BMIter[BMVert]:
        """

        :return:
        :rtype: BMIter[BMVert]
        """
        ...

    def __len__(self) -> int:
        """

        :return:
        :rtype: int
        """
        ...

class BMesh:
    """The BMesh data structure"""

    edges: BMEdgeSeq
    """ This meshes edge sequence (read-only).

    :type: BMEdgeSeq
    """

    faces: BMFaceSeq
    """ This meshes face sequence (read-only).

    :type: BMFaceSeq
    """

    is_valid: bool
    """ True when this element is valid (hasn't been removed).

    :type: bool
    """

    is_wrapped: bool
    """ True when this mesh is owned by blender (typically the editmode BMesh).

    :type: bool
    """

    loops: BMLoopSeq
    """ This meshes loops (read-only).

    :type: BMLoopSeq
    """

    select_history: BMEditSelSeq
    """ Sequence of selected items (the last is displayed as active).

    :type: BMEditSelSeq
    """

    select_mode: set
    """ The selection mode, values can be {'VERT', 'EDGE', 'FACE'}, can't be assigned an empty set.

    :type: set
    """

    verts: BMVertSeq
    """ This meshes vert sequence (read-only).

    :type: BMVertSeq
    """

    def calc_loop_triangles(self):
        """Calculate triangle tessellation from quads/ngons.

        :return: The triangulated faces.
        """
        ...

    def calc_volume(self, signed: bool = False) -> float:
        """Calculate mesh volume based on face normals.

        :param signed: when signed is true, negative values may be returned.
        :type signed: bool
        :return: The volume of the mesh.
        :rtype: float
        """
        ...

    def clear(self):
        """Clear all mesh data."""
        ...

    def copy(self) -> BMesh:
        """

        :return: A copy of this BMesh.
        :rtype: BMesh
        """
        ...

    def free(self):
        """Explicitly free the BMesh data from memory, causing exceptions on further access."""
        ...

    def from_mesh(
        self,
        mesh: bpy.types.Mesh,
        face_normals=True,
        vertex_normals=True,
        use_shape_key: bool = False,
        shape_key_index: int = 0,
    ):
        """Initialize this bmesh from existing mesh datablock.

        :param mesh: The mesh data to load.
        :type mesh: bpy.types.Mesh
        :param face_normals:
        :param vertex_normals:
        :param use_shape_key: Use the locations from a shape key.
        :type use_shape_key: bool
        :param shape_key_index: The shape key index to use.
        :type shape_key_index: int
        """
        ...

    def from_object(
        self,
        object: bpy.types.Object,
        depsgraph,
        cage: bool = False,
        face_normals: bool = True,
        vertex_normals: bool = True,
    ):
        """Initialize this bmesh from existing object data-block (only meshes are currently supported).

        :param object: The object data to load.
        :type object: bpy.types.Object
        :param depsgraph:
        :param cage: Get the mesh as a deformed cage.
        :type cage: bool
        :param face_normals: Calculate face normals.
        :type face_normals: bool
        :param vertex_normals: Calculate vertex normals.
        :type vertex_normals: bool
        """
        ...

    def normal_update(self):
        """Update normals of mesh faces and verts."""
        ...

    def select_flush(self, select: bool):
        """Flush selection, independent of the current selection mode.

        :param select: flush selection or de-selected elements.
        :type select: bool
        """
        ...

    def select_flush_mode(self):
        """flush selection based on the current mode current `BMesh.select_mode`."""
        ...

    def to_mesh(self, mesh: bpy.types.Mesh):
        """Writes this BMesh data into an existing Mesh datablock.

        :param mesh: The mesh data to write into.
        :type mesh: bpy.types.Mesh
        """
        ...

    def transform(
        self,
        matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
        | mathutils.Matrix,
        filter: set = None,
    ):
        """Transform the mesh (optionally filtering flagged data only).

        :param matrix: transform matrix.
        :type matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix
        :param filter: set of values in ('SELECT', 'HIDE', 'SEAM', 'SMOOTH', 'TAG').
        :type filter: set
        """
        ...
