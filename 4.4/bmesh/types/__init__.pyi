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
import numpy.typing as npt
import bpy.types
import mathutils

class BMDeformVert:
    def clear(self) -> None:
        """Clears all weights."""

    def get(self, key: int, default: typing.Any | None = None) -> None:
        """Returns the deform weight matching the key or default
        when not found (matches Pythons dictionary function of the same name).

                :param key: The key associated with deform weight.
                :param default: Optional argument for the value to return if
        key is not found.
        """

    def items(self) -> list[tuple[int, float]]:
        """Return (group, weight) pairs for this vertex
        (matching Pythons dict.items() functionality).

                :return: (key, value) pairs for each deform weight of this vertex.
        """

    def keys(self) -> list[int]:
        """Return the group indices used by this vertex
        (matching Pythons dict.keys() functionality).

                :return: the deform group this vertex uses
        """

    def values(self) -> list[float]:
        """Return the weights of the deform vertex
        (matching Pythons dict.values() functionality).

                :return: The weights that influence this vertex
        """

class BMEdge:
    """The BMesh edge connecting 2 verts"""

    hide: bool
    """ Hidden state of this element."""

    index: int
    """ Index of this element."""

    is_boundary: bool
    """ True when this edge is at the boundary of a face (read-only)."""

    is_contiguous: bool
    """ True when this edge is manifold, between two faces with the same winding (read-only)."""

    is_convex: bool
    """ True when this edge joins two convex faces, depends on a valid face normal (read-only)."""

    is_manifold: bool
    """ True when this edge is manifold (read-only)."""

    is_valid: bool
    """ True when this element is valid (hasn't been removed)."""

    is_wire: bool
    """ True when this edge is not connected to any faces (read-only)."""

    link_faces: BMElemSeq[BMFace]
    """ Faces connected to this edge, (read-only)."""

    link_loops: BMElemSeq[BMLoop]
    """ Loops connected to this edge, (read-only)."""

    seam: bool
    """ Seam for UV unwrapping."""

    select: bool
    """ Selected state of this element."""

    smooth: bool
    """ Smooth state of this element."""

    tag: bool
    """ Generic attribute scripts can use for own logic"""

    verts: BMElemSeq[BMVert]
    """ Verts this edge uses (always 2), (read-only)."""

    def calc_face_angle(self, fallback: typing.Any | None = None) -> float:
        """

                :param fallback: return this when the edge doesnt have 2 faces
        (instead of raising a `ValueError`).
                :return: The angle between 2 connected faces in radians.
        """

    def calc_face_angle_signed(self, fallback: typing.Any | None = None) -> float:
        """

                :param fallback: return this when the edge doesnt have 2 faces
        (instead of raising a `ValueError`).
                :return: The angle between 2 connected faces in radians (negative for concave join).
        """

    def calc_length(self) -> float:
        """

        :return: The length between both verts.
        """

    def calc_tangent(self, loop: BMLoop) -> mathutils.Vector:
        """Return the tangent at this edge relative to a face (pointing inward into the face).
        This uses the face normal for calculation.

                :param loop: The loop used for tangent calculation.
                :return: a normalized vector.
        """

    def copy_from(self, other: typing_extensions.Self) -> None:
        """Copy values from another element of matching type.

        :param other:
        """

    def hide_set(self, hide: bool) -> None:
        """Set the hide state.
        This is different from the hide attribute because it updates the selection and hide state of associated geometry.

                :param hide: Hidden or visible.
        """

    def normal_update(self) -> None:
        """Update normals of all connected faces and the edge verts."""

    def other_vert(self, vert: BMVert) -> BMVert | None:
        """Return the other vertex on this edge or None if the vertex is not used by this edge.

        :param vert: a vert in this edge.
        :return: The edges other vert.
        """

    def select_set(self, select: bool) -> None:
        """Set the selection.
        This is different from the select attribute because it updates the selection state of associated geometry.

                :param select: Select or de-select.
        """

    def __getitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1]
    ) -> _GenericType1:
        """

        :param key:
        :return:
        """

    def __setitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1], value: _GenericType1
    ) -> None:
        """

        :param key:
        :param value:
        """

    def __delitem__[_GenericType1](self, key: BMLayerItem[_GenericType1]) -> None:
        """

        :param key:
        """

