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
import typing_extensions
import bpy.types
import mathutils

class BMDeformVert:
    def clear(self):
        """Clears all weights."""

    def get(self, key: int, default: typing.Any | None = None):
        """Returns the deform weight matching the key or default
        when not found (matches Python's dictionary function of the same name).

                :param key: The key associated with deform weight.
                :type key: int
                :param default: Optional argument for the value to return if
        key is not found.
                :type default: typing.Any | None
        """

    def items(self) -> list[tuple[int, float]]:
        """Return (group, weight) pairs for this vertex
        (matching Python's dict.items() functionality).

                :return: (key, value) pairs for each deform weight of this vertex.
                :rtype: list[tuple[int, float]]
        """

    def keys(self) -> list[int]:
        """Return the group indices used by this vertex
        (matching Python's dict.keys() functionality).

                :return: the deform group this vertex uses
                :rtype: list[int]
        """

    def values(self) -> list[float]:
        """Return the weights of the deform vertex
        (matching Python's dict.values() functionality).

                :return: The weights that influence this vertex
                :rtype: list[float]
        """

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

    link_faces: BMElemSeq[BMFace]
    """ Faces connected to this edge, (read-only).

    :type: BMElemSeq[BMFace]
    """

    link_loops: BMElemSeq[BMLoop]
    """ Loops connected to this edge, (read-only).

    :type: BMElemSeq[BMLoop]
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

    verts: BMElemSeq[BMVert]
    """ Verts this edge uses (always 2), (read-only).

    :type: BMElemSeq[BMVert]
    """

    def calc_face_angle(self, fallback: typing.Any | None = None) -> float:
        """

                :param fallback: return this when the edge doesn't have 2 faces
        (instead of raising a `ValueError`).
                :type fallback: typing.Any | None
                :return: The angle between 2 connected faces in radians.
                :rtype: float
        """

    def calc_face_angle_signed(self, fallback: typing.Any | None = None) -> float:
        """

                :param fallback: return this when the edge doesn't have 2 faces
        (instead of raising a `ValueError`).
                :type fallback: typing.Any | None
                :return: The angle between 2 connected faces in radians (negative for concave join).
                :rtype: float
        """

    def calc_length(self) -> float:
        """

        :return: The length between both verts.
        :rtype: float
        """

    def calc_tangent(self, loop: BMLoop) -> mathutils.Vector:
        """Return the tangent at this edge relative to a face (pointing inward into the face).
        This uses the face normal for calculation.

                :param loop: The loop used for tangent calculation.
                :type loop: BMLoop
                :return: a normalized vector.
                :rtype: mathutils.Vector
        """

    def copy_from(self, other: typing_extensions.Self):
        """Copy values from another element of matching type.

        :param other:
        :type other: typing_extensions.Self
        """

    def hide_set(self, hide: bool):
        """Set the hide state.
        This is different from the hide attribute because it updates the selection and hide state of associated geometry.

                :param hide: Hidden or visible.
                :type hide: bool
        """

    def normal_update(self):
        """Update normals of all connected faces and the edge verts."""

    def other_vert(self, vert: BMVert) -> BMVert | None:
        """Return the other vertex on this edge or None if the vertex is not used by this edge.

        :param vert: a vert in this edge.
        :type vert: BMVert
        :return: The edges other vert.
        :rtype: BMVert | None
        """

    def select_set(self, select: bool):
        """Set the selection.
        This is different from the select attribute because it updates the selection state of associated geometry.

                :param select: Select or de-select.
                :type select: bool
        """

    def __getitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1]
    ) -> _GenericType1:
        """

        :param key:
        :type key: BMLayerItem[_GenericType1]
        :return:
        :rtype: _GenericType1
        """

    def __setitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1], value: _GenericType1
    ):
        """

        :param key:
        :type key: BMLayerItem[_GenericType1]
        :param value:
        :type value: _GenericType1
        """

    def __delitem__[_GenericType1](self, key: BMLayerItem[_GenericType1]):
        """

        :param key:
        :type key: BMLayerItem[_GenericType1]
        """

class BMEdgeSeq:
    layers: BMLayerAccessEdge
    """ custom-data layers (read-only).

    :type: BMLayerAccessEdge
    """

    def ensure_lookup_table(self):
        """Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg bm.verts[index].This needs to be called again after adding/removing data in this sequence."""

    def get(self, verts: collections.abc.Sequence[BMVert], fallback=None) -> BMEdge:
        """Return an edge which uses the verts passed.

        :param verts: Sequence of verts.
        :type verts: collections.abc.Sequence[BMVert]
        :param fallback: Return this value if nothing is found.
        :return: The edge found or None
        :rtype: BMEdge
        """

    def index_update(self):
        """Initialize the index values of this sequence.This is the equivalent of looping over all elements and assigning the index values."""

    def new(
        self, verts: collections.abc.Sequence[BMVert], example: BMEdge | None = None
    ) -> BMEdge:
        """Create a new edge from a given pair of verts.

        :param verts: Vertex pair.
        :type verts: collections.abc.Sequence[BMVert]
        :param example: Existing edge to initialize settings (optional argument).
        :type example: BMEdge | None
        :return: The newly created edge.
        :rtype: BMEdge
        """

    def remove(self, edge: BMEdge):
        """Remove an edge.

        :param edge:
        :type edge: BMEdge
        """

    def sort(
        self,
        key: None
        | collections.abc.Callable[[BMVert | BMEdge | BMFace], int]
        | None = None,
        reverse: bool = False,
    ):
        """Sort the elements of this sequence, using an optional custom sort key.
        Indices of elements are not changed, `BMElemSeq.index_update` can be used for that.

                :param key: The key that sets the ordering of the elements.
                :type key: None | collections.abc.Callable[[BMVert | BMEdge | BMFace], int] | None
                :param reverse: Reverse the order of the elements
                :type reverse: bool
        """

    @typing.overload
    def __getitem__(self, key: int) -> BMEdge:
        """

        :param key:
        :type key: int
        :return:
        :rtype: BMEdge
        """

    @typing.overload
    def __getitem__(self, key: slice) -> list[BMEdge, ...]:
        """

        :param key:
        :type key: slice
        :return:
        :rtype: list[BMEdge, ...]
        """

    def __iter__(self) -> BMIter[BMEdge]:
        """

        :return:
        :rtype: BMIter[BMEdge]
        """

    def __len__(self) -> int:
        """

        :return:
        :rtype: int
        """

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

    def clear(self):
        """Empties the selection history."""

    def discard(self, element):
        """Discard an element from the selection history.Like remove but doesn't raise an error when the elements not in the selection list.

        :param element:
        """

    def remove(self, element):
        """Remove an element from the selection history.

        :param element:
        """

    def validate(self):
        """Ensures all elements in the selection history are selected."""

class BMElemSeq[_GenericType1]:
    """General sequence type used for accessing any sequence of
    `BMVert`, `BMEdge`, `BMFace`, `BMLoop`.When accessed via `BMesh.verts`, `BMesh.edges`, `BMesh.faces`
    there are also functions to create/remove items.
    """

    def index_update(self):
        """Initialize the index values of this sequence.This is the equivalent of looping over all elements and assigning the index values."""

    @typing.overload
    def __getitem__(self, key: int) -> _GenericType1:
        """

        :param key:
        :type key: int
        :return:
        :rtype: _GenericType1
        """

    @typing.overload
    def __getitem__(self, key: slice) -> list[_GenericType1, ...]:
        """

        :param key:
        :type key: slice
        :return:
        :rtype: list[_GenericType1, ...]
        """

    def __iter__(self) -> BMIter[_GenericType1]:
        """

        :return:
        :rtype: BMIter[_GenericType1]
        """

    def __len__(self) -> int:
        """

        :return:
        :rtype: int
        """

class BMFace:
    """The BMesh face with 3 or more sides"""

    edges: BMElemSeq[BMEdge]
    """ Edges of this face, (read-only).

    :type: BMElemSeq[BMEdge]
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

    loops: BMElemSeq[BMLoop]
    """ Loops of this face, (read-only).

    :type: BMElemSeq[BMLoop]
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

    verts: BMElemSeq[BMVert]
    """ Verts of this face, (read-only).

    :type: BMElemSeq[BMVert]
    """

    def calc_area(self) -> float:
        """Return the area of the face.

        :return: Return the area of the face.
        :rtype: float
        """

    def calc_center_bounds(self) -> mathutils.Vector:
        """Return bounds center of the face.

        :return: a 3D vector.
        :rtype: mathutils.Vector
        """

    def calc_center_median(self) -> mathutils.Vector:
        """Return median center of the face.

        :return: a 3D vector.
        :rtype: mathutils.Vector
        """

    def calc_center_median_weighted(self) -> mathutils.Vector:
        """Return median center of the face weighted by edge lengths.

        :return: a 3D vector.
        :rtype: mathutils.Vector
        """

    def calc_perimeter(self) -> float:
        """Return the perimeter of the face.

        :return: Return the perimeter of the face.
        :rtype: float
        """

    def calc_tangent_edge(self) -> mathutils.Vector:
        """Return face tangent based on longest edge.

        :return: a normalized vector.
        :rtype: mathutils.Vector
        """

    def calc_tangent_edge_diagonal(self) -> mathutils.Vector:
        """Return face tangent based on the edge farthest from any vertex.

        :return: a normalized vector.
        :rtype: mathutils.Vector
        """

    def calc_tangent_edge_pair(self) -> mathutils.Vector:
        """Return face tangent based on the two longest disconnected edges.

        :return: a normalized vector.
        :rtype: mathutils.Vector
        """

    def calc_tangent_vert_diagonal(self) -> mathutils.Vector:
        """Return face tangent based on the two most distant vertices.

        :return: a normalized vector.
        :rtype: mathutils.Vector
        """

    def copy(self, verts: bool = True, edges: bool = True) -> typing_extensions.Self:
        """Make a copy of this face.

        :param verts: When set, the faces verts will be duplicated too.
        :type verts: bool
        :param edges: When set, the faces edges will be duplicated too.
        :type edges: bool
        :return: The newly created face.
        :rtype: typing_extensions.Self
        """

    def copy_from(self, other: typing_extensions.Self):
        """Copy values from another element of matching type.

        :param other:
        :type other: typing_extensions.Self
        """

    def copy_from_face_interp(self, face: typing_extensions.Self, vert: bool = True):
        """Interpolate the customdata from another face onto this one (faces should overlap).

        :param face: The face to interpolate data from.
        :type face: typing_extensions.Self
        :param vert: When True, also copy vertex data.
        :type vert: bool
        """

    def hide_set(self, hide: bool):
        """Set the hide state.
        This is different from the hide attribute because it updates the selection and hide state of associated geometry.

                :param hide: Hidden or visible.
                :type hide: bool
        """

    def normal_flip(self):
        """Reverses winding of a face, which flips its normal."""

    def normal_update(self):
        """Update face normal based on the positions of the face verts.
        This does not update the normals of face verts.

        """

    def select_set(self, select: bool):
        """Set the selection.
        This is different from the select attribute because it updates the selection state of associated geometry.

                :param select: Select or de-select.
                :type select: bool
        """

    def __getitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1]
    ) -> _GenericType1:
        """

        :param key:
        :type key: BMLayerItem[_GenericType1]
        :return:
        :rtype: _GenericType1
        """

    def __setitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1], value: _GenericType1
    ):
        """

        :param key:
        :type key: BMLayerItem[_GenericType1]
        :param value:
        :type value: _GenericType1
        """

    def __delitem__[_GenericType1](self, key: BMLayerItem[_GenericType1]):
        """

        :param key:
        :type key: BMLayerItem[_GenericType1]
        """

class BMFaceSeq:
    active: BMFace | None
    """ active face.

    :type: BMFace | None
    """

    layers: BMLayerAccessFace
    """ custom-data layers (read-only).

    :type: BMLayerAccessFace
    """

    def ensure_lookup_table(self):
        """Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg bm.verts[index].This needs to be called again after adding/removing data in this sequence."""

    def get(self, verts: collections.abc.Sequence[BMVert], fallback=None) -> BMFace:
        """Return a face which uses the verts passed.

        :param verts: Sequence of verts.
        :type verts: collections.abc.Sequence[BMVert]
        :param fallback: Return this value if nothing is found.
        :return: The face found or None
        :rtype: BMFace
        """

    def index_update(self):
        """Initialize the index values of this sequence.This is the equivalent of looping over all elements and assigning the index values."""

    def new(
        self, verts: collections.abc.Sequence[BMVert], example: BMFace | None = None
    ) -> BMFace:
        """Create a new face from a given set of verts.

        :param verts: Sequence of 3 or more verts.
        :type verts: collections.abc.Sequence[BMVert]
        :param example: Existing face to initialize settings (optional argument).
        :type example: BMFace | None
        :return: The newly created face.
        :rtype: BMFace
        """

    def remove(self, face: BMFace):
        """Remove a face.

        :param face:
        :type face: BMFace
        """

    def sort(
        self,
        key: None
        | collections.abc.Callable[[BMVert | BMEdge | BMFace], int]
        | None = None,
        reverse: bool = False,
    ):
        """Sort the elements of this sequence, using an optional custom sort key.
        Indices of elements are not changed, `BMElemSeq.index_update` can be used for that.

                :param key: The key that sets the ordering of the elements.
                :type key: None | collections.abc.Callable[[BMVert | BMEdge | BMFace], int] | None
                :param reverse: Reverse the order of the elements
                :type reverse: bool
        """

    @typing.overload
    def __getitem__(self, key: int) -> BMFace:
        """

        :param key:
        :type key: int
        :return:
        :rtype: BMFace
        """

    @typing.overload
    def __getitem__(self, key: slice) -> list[BMFace, ...]:
        """

        :param key:
        :type key: slice
        :return:
        :rtype: list[BMFace, ...]
        """

    def __iter__(self) -> BMIter[BMFace]:
        """

        :return:
        :rtype: BMIter[BMFace]
        """

    def __len__(self) -> int:
        """

        :return:
        :rtype: int
        """

class BMIter[_GenericType1]:
    """Internal BMesh type for looping over verts/faces/edges,
    used for iterating over `BMElemSeq` types.
    """

    def __iter__(self) -> BMIter[_GenericType1]:
        """

        :return:
        :rtype: BMIter[_GenericType1]
        """

    def __next__(self) -> _GenericType1:
        """

        :return:
        :rtype: _GenericType1
        """

class BMLayerAccessEdge:
    """Exposes custom-data layer attributes."""

    color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with 8-bit precision custom-data layer.

    :type: BMLayerCollection[mathutils.Vector]
    """

    float: BMLayerCollection[float]
    """ Generic float custom-data layer.

    :type: BMLayerCollection[float]
    """

    float_color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with float precision custom-data layer.

    :type: BMLayerCollection[mathutils.Vector]
    """

    float_vector: BMLayerCollection[mathutils.Vector]
    """ Generic 3D vector with float precision custom-data layer.

    :type: BMLayerCollection[mathutils.Vector]
    """

    freestyle: BMLayerCollection
    """ Accessor for Freestyle edge layer.

    :type: BMLayerCollection
    """

    int: BMLayerCollection[int]
    """ Generic int custom-data layer.

    :type: BMLayerCollection[int]
    """

    string: BMLayerCollection[bytes]
    """ Generic string custom-data layer (exposed as bytes, 255 max length).

    :type: BMLayerCollection[bytes]
    """

class BMLayerAccessFace:
    """Exposes custom-data layer attributes."""

    color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with 8-bit precision custom-data layer.

    :type: BMLayerCollection[mathutils.Vector]
    """

    float: BMLayerCollection[float]
    """ Generic float custom-data layer.

    :type: BMLayerCollection[float]
    """

    float_color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with float precision custom-data layer.

    :type: BMLayerCollection[mathutils.Vector]
    """

    float_vector: BMLayerCollection[mathutils.Vector]
    """ Generic 3D vector with float precision custom-data layer.

    :type: BMLayerCollection[mathutils.Vector]
    """

    freestyle: BMLayerCollection
    """ Accessor for Freestyle face layer.

    :type: BMLayerCollection
    """

    int: BMLayerCollection[int]
    """ Generic int custom-data layer.

    :type: BMLayerCollection[int]
    """

    string: BMLayerCollection[bytes]
    """ Generic string custom-data layer (exposed as bytes, 255 max length).

    :type: BMLayerCollection[bytes]
    """

class BMLayerAccessLoop:
    """Exposes custom-data layer attributes."""

    color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with 8-bit precision custom-data layer.

    :type: BMLayerCollection[mathutils.Vector]
    """

    float: BMLayerCollection[float]
    """ Generic float custom-data layer.

    :type: BMLayerCollection[float]
    """

    float_color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with float precision custom-data layer.

    :type: BMLayerCollection[mathutils.Vector]
    """

    float_vector: BMLayerCollection[mathutils.Vector]
    """ Generic 3D vector with float precision custom-data layer.

    :type: BMLayerCollection[mathutils.Vector]
    """

    int: BMLayerCollection[int]
    """ Generic int custom-data layer.

    :type: BMLayerCollection[int]
    """

    string: BMLayerCollection[bytes]
    """ Generic string custom-data layer (exposed as bytes, 255 max length).

    :type: BMLayerCollection[bytes]
    """

    uv: BMLayerCollection[BMLoopUV]
    """ Accessor for `BMLoopUV` UV (as a 2D Vector).

    :type: BMLayerCollection[BMLoopUV]
    """

class BMLayerAccessVert:
    """Exposes custom-data layer attributes."""

    color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with 8-bit precision custom-data layer.

    :type: BMLayerCollection[mathutils.Vector]
    """

    deform: BMLayerCollection[BMDeformVert]
    """ Vertex deform weight `BMDeformVert` (TODO).

    :type: BMLayerCollection[BMDeformVert]
    """

    float: BMLayerCollection[float]
    """ Generic float custom-data layer.

    :type: BMLayerCollection[float]
    """

    float_color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with float precision custom-data layer.

    :type: BMLayerCollection[mathutils.Vector]
    """

    float_vector: BMLayerCollection[mathutils.Vector]
    """ Generic 3D vector with float precision custom-data layer.

    :type: BMLayerCollection[mathutils.Vector]
    """

    int: BMLayerCollection[int]
    """ Generic int custom-data layer.

    :type: BMLayerCollection[int]
    """

    shape: BMLayerCollection[mathutils.Vector]
    """ Vertex shapekey absolute location (as a 3D Vector).

    :type: BMLayerCollection[mathutils.Vector]
    """

    skin: typing.Any
    """ Accessor for skin layer."""

    string: BMLayerCollection[bytes]
    """ Generic string custom-data layer (exposed as bytes, 255 max length).

    :type: BMLayerCollection[bytes]
    """

class BMLayerCollection[_GenericType1]:
    """Gives access to a collection of custom-data layers of the same type and behaves like Python dictionaries, except for the ability to do list like index access."""

    active: BMLayerItem[_GenericType1]
    """ 

    :type: BMLayerItem[_GenericType1]
    """

    is_singleton: bool
    """ True if there can exists only one layer of this type (read-only).

    :type: bool
    """

    def get[_GenericType2](
        self, key: str, default: _GenericType2 = None
    ) -> BMLayerItem[_GenericType1] | _GenericType2:
        """Returns the value of the layer matching the key or default
        when not found (matches Python's dictionary function of the same name).

                :param key: The key associated with the layer.
                :type key: str
                :param default: Optional argument for the value to return if
        key is not found.
                :type default: _GenericType2
                :return:
                :rtype: BMLayerItem[_GenericType1] | _GenericType2
        """

    def items(self) -> list[str, BMLayerItem[_GenericType1]]:
        """Return the identifiers of collection members
        (matching Python's dict.items() functionality).

                :return: (key, value) pairs for each member of this collection.
                :rtype: list[str, BMLayerItem[_GenericType1]]
        """

    def keys(self) -> list[str]:
        """Return the identifiers of collection members
        (matching Python's dict.keys() functionality).

                :return: the identifiers for each member of this collection.
                :rtype: list[str]
        """

    def new(self, name: str | None = "") -> BMLayerItem[_GenericType1]:
        """Create a new layer

        :param name: Optional name argument (will be made unique).
        :type name: str | None
        :return: The newly created layer.
        :rtype: BMLayerItem[_GenericType1]
        """

    def remove(self, layer: BMLayerItem[_GenericType1]):
        """Remove a layer

        :param layer: The layer to remove.
        :type layer: BMLayerItem[_GenericType1]
        """

    def values(self) -> list[BMLayerItem[_GenericType1]]:
        """Return the values of collection
        (matching Python's dict.values() functionality).

                :return: the members of this collection.
                :rtype: list[BMLayerItem[_GenericType1]]
        """

    def verify(self) -> BMLayerItem[_GenericType1]:
        """Create a new layer or return an existing active layer

        :return: The newly verified layer.
        :rtype: BMLayerItem[_GenericType1]
        """

class BMLayerItem[_GenericType1]:
    """Exposes a single custom data layer, their main purpose is for use as item accessors to custom-data when used with vert/edge/face/loop data."""

    name: str
    """ The layers unique name (read-only).

    :type: str
    """

    def copy_from(self, other: typing_extensions.Self):
        """Return a copy of the layer

        :param other: Another layer to copy from.
        :type other: typing_extensions.Self
        """

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

    link_loop_next: typing_extensions.Self
    """ The next face corner (read-only).

    :type: typing_extensions.Self
    """

    link_loop_prev: typing_extensions.Self
    """ The previous face corner (read-only).

    :type: typing_extensions.Self
    """

    link_loop_radial_next: typing_extensions.Self
    """ The next loop around the edge (read-only).

    :type: typing_extensions.Self
    """

    link_loop_radial_prev: typing_extensions.Self
    """ The previous loop around the edge (read-only).

    :type: typing_extensions.Self
    """

    link_loops: BMElemSeq[BMLoop]
    """ Loops connected to this loop, (read-only).

    :type: BMElemSeq[BMLoop]
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

    def calc_normal(self) -> mathutils.Vector:
        """Return normal at this loops corner of the face.
        Falls back to the face normal for straight lines.

                :return: a normalized vector.
                :rtype: mathutils.Vector
        """

    def calc_tangent(self) -> mathutils.Vector:
        """Return the tangent at this loops corner of the face (pointing inward into the face).
        Falls back to the face normal for straight lines.

                :return: a normalized vector.
                :rtype: mathutils.Vector
        """

    def copy_from(self, other: typing_extensions.Self):
        """Copy values from another element of matching type.

        :param other:
        :type other: typing_extensions.Self
        """

    def copy_from_face_interp(
        self, face: BMFace, vert: bool = True, multires: bool = True
    ):
        """Interpolate the customdata from a face onto this loop (the loops vert should overlap the face).

        :param face: The face to interpolate data from.
        :type face: BMFace
        :param vert: When enabled, interpolate the loops vertex data (optional).
        :type vert: bool
        :param multires: When enabled, interpolate the loops multires data (optional).
        :type multires: bool
        """

    def __getitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1]
    ) -> _GenericType1:
        """

        :param key:
        :type key: BMLayerItem[_GenericType1]
        :return:
        :rtype: _GenericType1
        """

    def __setitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1], value: _GenericType1
    ):
        """

        :param key:
        :type key: BMLayerItem[_GenericType1]
        :param value:
        :type value: _GenericType1
        """

    def __delitem__[_GenericType1](self, key: BMLayerItem[_GenericType1]):
        """

        :param key:
        :type key: BMLayerItem[_GenericType1]
        """