class BMEdgeSeq:
    layers: BMLayerAccessEdge
    """ custom-data layers (read-only)."""

    def ensure_lookup_table(self) -> None:
        """Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg bm.verts[index].This needs to be called again after adding/removing data in this sequence."""

    def get(self, verts: collections.abc.Sequence[BMVert], fallback=None) -> BMEdge:
        """Return an edge which uses the verts passed.

        :param verts: Sequence of verts.
        :param fallback: Return this value if nothing is found.
        :return: The edge found or None
        """

    def index_update(self) -> None:
        """Initialize the index values of this sequence.This is the equivalent of looping over all elements and assigning the index values."""

    def new(
        self, verts: collections.abc.Sequence[BMVert], example: BMEdge | None = None
    ) -> BMEdge:
        """Create a new edge from a given pair of verts.

        :param verts: Vertex pair.
        :param example: Existing edge to initialize settings (optional argument).
        :return: The newly created edge.
        """

    def remove(self, edge: BMEdge) -> None:
        """Remove an edge.

        :param edge:
        """

    def sort(
        self,
        key: None
        | collections.abc.Callable[[BMVert | BMEdge | BMFace], int]
        | None = None,
        reverse: bool = False,
    ) -> None:
        """Sort the elements of this sequence, using an optional custom sort key.
        Indices of elements are not changed, `BMElemSeq.index_update` can be used for that.

                :param key: The key that sets the ordering of the elements.
                :param reverse: Reverse the order of the elements
        """

    @typing.overload
    def __getitem__(self, key: int) -> BMEdge:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __getitem__(self, key: slice) -> list[BMEdge]:
        """

        :param key:
        :return:
        """

    def __iter__(self) -> BMIter[BMEdge]:
        """

        :return:
        """

    def __len__(self) -> int:
        """

        :return:
        """

class BMEditSelIter: ...

class BMEditSelSeq:
    active: BMEdge | BMFace | BMVert
    """ The last selected element or None (read-only)."""

    def add(self, element) -> None:
        """Add an element to the selection history (no action taken if its already added).

        :param element:
        """

    def clear(self) -> None:
        """Empties the selection history."""

    def discard(self, element) -> None:
        """Discard an element from the selection history.Like remove but doesnt raise an error when the elements not in the selection list.

        :param element:
        """

    def remove(self, element) -> None:
        """Remove an element from the selection history.

        :param element:
        """

    def validate(self) -> None:
        """Ensures all elements in the selection history are selected."""

class BMElemSeq[_GenericType1]:
    """General sequence type used for accessing any sequence of
    `BMVert`, `BMEdge`, `BMFace`, `BMLoop`.When accessed via `BMesh.verts`, `BMesh.edges`, `BMesh.faces`
    there are also functions to create/remove items.
    """

    def index_update(self) -> None:
        """Initialize the index values of this sequence.This is the equivalent of looping over all elements and assigning the index values."""

    @typing.overload
    def __getitem__(self, key: int) -> _GenericType1:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __getitem__(self, key: slice) -> list[_GenericType1]:
        """

        :param key:
        :return:
        """

    def __iter__(self) -> BMIter[_GenericType1]:
        """

        :return:
        """

    def __len__(self) -> int:
        """

        :return:
        """

class BMFace:
    """The BMesh face with 3 or more sides"""

    edges: BMElemSeq[BMEdge]
    """ Edges of this face, (read-only)."""

    hide: bool
    """ Hidden state of this element."""

    index: int
    """ Index of this element."""

    is_valid: bool
    """ True when this element is valid (hasn't been removed)."""

    loops: BMElemSeq[BMLoop]
    """ Loops of this face, (read-only)."""

    material_index: int
    """ The face's material index."""

    normal: mathutils.Vector
    """ The normal for this face as a 3D, wrapped vector."""

    select: bool
    """ Selected state of this element."""

    smooth: bool
    """ Smooth state of this element."""

    tag: bool
    """ Generic attribute scripts can use for own logic"""

    verts: BMElemSeq[BMVert]
    """ Verts of this face, (read-only)."""

    def calc_area(self) -> float:
        """Return the area of the face.

        :return: Return the area of the face.
        """

    def calc_center_bounds(self) -> mathutils.Vector:
        """Return bounds center of the face.

        :return: a 3D vector.
        """

    def calc_center_median(self) -> mathutils.Vector:
        """Return median center of the face.

        :return: a 3D vector.
        """

    def calc_center_median_weighted(self) -> mathutils.Vector:
        """Return median center of the face weighted by edge lengths.

        :return: a 3D vector.
        """

    def calc_perimeter(self) -> float:
        """Return the perimeter of the face.

        :return: Return the perimeter of the face.
        """

    def calc_tangent_edge(self) -> mathutils.Vector:
        """Return face tangent based on longest edge.

        :return: a normalized vector.
        """

    def calc_tangent_edge_diagonal(self) -> mathutils.Vector:
        """Return face tangent based on the edge farthest from any vertex.

        :return: a normalized vector.
        """

    def calc_tangent_edge_pair(self) -> mathutils.Vector:
        """Return face tangent based on the two longest disconnected edges.

        :return: a normalized vector.
        """

    def calc_tangent_vert_diagonal(self) -> mathutils.Vector:
        """Return face tangent based on the two most distant vertices.

        :return: a normalized vector.
        """

    def copy(self, verts: bool = True, edges: bool = True) -> typing_extensions.Self:
        """Make a copy of this face.

        :param verts: When set, the faces verts will be duplicated too.
        :param edges: When set, the faces edges will be duplicated too.
        :return: The newly created face.
        """

    def copy_from(self, other: typing_extensions.Self) -> None:
        """Copy values from another element of matching type.

        :param other:
        """

    def copy_from_face_interp(
        self, face: typing_extensions.Self, vert: bool = True
    ) -> None:
        """Interpolate the customdata from another face onto this one (faces should overlap).

        :param face: The face to interpolate data from.
        :param vert: When True, also copy vertex data.
        """

    def hide_set(self, hide: bool) -> None:
        """Set the hide state.
        This is different from the hide attribute because it updates the selection and hide state of associated geometry.

                :param hide: Hidden or visible.
        """

    def normal_flip(self) -> None:
        """Reverses winding of a face, which flips its normal."""

    def normal_update(self) -> None:
        """Update face normal based on the positions of the face verts.
        This does not update the normals of face verts.

        """

    def select_set(self, select: bool) -> None:
        """Set the selection.
        This is different from the select attribute because it updates the selection state of associated geometry.

                :param select: Select or de-select.
        """

    def __getitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1]
    ) -> _GenericType1:
        """

        :param key:
        :return:
        """

    def __setitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1], value: _GenericType1
    ) -> None:
        """

        :param key:
        :param value:
        """

    def __delitem__[_GenericType1](self, key: BMLayerItem[_GenericType1]) -> None:
        """

        :param key:
        """

class BMFaceSeq:
    active: BMFace | None
    """ active face."""

    layers: BMLayerAccessFace
    """ custom-data layers (read-only)."""

    def ensure_lookup_table(self) -> None:
        """Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg bm.verts[index].This needs to be called again after adding/removing data in this sequence."""

    def get(self, verts: collections.abc.Sequence[BMVert], fallback=None) -> BMFace:
        """Return a face which uses the verts passed.

        :param verts: Sequence of verts.
        :param fallback: Return this value if nothing is found.
        :return: The face found or None
        """

    def index_update(self) -> None:
        """Initialize the index values of this sequence.This is the equivalent of looping over all elements and assigning the index values."""

    def new(
        self, verts: collections.abc.Sequence[BMVert], example: BMFace | None = None
    ) -> BMFace:
        """Create a new face from a given set of verts.

        :param verts: Sequence of 3 or more verts.
        :param example: Existing face to initialize settings (optional argument).
        :return: The newly created face.
        """

    def remove(self, face: BMFace) -> None:
        """Remove a face.

        :param face:
        """

    def sort(
        self,
        key: None
        | collections.abc.Callable[[BMVert | BMEdge | BMFace], int]
        | None = None,
        reverse: bool = False,
    ) -> None:
        """Sort the elements of this sequence, using an optional custom sort key.
        Indices of elements are not changed, `BMElemSeq.index_update` can be used for that.

                :param key: The key that sets the ordering of the elements.
                :param reverse: Reverse the order of the elements
        """

    @typing.overload
    def __getitem__(self, key: int) -> BMFace:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __getitem__(self, key: slice) -> list[BMFace]:
        """

        :param key:
        :return:
        """

    def __iter__(self) -> BMIter[BMFace]:
        """

        :return:
        """

    def __len__(self) -> int:
        """

        :return:
        """