class BMLoopSeq:
    layers: BMLayerAccessLoop
    """ custom-data layers (read-only).

    :type: BMLayerAccessLoop
    """

    @typing.overload
    def __getitem__(self, key: int) -> BMLoop:
        """

        :param key:
        :type key: int
        :return:
        :rtype: BMLoop
        """

    @typing.overload
    def __getitem__(self, key: slice) -> list[BMLoop, ...]:
        """

        :param key:
        :type key: slice
        :return:
        :rtype: list[BMLoop, ...]
        """

    def __iter__(self) -> BMIter[BMLoop]:
        """

        :return:
        :rtype: BMIter[BMLoop]
        """

    def __len__(self) -> int:
        """

        :return:
        :rtype: int
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

    link_edges: BMElemSeq[BMEdge]
    """ Edges connected to this vertex (read-only).

    :type: BMElemSeq[BMEdge]
    """

    link_faces: BMElemSeq[BMFace]
    """ Faces connected to this vertex (read-only).

    :type: BMElemSeq[BMFace]
    """

    link_loops: BMElemSeq[BMLoop]
    """ Loops that use this vertex (read-only).

    :type: BMElemSeq[BMLoop]
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

    def calc_edge_angle(self, fallback: typing.Any | None = None) -> float:
        """Return the angle between this vert's two connected edges.

                :param fallback: return this when the vert doesn't have 2 edges
        (instead of raising a `ValueError`).
                :type fallback: typing.Any | None
                :return: Angle between edges in radians.
                :rtype: float
        """

    def calc_shell_factor(self) -> float:
        """Return a multiplier calculated based on the sharpness of the vertex.
        Where a flat surface gives 1.0, and higher values sharper edges.
        This is used to maintain shell thickness when offsetting verts along their normals.

                :return: offset multiplier
                :rtype: float
        """

    def copy_from(self, other: typing_extensions.Self):
        """Copy values from another element of matching type.

        :param other:
        :type other: typing_extensions.Self
        """

    def copy_from_face_interp(self, face: BMFace):
        """Interpolate the customdata from a face onto this loop (the loops vert should overlap the face).

        :param face: The face to interpolate data from.
        :type face: BMFace
        """

    def copy_from_vert_interp(
        self, vert_pair: collections.abc.Sequence[BMVert], fac: float
    ):
        """Interpolate the customdata from a vert between 2 other verts.

        :param vert_pair: The verts between which to interpolate data from.
        :type vert_pair: collections.abc.Sequence[BMVert]
        :param fac:
        :type fac: float
        """

    def hide_set(self, hide: bool):
        """Set the hide state.
        This is different from the hide attribute because it updates the selection and hide state of associated geometry.

                :param hide: Hidden or visible.
                :type hide: bool
        """

    def normal_update(self):
        """Update vertex normal.
        This does not update the normals of adjoining faces.

        """

    def select_set(self, select: bool):
        """Set the selection.
        This is different from the select attribute because it updates the selection state of associated geometry.

                :param select: Select or de-select.
                :type select: bool
        """

    def __getitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1]
    ) -> _GenericType1:
        """

        :param key:
        :type key: BMLayerItem[_GenericType1]
        :return:
        :rtype: _GenericType1
        """

    def __setitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1], value: _GenericType1
    ):
        """

        :param key:
        :type key: BMLayerItem[_GenericType1]
        :param value:
        :type value: _GenericType1
        """

    def __delitem__[_GenericType1](self, key: BMLayerItem[_GenericType1]):
        """

        :param key:
        :type key: BMLayerItem[_GenericType1]
        """