class BMIter[_GenericType1]:
    """Internal BMesh type for looping over verts/faces/edges,
    used for iterating over `BMElemSeq` types.
    """

    def __iter__(self) -> BMIter[_GenericType1]:
        """

        :return:
        """

    def __next__(self) -> _GenericType1:
        """

        :return:
        """

class BMLayerAccessEdge:
    """Exposes custom-data layer attributes."""

    bool: BMLayerCollection[boolean]
    """ Generic boolean custom-data layer."""

    color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with 8-bit precision custom-data layer."""

    float: BMLayerCollection[float]
    """ Generic float custom-data layer."""

    float_color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with float precision custom-data layer."""

    float_vector: BMLayerCollection[mathutils.Vector]
    """ Generic 3D vector with float precision custom-data layer."""

    freestyle: BMLayerCollection
    """ Accessor for Freestyle edge layer."""

    int: BMLayerCollection[int]
    """ Generic int custom-data layer."""

    string: BMLayerCollection[bytes]
    """ Generic string custom-data layer (exposed as bytes, 255 max length)."""

class BMLayerAccessFace:
    """Exposes custom-data layer attributes."""

    bool: BMLayerCollection[boolean]
    """ Generic boolean custom-data layer."""

    color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with 8-bit precision custom-data layer."""

    float: BMLayerCollection[float]
    """ Generic float custom-data layer."""

    float_color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with float precision custom-data layer."""

    float_vector: BMLayerCollection[mathutils.Vector]
    """ Generic 3D vector with float precision custom-data layer."""

    freestyle: BMLayerCollection
    """ Accessor for Freestyle face layer."""

    int: BMLayerCollection[int]
    """ Generic int custom-data layer."""

    string: BMLayerCollection[bytes]
    """ Generic string custom-data layer (exposed as bytes, 255 max length)."""

class BMLayerAccessLoop:
    """Exposes custom-data layer attributes."""

    bool: BMLayerCollection[boolean]
    """ Generic boolean custom-data layer."""

    color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with 8-bit precision custom-data layer."""

    float: BMLayerCollection[float]
    """ Generic float custom-data layer."""

    float_color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with float precision custom-data layer."""

    float_vector: BMLayerCollection[mathutils.Vector]
    """ Generic 3D vector with float precision custom-data layer."""

    int: BMLayerCollection[int]
    """ Generic int custom-data layer."""

    string: BMLayerCollection[bytes]
    """ Generic string custom-data layer (exposed as bytes, 255 max length)."""

    uv: BMLayerCollection[BMLoopUV]
    """ Accessor for `BMLoopUV` UV (as a 2D Vector)."""

class BMLayerAccessVert:
    """Exposes custom-data layer attributes."""

    bool: BMLayerCollection[boolean]
    """ Generic boolean custom-data layer."""

    color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with 8-bit precision custom-data layer."""

    deform: BMLayerCollection[BMDeformVert]
    """ Vertex deform weight `BMDeformVert` (TODO)."""

    float: BMLayerCollection[float]
    """ Generic float custom-data layer."""

    float_color: BMLayerCollection[mathutils.Vector]
    """ Generic RGBA color with float precision custom-data layer."""

    float_vector: BMLayerCollection[mathutils.Vector]
    """ Generic 3D vector with float precision custom-data layer."""

    int: BMLayerCollection[int]
    """ Generic int custom-data layer."""

    shape: BMLayerCollection[mathutils.Vector]
    """ Vertex shapekey absolute location (as a 3D Vector)."""

    skin: typing.Any
    """ Accessor for skin layer."""

    string: BMLayerCollection[bytes]
    """ Generic string custom-data layer (exposed as bytes, 255 max length)."""

class BMLayerCollection[_GenericType1]:
    """Gives access to a collection of custom-data layers of the same type and behaves like Python dictionaries, except for the ability to do list like index access."""

    active: BMLayerItem[_GenericType1]
    is_singleton: bool
    """ True if there can exists only one layer of this type (read-only)."""

    def get[_GenericType2](
        self, key: str, default: _GenericType2 = None
    ) -> BMLayerItem[_GenericType1] | _GenericType2:
        """Returns the value of the layer matching the key or default
        when not found (matches Pythons dictionary function of the same name).

                :param key: The key associated with the layer.
                :param default: Optional argument for the value to return if
        key is not found.
                :return:
        """

    def items(self) -> list[str, BMLayerItem[_GenericType1]]:
        """Return the identifiers of collection members
        (matching Pythons dict.items() functionality).

                :return: (key, value) pairs for each member of this collection.
        """

    def keys(self) -> list[str]:
        """Return the identifiers of collection members
        (matching Pythons dict.keys() functionality).

                :return: the identifiers for each member of this collection.
        """

    def new(self, name: str | None = "") -> BMLayerItem[_GenericType1]:
        """Create a new layer

        :param name: Optional name argument (will be made unique).
        :return: The newly created layer.
        """

    def remove(self, layer: BMLayerItem[_GenericType1]) -> None:
        """Remove a layer

        :param layer: The layer to remove.
        """

    def values(self) -> list[BMLayerItem[_GenericType1]]:
        """Return the values of collection
        (matching Pythons dict.values() functionality).

                :return: the members of this collection.
        """

    def verify(self) -> BMLayerItem[_GenericType1]:
        """Create a new layer or return an existing active layer

        :return: The newly verified layer.
        """

class BMLayerItem[_GenericType1]:
    """Exposes a single custom data layer, their main purpose is for use as item accessors to custom-data when used with vert/edge/face/loop data."""

    name: str
    """ The layers unique name (read-only)."""

    def copy_from(self, other: typing_extensions.Self) -> None:
        """Return a copy of the layer

        :param other: Another layer to copy from.
        """

class BMLoop:
    """This is normally accessed from `BMFace.loops` where each face loop represents a corner of the face."""

    edge: BMEdge
    """ The loop's edge (between this loop and the next), (read-only)."""

    face: BMFace
    """ The face this loop makes (read-only)."""

    index: int
    """ Index of this element."""

    is_convex: bool
    """ True when this loop is at the convex corner of a face, depends on a valid face normal (read-only)."""

    is_valid: bool
    """ True when this element is valid (hasn't been removed)."""

    link_loop_next: typing_extensions.Self
    """ The next face corner (read-only)."""

    link_loop_prev: typing_extensions.Self
    """ The previous face corner (read-only)."""

    link_loop_radial_next: typing_extensions.Self
    """ The next loop around the edge (read-only)."""

    link_loop_radial_prev: typing_extensions.Self
    """ The previous loop around the edge (read-only)."""

    link_loops: BMElemSeq[BMLoop]
    """ Loops connected to this loop, (read-only)."""

    tag: bool
    """ Generic attribute scripts can use for own logic"""

    vert: BMVert
    """ The loop's vertex (read-only)."""

    def calc_angle(self) -> float:
        """Return the angle at this loops corner of the face.
        This is calculated so sharper corners give lower angles.

                :return: The angle in radians.
        """

    def calc_normal(self) -> mathutils.Vector:
        """Return normal at this loops corner of the face.
        Falls back to the face normal for straight lines.

                :return: a normalized vector.
        """

    def calc_tangent(self) -> mathutils.Vector:
        """Return the tangent at this loops corner of the face (pointing inward into the face).
        Falls back to the face normal for straight lines.

                :return: a normalized vector.
        """

    def copy_from(self, other: typing_extensions.Self) -> None:
        """Copy values from another element of matching type.

        :param other:
        """

    def copy_from_face_interp(
        self, face: BMFace, vert: bool = True, multires: bool = True
    ) -> None:
        """Interpolate the customdata from a face onto this loop (the loops vert should overlap the face).

        :param face: The face to interpolate data from.
        :param vert: When enabled, interpolate the loops vertex data (optional).
        :param multires: When enabled, interpolate the loops multires data (optional).
        """

    def __getitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1]
    ) -> _GenericType1:
        """

        :param key:
        :return:
        """

    def __setitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1], value: _GenericType1
    ) -> None:
        """

        :param key:
        :param value:
        """

    def __delitem__[_GenericType1](self, key: BMLayerItem[_GenericType1]) -> None:
        """

        :param key:
        """