class BMVertSeq:
    layers: BMLayerAccessVert
    """ custom-data layers (read-only).

    :type: BMLayerAccessVert
    """

    def ensure_lookup_table(self):
        """Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg bm.verts[index].This needs to be called again after adding/removing data in this sequence."""

    def index_update(self):
        """Initialize the index values of this sequence.This is the equivalent of looping over all elements and assigning the index values."""

    def new(
        self,
        co: collections.abc.Sequence[float] | mathutils.Vector = (0.0, 0.0, 0.0),
        example: BMVert | None = None,
    ) -> BMVert:
        """Create a new vertex.

        :param co: The initial location of the vertex (optional argument).
        :type co: collections.abc.Sequence[float] | mathutils.Vector
        :param example: Existing vert to initialize settings.
        :type example: BMVert | None
        :return: The newly created vertex.
        :rtype: BMVert
        """

    def remove(self, vert: BMVert):
        """Remove a vert.

        :param vert:
        :type vert: BMVert
        """

    def sort(
        self,
        key: None
        | collections.abc.Callable[[BMVert | BMEdge | BMFace], int]
        | None = None,
        reverse: bool = False,
    ):
        """Sort the elements of this sequence, using an optional custom sort key.
        Indices of elements are not changed, `BMElemSeq.index_update` can be used for that.

                :param key: The key that sets the ordering of the elements.
                :type key: None | collections.abc.Callable[[BMVert | BMEdge | BMFace], int] | None
                :param reverse: Reverse the order of the elements
                :type reverse: bool
        """

    @typing.overload
    def __getitem__(self, key: int) -> BMVert:
        """

        :param key:
        :type key: int
        :return:
        :rtype: BMVert
        """

    @typing.overload
    def __getitem__(self, key: slice) -> list[BMVert, ...]:
        """

        :param key:
        :type key: slice
        :return:
        :rtype: list[BMVert, ...]
        """

    def __iter__(self) -> BMIter[BMVert]:
        """

        :return:
        :rtype: BMIter[BMVert]
        """

    def __len__(self) -> int:
        """

        :return:
        :rtype: int
        """

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

    def calc_loop_triangles(self) -> list[tuple[BMLoop, BMLoop, BMLoop]]:
        """Calculate triangle tessellation from quads/ngons.

        :return: The triangulated faces.
        :rtype: list[tuple[BMLoop, BMLoop, BMLoop]]
        """

    def calc_volume(self, signed: bool = False) -> float:
        """Calculate mesh volume based on face normals.

        :param signed: when signed is true, negative values may be returned.
        :type signed: bool
        :return: The volume of the mesh.
        :rtype: float
        """

    def clear(self):
        """Clear all mesh data."""

    def copy(self) -> typing_extensions.Self:
        """

        :return: A copy of this BMesh.
        :rtype: typing_extensions.Self
        """

    def free(self):
        """Explicitly free the BMesh data from memory, causing exceptions on further access."""

    def from_mesh(
        self,
        mesh: bpy.types.Mesh,
        face_normals: bool = True,
        vertex_normals: bool = True,
        use_shape_key: bool = False,
        shape_key_index: int = 0,
    ):
        """Initialize this bmesh from existing mesh datablock.

        :param mesh: The mesh data to load.
        :type mesh: bpy.types.Mesh
        :param face_normals:
        :type face_normals: bool
        :param vertex_normals:
        :type vertex_normals: bool
        :param use_shape_key: Use the locations from a shape key.
        :type use_shape_key: bool
        :param shape_key_index: The shape key index to use.
        :type shape_key_index: int
        """

    def from_object(
        self,
        object: bpy.types.Object,
        depsgraph: bpy.types.Depsgraph,
        cage: bool = False,
        face_normals: bool = True,
        vertex_normals: bool = True,
    ):
        """Initialize this bmesh from existing object data-block (only meshes are currently supported).

        :param object: The object data to load.
        :type object: bpy.types.Object
        :param depsgraph:
        :type depsgraph: bpy.types.Depsgraph
        :param cage: Get the mesh as a deformed cage.
        :type cage: bool
        :param face_normals: Calculate face normals.
        :type face_normals: bool
        :param vertex_normals: Calculate vertex normals.
        :type vertex_normals: bool
        """

    def normal_update(self):
        """Update normals of mesh faces and verts."""

    def select_flush(self, select: bool):
        """Flush selection, independent of the current selection mode.

        :param select: flush selection or de-selected elements.
        :type select: bool
        """

    def select_flush_mode(self):
        """flush selection based on the current mode current `BMesh.select_mode`."""

    def to_mesh(self, mesh: bpy.types.Mesh):
        """Writes this BMesh data into an existing Mesh datablock.

        :param mesh: The mesh data to write into.
        :type mesh: bpy.types.Mesh
        """

    def transform(
        self,
        matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
        | mathutils.Matrix,
        filter=None,
    ):
        """Transform the mesh (optionally filtering flagged data only).

        :param matrix: 4x4x transform matrix.
        :type matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix
        :param filter: set of values in ('SELECT', 'HIDE', 'SEAM', 'SMOOTH', 'TAG').
        """