class BMLoopSeq:
    layers: BMLayerAccessLoop
    """ custom-data layers (read-only)."""

    @typing.overload
    def __getitem__(self, key: int) -> BMLoop:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __getitem__(self, key: slice) -> list[BMLoop]:
        """

        :param key:
        :return:
        """

    def __iter__(self) -> BMIter[BMLoop]:
        """

        :return:
        """

    def __len__(self) -> int:
        """

        :return:
        """

class BMLoopUV:
    pin_uv: bool
    """ UV pin state."""

    select: bool
    """ UV select state."""

    select_edge: bool
    """ UV edge select state."""

    uv: mathutils.Vector
    """ Loops UV (as a 2D Vector)."""

class BMVert:
    """The BMesh vertex type"""

    co: mathutils.Vector
    """ The coordinates for this vertex as a 3D, wrapped vector."""

    hide: bool
    """ Hidden state of this element."""

    index: int
    """ Index of this element."""

    is_boundary: bool
    """ True when this vertex is connected to boundary edges (read-only)."""

    is_manifold: bool
    """ True when this vertex is manifold (read-only)."""

    is_valid: bool
    """ True when this element is valid (hasn't been removed)."""

    is_wire: bool
    """ True when this vertex is not connected to any faces (read-only)."""

    link_edges: BMElemSeq[BMEdge]
    """ Edges connected to this vertex (read-only)."""

    link_faces: BMElemSeq[BMFace]
    """ Faces connected to this vertex (read-only)."""

    link_loops: BMElemSeq[BMLoop]
    """ Loops that use this vertex (read-only)."""

    normal: mathutils.Vector
    """ The normal for this vertex as a 3D, wrapped vector."""

    select: bool
    """ Selected state of this element."""

    tag: bool
    """ Generic attribute scripts can use for own logic"""

    def calc_edge_angle(self, fallback: typing.Any | None = None) -> float:
        """Return the angle between this verts two connected edges.

                :param fallback: return this when the vert doesnt have 2 edges
        (instead of raising a `ValueError`).
                :return: Angle between edges in radians.
        """

    def calc_shell_factor(self) -> float:
        """Return a multiplier calculated based on the sharpness of the vertex.
        Where a flat surface gives 1.0, and higher values sharper edges.
        This is used to maintain shell thickness when offsetting verts along their normals.

                :return: offset multiplier
        """

    def copy_from(self, other: typing_extensions.Self) -> None:
        """Copy values from another element of matching type.

        :param other:
        """

    def copy_from_face_interp(self, face: BMFace) -> None:
        """Interpolate the customdata from a face onto this loop (the loops vert should overlap the face).

        :param face: The face to interpolate data from.
        """

    def copy_from_vert_interp(
        self, vert_pair: collections.abc.Sequence[BMVert], fac: float
    ) -> None:
        """Interpolate the customdata from a vert between 2 other verts.

        :param vert_pair: The verts between which to interpolate data from.
        :param fac:
        """

    def hide_set(self, hide: bool) -> None:
        """Set the hide state.
        This is different from the hide attribute because it updates the selection and hide state of associated geometry.

                :param hide: Hidden or visible.
        """

    def normal_update(self) -> None:
        """Update vertex normal.
        This does not update the normals of adjoining faces.

        """

    def select_set(self, select: bool) -> None:
        """Set the selection.
        This is different from the select attribute because it updates the selection state of associated geometry.

                :param select: Select or de-select.
        """

    def __getitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1]
    ) -> _GenericType1:
        """

        :param key:
        :return:
        """

    def __setitem__[_GenericType1](
        self, key: BMLayerItem[_GenericType1], value: _GenericType1
    ) -> None:
        """

        :param key:
        :param value:
        """

    def __delitem__[_GenericType1](self, key: BMLayerItem[_GenericType1]) -> None:
        """

        :param key:
        """

class BMVertSeq:
    layers: BMLayerAccessVert
    """ custom-data layers (read-only)."""

    def ensure_lookup_table(self) -> None:
        """Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg bm.verts[index].This needs to be called again after adding/removing data in this sequence."""

    def index_update(self) -> None:
        """Initialize the index values of this sequence.This is the equivalent of looping over all elements and assigning the index values."""

    def new(
        self,
        co: collections.abc.Sequence[float] | mathutils.Vector = (0.0, 0.0, 0.0),
        example: BMVert | None = None,
    ) -> BMVert:
        """Create a new vertex.

        :param co: The initial location of the vertex (optional argument).
        :param example: Existing vert to initialize settings.
        :return: The newly created vertex.
        """

    def remove(self, vert: BMVert) -> None:
        """Remove a vert.

        :param vert:
        """

    def sort(
        self,
        key: None
        | collections.abc.Callable[[BMVert | BMEdge | BMFace], int]
        | None = None,
        reverse: bool = False,
    ) -> None:
        """Sort the elements of this sequence, using an optional custom sort key.
        Indices of elements are not changed, `BMElemSeq.index_update` can be used for that.

                :param key: The key that sets the ordering of the elements.
                :param reverse: Reverse the order of the elements
        """

    @typing.overload
    def __getitem__(self, key: int) -> BMVert:
        """

        :param key:
        :return:
        """

    @typing.overload
    def __getitem__(self, key: slice) -> list[BMVert]:
        """

        :param key:
        :return:
        """

    def __iter__(self) -> BMIter[BMVert]:
        """

        :return:
        """

    def __len__(self) -> int:
        """

        :return:
        """

class BMesh:
    """The BMesh data structure"""

    edges: BMEdgeSeq
    """ This meshes edge sequence (read-only)."""

    faces: BMFaceSeq
    """ This meshes face sequence (read-only)."""

    is_valid: bool
    """ True when this element is valid (hasn't been removed)."""

    is_wrapped: bool
    """ True when this mesh is owned by blender (typically the editmode BMesh)."""

    loops: BMLoopSeq
    """ This meshes loops (read-only)."""

    select_history: BMEditSelSeq
    """ Sequence of selected items (the last is displayed as active)."""

    select_mode: set
    """ The selection mode, values can be {'VERT', 'EDGE', 'FACE'}, can't be assigned an empty set."""

    verts: BMVertSeq
    """ This meshes vert sequence (read-only)."""

    def calc_loop_triangles(self) -> list[tuple[BMLoop, BMLoop, BMLoop]]:
        """Calculate triangle tessellation from quads/ngons.

        :return: The triangulated faces.
        """

    def calc_volume(self, signed: bool = False) -> float:
        """Calculate mesh volume based on face normals.

        :param signed: when signed is true, negative values may be returned.
        :return: The volume of the mesh.
        """

    def clear(self) -> None:
        """Clear all mesh data."""

    def copy(self) -> typing_extensions.Self:
        """

        :return: A copy of this BMesh.
        """

    def free(self) -> None:
        """Explicitly free the BMesh data from memory, causing exceptions on further access."""

    def from_mesh(
        self,
        mesh: bpy.types.Mesh,
        face_normals: bool = True,
        vertex_normals: bool = True,
        use_shape_key: bool = False,
        shape_key_index: int = 0,
    ) -> None:
        """Initialize this bmesh from existing mesh datablock.

        :param mesh: The mesh data to load.
        :param face_normals:
        :param vertex_normals:
        :param use_shape_key: Use the locations from a shape key.
        :param shape_key_index: The shape key index to use.
        """

    def from_object(
        self,
        object: bpy.types.Object,
        depsgraph: bpy.types.Depsgraph,
        cage: bool = False,
        face_normals: bool = True,
        vertex_normals: bool = True,
    ) -> None:
        """Initialize this bmesh from existing object data-block (only meshes are currently supported).

        :param object: The object data to load.
        :param depsgraph:
        :param cage: Get the mesh as a deformed cage.
        :param face_normals: Calculate face normals.
        :param vertex_normals: Calculate vertex normals.
        """

    def normal_update(self) -> None:
        """Update normals of mesh faces and verts."""

    def select_flush(self, select: bool) -> None:
        """Flush selection, independent of the current selection mode.

        :param select: flush selection or de-selected elements.
        """

    def select_flush_mode(self) -> None:
        """flush selection based on the current mode current `BMesh.select_mode`."""

    def to_mesh(self, mesh: bpy.types.Mesh) -> None:
        """Writes this BMesh data into an existing Mesh datablock.

        :param mesh: The mesh data to write into.
        """

    def transform(
        self,
        matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
        | mathutils.Matrix,
        filter: set[str] | None = None,
    ) -> None:
        """Transform the mesh (optionally filtering flagged data only).

        :param matrix: 4x4x transform matrix.
        :param filter: set of values in (SELECT, HIDE, SEAM, SMOOTH, TAG).
        """
