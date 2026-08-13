import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

class add_simple_uvs(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add cube map UVs on mesh

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class add_texture_paint_slot(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            "BASE_COLOR",
            "SPECULAR",
            "ROUGHNESS",
            "METALLIC",
            "NORMAL",
            "BUMP",
            "DISPLACEMENT",
        ]
        | None = "BASE_COLOR",
        slot_type: typing.Literal["IMAGE", "COLOR_ATTRIBUTE"] | None = "IMAGE",
        name: str = "Untitled",
        color: collections.abc.Sequence[float] | None = (0.0, 0.0, 0.0, 1.0),
        width: int | None = 1024,
        height: int | None = 1024,
        alpha: bool | None = True,
        generated_type: typing.Literal[
            bpy.stub_internal.rna_enums.ImageGeneratedTypeItems
        ]
        | None = "BLANK",
        float: bool | None = False,
        domain: typing.Literal[bpy.stub_internal.rna_enums.ColorAttributeDomainItems]
        | None = "POINT",
        data_type: typing.Literal[bpy.stub_internal.rna_enums.ColorAttributeTypeItems]
        | None = "FLOAT_COLOR",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a paint slot

        :param execution_context:
        :param undo:
        :param type: Material Layer Type, Material layer type of new paint slot (optional)
        :param slot_type: Slot Type, Type of new paint slot (optional)
        :param name: Name, Name for new paint slot source (optional, never None)
        :param color: Color, Default fill color (array of 4 items, in [0, inf], optional)
        :param width: Width, Image width (in [1, inf], optional)
        :param height: Height, Image height (in [1, inf], optional)
        :param alpha: Alpha, Create an image with an alpha channel (optional)
        :param generated_type: Generated Type, Fill the image with a grid for UV map testing (optional)
        :param float: 32-bit Float, Create image with 32-bit floating-point bit depth (optional)
        :param domain: Domain, Type of element that attribute is stored on (optional)
        :param data_type: Data Type, Type of data stored in attribute (optional)
        :return: Result of the operator call.
        """

class brush_colors_flip(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Swap primary and secondary brush colors

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class face_select_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"]
        | None = "TOGGLE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change selection for all faces

                :param execution_context:
                :param undo:
                :param action: Action, Selection action to execute (optional)

        TOGGLE
        Toggle -- Toggle selection for all elements.

        SELECT
        Select -- Select all elements.

        DESELECT
        Deselect -- Deselect all elements.

        INVERT
        Invert -- Invert selection of all elements.
                :return: Result of the operator call.
        """

class face_select_hide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        unselected: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Hide selected faces

        :param execution_context:
        :param undo:
        :param unselected: Unselected, Hide unselected rather than selected objects (optional)
        :return: Result of the operator call.
        """

class face_select_less(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        face_step: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Deselect Faces connected to existing selection

        :param execution_context:
        :param undo:
        :param face_step: Face Step, Also deselect faces that only touch on a corner (optional)
        :return: Result of the operator call.
        """

class face_select_linked(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select linked faces

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class face_select_linked_pick(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        deselect: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select linked faces under the cursor

        :param execution_context:
        :param undo:
        :param deselect: Deselect, Deselect rather than select items (optional)
        :return: Result of the operator call.
        """

class face_select_loop(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        select: bool | None = True,
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select face loop under the cursor

        :param execution_context:
        :param undo:
        :param select: Select, If false, faces will be deselected (optional)
        :param extend: Extend, Extend the selection (optional)
        :return: Result of the operator call.
        """

class face_select_more(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        face_step: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select Faces connected to existing selection

        :param execution_context:
        :param undo:
        :param face_step: Face Step, Also select faces that only touch on a corner (optional)
        :return: Result of the operator call.
        """

class face_vert_reveal(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        select: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reveal hidden faces and vertices

        :param execution_context:
        :param undo:
        :param select: Select, Specifies whether the newly revealed geometry should be selected (optional)
        :return: Result of the operator call.
        """

class grab_clone(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        delta: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move the clone source image

        :param execution_context:
        :param undo:
        :param delta: Delta, Delta offset of clone image in 0.0 to 1.0 coordinates (array of 2 items, in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class hide_show(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        xmin: int | None = 0,
        xmax: int | None = 0,
        ymin: int | None = 0,
        ymax: int | None = 0,
        wait_for_input: bool | None = True,
        action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
        area: typing.Literal["OUTSIDE", "Inside"] | None = "Inside",
        use_front_faces_only: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Hide/show some vertices

                :param execution_context:
                :param undo:
                :param xmin: X Min, (in [-inf, inf], optional)
                :param xmax: X Max, (in [-inf, inf], optional)
                :param ymin: Y Min, (in [-inf, inf], optional)
                :param ymax: Y Max, (in [-inf, inf], optional)
                :param wait_for_input: Wait for Input, (optional)
                :param action: Visibility Action, Whether to hide or show vertices (optional)

        HIDE
        Hide -- Hide vertices.

        SHOW
        Show -- Show vertices.
                :param area: Visibility Area, Which vertices to hide or show (optional)

        OUTSIDE
        Outside -- Hide or show vertices outside the selection.

        Inside
        Inside -- Hide or show vertices inside the selection.
                :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
                :return: Result of the operator call.
        """

class hide_show_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Hide/show all vertices

                :param execution_context:
                :param undo:
                :param action: Visibility Action, Whether to hide or show vertices (optional)

        HIDE
        Hide -- Hide vertices.

        SHOW
        Show -- Show vertices.
                :return: Result of the operator call.
        """

class hide_show_lasso_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
        use_smooth_stroke: bool | None = False,
        smooth_stroke_factor: float | None = 0.75,
        smooth_stroke_radius: int | None = 35,
        action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
        area: typing.Literal["OUTSIDE", "Inside"] | None = "Inside",
        use_front_faces_only: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Hide/show some vertices

                :param execution_context:
                :param undo:
                :param path: Path, (optional)
                :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
                :param smooth_stroke_factor: Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
                :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
                :param action: Visibility Action, Whether to hide or show vertices (optional)

        HIDE
        Hide -- Hide vertices.

        SHOW
        Show -- Show vertices.
                :param area: Visibility Area, Which vertices to hide or show (optional)

        OUTSIDE
        Outside -- Hide or show vertices outside the selection.

        Inside
        Inside -- Hide or show vertices inside the selection.
                :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
                :return: Result of the operator call.
        """

class hide_show_line_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        xstart: int | None = 0,
        xend: int | None = 0,
        ystart: int | None = 0,
        yend: int | None = 0,
        flip: bool | None = False,
        cursor: int | None = 5,
        action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
        area: typing.Literal["OUTSIDE", "Inside"] | None = "Inside",
        use_front_faces_only: bool | None = False,
        use_limit_to_segment: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Hide/show some vertices

                :param execution_context:
                :param undo:
                :param xstart: X Start, (in [-inf, inf], optional)
                :param xend: X End, (in [-inf, inf], optional)
                :param ystart: Y Start, (in [-inf, inf], optional)
                :param yend: Y End, (in [-inf, inf], optional)
                :param flip: Flip, (optional)
                :param cursor: Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
                :param action: Visibility Action, Whether to hide or show vertices (optional)

        HIDE
        Hide -- Hide vertices.

        SHOW
        Show -- Show vertices.
                :param area: Visibility Area, Which vertices to hide or show (optional)

        OUTSIDE
        Outside -- Hide or show vertices outside the selection.

        Inside
        Inside -- Hide or show vertices inside the selection.
                :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
                :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line (optional)
                :return: Result of the operator call.
        """

class hide_show_masked(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Hide/show all masked vertices above a threshold

                :param execution_context:
                :param undo:
                :param action: Visibility Action, Whether to hide or show vertices (optional)

        HIDE
        Hide -- Hide vertices.

        SHOW
        Show -- Show vertices.
                :return: Result of the operator call.
        """

class hide_show_polyline_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
        action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
        area: typing.Literal["OUTSIDE", "Inside"] | None = "Inside",
        use_front_faces_only: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Hide/show some vertices

                :param execution_context:
                :param undo:
                :param path: Path, (optional)
                :param action: Visibility Action, Whether to hide or show vertices (optional)

        HIDE
        Hide -- Hide vertices.

        SHOW
        Show -- Show vertices.
                :param area: Visibility Area, Which vertices to hide or show (optional)

        OUTSIDE
        Outside -- Hide or show vertices outside the selection.

        Inside
        Inside -- Hide or show vertices inside the selection.
                :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
                :return: Result of the operator call.
        """

class image_from_view(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        filepath: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make an image from biggest 3D view for reprojection

        :param execution_context:
        :param undo:
        :param filepath: File Path, Name of the file (optional, never None)
        :return: Result of the operator call.
        """

class image_paint(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
        | None = None,
        mode: typing.Literal["NORMAL", "INVERT"] | None = "NORMAL",
        brush_toggle: typing.Literal["None", "SMOOTH", "ERASE", "MASK"] | None = "None",
        pen_flip: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Paint a stroke into the image

                :param execution_context:
                :param undo:
                :param stroke: Stroke, (optional)
                :param mode: Stroke Mode, Action taken when a paint stroke is made (optional)

        NORMAL
        Regular -- Apply brush normally.

        INVERT
        Invert -- Invert action of brush for duration of stroke.
                :param brush_toggle: Temporary Brush Toggle Type, Brush to use for duration of stroke (optional)

        None
        None -- Apply brush normally.

        SMOOTH
        Smooth -- Switch to smooth brush for duration of stroke.

        ERASE
        Erase -- Switch to erase brush for duration of stroke.

        MASK
        Mask -- Switch to mask brush for duration of stroke.
                :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used (optional)
                :return: Result of the operator call.
        """

class mask_box_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        xmin: int | None = 0,
        xmax: int | None = 0,
        ymin: int | None = 0,
        ymax: int | None = 0,
        wait_for_input: bool | None = True,
        use_front_faces_only: bool | None = False,
        mode: typing.Literal["VALUE", "VALUE_INVERSE", "INVERT"] | None = "VALUE",
        value: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Mask within a rectangle defined by the cursor

                :param execution_context:
                :param undo:
                :param xmin: X Min, (in [-inf, inf], optional)
                :param xmax: X Max, (in [-inf, inf], optional)
                :param ymin: Y Min, (in [-inf, inf], optional)
                :param ymax: Y Max, (in [-inf, inf], optional)
                :param wait_for_input: Wait for Input, (optional)
                :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
                :param mode: Mode, (optional)

        VALUE
        Value -- Set mask to the level specified by the value property.

        VALUE_INVERSE
        Value Inverted -- Set mask to the level specified by the inverted value property.

        INVERT
        Invert -- Invert the mask.
                :param value: Value, Mask level to use when mode is Value; zero means no masking and one is fully masked (in [0, 1], optional)
                :return: Result of the operator call.
        """

class mask_flood_fill(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["VALUE", "VALUE_INVERSE", "INVERT"] | None = "VALUE",
        value: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Fill the whole mask with a given value, or invert its values

                :param execution_context:
                :param undo:
                :param mode: Mode, (optional)

        VALUE
        Value -- Set mask to the level specified by the value property.

        VALUE_INVERSE
        Value Inverted -- Set mask to the level specified by the inverted value property.

        INVERT
        Invert -- Invert the mask.
                :param value: Value, Mask level to use when mode is Value; zero means no masking and one is fully masked (in [0, 1], optional)
                :return: Result of the operator call.
        """

class mask_lasso_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
        use_smooth_stroke: bool | None = False,
        smooth_stroke_factor: float | None = 0.75,
        smooth_stroke_radius: int | None = 35,
        use_front_faces_only: bool | None = False,
        mode: typing.Literal["VALUE", "VALUE_INVERSE", "INVERT"] | None = "VALUE",
        value: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Mask within a shape defined by the cursor

                :param execution_context:
                :param undo:
                :param path: Path, (optional)
                :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
                :param smooth_stroke_factor: Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
                :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
                :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
                :param mode: Mode, (optional)

        VALUE
        Value -- Set mask to the level specified by the value property.

        VALUE_INVERSE
        Value Inverted -- Set mask to the level specified by the inverted value property.

        INVERT
        Invert -- Invert the mask.
                :param value: Value, Mask level to use when mode is Value; zero means no masking and one is fully masked (in [0, 1], optional)
                :return: Result of the operator call.
        """

class mask_line_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        xstart: int | None = 0,
        xend: int | None = 0,
        ystart: int | None = 0,
        yend: int | None = 0,
        flip: bool | None = False,
        cursor: int | None = 5,
        use_front_faces_only: bool | None = False,
        use_limit_to_segment: bool | None = False,
        mode: typing.Literal["VALUE", "VALUE_INVERSE", "INVERT"] | None = "VALUE",
        value: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Mask to one side of a line defined by the cursor

                :param execution_context:
                :param undo:
                :param xstart: X Start, (in [-inf, inf], optional)
                :param xend: X End, (in [-inf, inf], optional)
                :param ystart: Y Start, (in [-inf, inf], optional)
                :param yend: Y End, (in [-inf, inf], optional)
                :param flip: Flip, (optional)
                :param cursor: Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
                :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
                :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line (optional)
                :param mode: Mode, (optional)

        VALUE
        Value -- Set mask to the level specified by the value property.

        VALUE_INVERSE
        Value Inverted -- Set mask to the level specified by the inverted value property.

        INVERT
        Invert -- Invert the mask.
                :param value: Value, Mask level to use when mode is Value; zero means no masking and one is fully masked (in [0, 1], optional)
                :return: Result of the operator call.
        """

class mask_polyline_gesture(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
        use_front_faces_only: bool | None = False,
        mode: typing.Literal["VALUE", "VALUE_INVERSE", "INVERT"] | None = "VALUE",
        value: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Mask within a shape defined by the cursor

                :param execution_context:
                :param undo:
                :param path: Path, (optional)
                :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
                :param mode: Mode, (optional)

        VALUE
        Value -- Set mask to the level specified by the value property.

        VALUE_INVERSE
        Value Inverted -- Set mask to the level specified by the inverted value property.

        INVERT
        Invert -- Invert the mask.
                :param value: Value, Mask level to use when mode is Value; zero means no masking and one is fully masked (in [0, 1], optional)
                :return: Result of the operator call.
        """

class project_image(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        image: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Project an edited render from the active camera back onto the object

        :param execution_context:
        :param undo:
        :param image: Image, (optional)
        :return: Result of the operator call.
        """

class sample_color(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        location: collections.abc.Sequence[int] | None = (0, 0),
        merged: bool | None = False,
        palette: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Use the mouse to sample a color in the image

        :param execution_context:
        :param undo:
        :param location: Location, (array of 2 items, in [0, inf], optional)
        :param merged: Sample Merged, Sample the output display color (optional)
        :param palette: Add to Palette, (optional)
        :return: Result of the operator call.
        """

class texture_paint_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle texture paint mode in 3D view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vert_select_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"]
        | None = "TOGGLE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change selection for all vertices

                :param execution_context:
                :param undo:
                :param action: Action, Selection action to execute (optional)

        TOGGLE
        Toggle -- Toggle selection for all elements.

        SELECT
        Select -- Select all elements.

        DESELECT
        Deselect -- Deselect all elements.

        INVERT
        Invert -- Invert selection of all elements.
                :return: Result of the operator call.
        """

class vert_select_hide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        unselected: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Hide selected vertices

        :param execution_context:
        :param undo:
        :param unselected: Unselected, Hide unselected rather than selected vertices (optional)
        :return: Result of the operator call.
        """

class vert_select_less(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        face_step: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Deselect Vertices connected to existing selection

        :param execution_context:
        :param undo:
        :param face_step: Face Step, Also deselect faces that only touch on a corner (optional)
        :return: Result of the operator call.
        """

class vert_select_linked(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select linked vertices

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vert_select_linked_pick(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        select: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select linked vertices under the cursor

        :param execution_context:
        :param undo:
        :param select: Select, Whether to select or deselect linked vertices under the cursor (optional)
        :return: Result of the operator call.
        """

class vert_select_loop(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        select: bool | None = True,
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select vertex loop under the cursor

        :param execution_context:
        :param undo:
        :param select: Select, If false, vertices will be deselected (optional)
        :param extend: Extend, Extend the selection (optional)
        :return: Result of the operator call.
        """

class vert_select_more(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        face_step: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select Vertices connected to existing selection

        :param execution_context:
        :param undo:
        :param face_step: Face Step, Also select faces that only touch on a corner (optional)
        :return: Result of the operator call.
        """

class vert_select_ungrouped(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select vertices without a group

        :param execution_context:
        :param undo:
        :param extend: Extend, Extend the selection (optional)
        :return: Result of the operator call.
        """

class vertex_color_brightness_contrast(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        brightness: float | None = 0.0,
        contrast: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Adjust vertex color brightness/contrast

        :param execution_context:
        :param undo:
        :param brightness: Brightness, (in [-100, 100], optional)
        :param contrast: Contrast, (in [-100, 100], optional)
        :return: Result of the operator call.
        """

class vertex_color_dirt(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        blur_strength: float | None = 1.0,
        blur_iterations: int | None = 1,
        clean_angle: float | None = 3.14159,
        dirt_angle: float | None = 0.0,
        dirt_only: bool | None = False,
        normalize: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Generate a dirt map gradient based on cavity

        :param execution_context:
        :param undo:
        :param blur_strength: Blur Strength, Blur strength per iteration (in [0.01, 1], optional)
        :param blur_iterations: Blur Iterations, Number of times to blur the colors (higher blurs more) (in [0, 40], optional)
        :param clean_angle: Highlight Angle, Less than 90 limits the angle used in the tonal range (in [0, 3.14159], optional)
        :param dirt_angle: Dirt Angle, Less than 90 limits the angle used in the tonal range (in [0, 3.14159], optional)
        :param dirt_only: Dirt Only, Dont calculate cleans for convex areas (optional)
        :param normalize: Normalize, Normalize the colors, increasing the contrast (optional)
        :return: Result of the operator call.
        """

class vertex_color_from_weight(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Convert active weight into gray scale vertex colors

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertex_color_hsv(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        h: float | None = 0.5,
        s: float | None = 1.0,
        v: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Adjust vertex color Hue/Saturation/Value

        :param execution_context:
        :param undo:
        :param h: Hue, (in [0, 1], optional)
        :param s: Saturation, (in [0, 2], optional)
        :param v: Value, (in [0, 2], optional)
        :return: Result of the operator call.
        """

class vertex_color_invert(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Invert RGB values

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertex_color_levels(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        offset: float | None = 0.0,
        gain: float | None = 1.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Adjust levels of vertex colors

        :param execution_context:
        :param undo:
        :param offset: Offset, Value to add to colors (in [-1, 1], optional)
        :param gain: Gain, Value to multiply colors by (in [0, inf], optional)
        :return: Result of the operator call.
        """

class vertex_color_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        use_alpha: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Fill the active vertex color layer with the current paint color

        :param execution_context:
        :param undo:
        :param use_alpha: Affect Alpha, Set color completely opaque instead of reusing existing alpha (optional)
        :return: Result of the operator call.
        """

class vertex_color_smooth(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Smooth colors across vertices

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class vertex_paint(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
        | None = None,
        mode: typing.Literal["NORMAL", "INVERT"] | None = "NORMAL",
        brush_toggle: typing.Literal["None", "SMOOTH", "ERASE", "MASK"] | None = "None",
        pen_flip: bool | None = False,
        override_location: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Paint a stroke in the active color attribute layer

                :param execution_context:
                :param undo:
                :param stroke: Stroke, (optional)
                :param mode: Stroke Mode, Action taken when a paint stroke is made (optional)

        NORMAL
        Regular -- Apply brush normally.

        INVERT
        Invert -- Invert action of brush for duration of stroke.
                :param brush_toggle: Temporary Brush Toggle Type, Brush to use for duration of stroke (optional)

        None
        None -- Apply brush normally.

        SMOOTH
        Smooth -- Switch to smooth brush for duration of stroke.

        ERASE
        Erase -- Switch to erase brush for duration of stroke.

        MASK
        Mask -- Switch to mask brush for duration of stroke.
                :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used (optional)
                :param override_location: Override Location, Override the given "location" array by recalculating object space positions from the provided "mouse_event" positions (optional)
                :return: Result of the operator call.
        """

class vertex_paint_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle the vertex paint mode in 3D view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class visibility_filter(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        action: typing.Literal["GROW", "SHRINK"] | None = "GROW",
        iterations: int | None = 1,
        auto_iteration_count: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Edit the visibility of the current mesh

                :param execution_context:
                :param undo:
                :param action: Action, (optional)

        GROW
        Grow Visibility -- Grow the visibility by one face based on mesh topology.

        SHRINK
        Shrink Visibility -- Shrink the visibility by one face based on mesh topology.
                :param iterations: Iterations, Number of times that the filter is going to be applied (in [1, 100], optional)
                :param auto_iteration_count: Auto Iteration Count, Use an automatic number of iterations based on the number of vertices of the sculpt (optional)
                :return: Result of the operator call.
        """

class visibility_invert(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Invert the visibility of all vertices

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class weight_from_bones(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["AUTOMATIC", "ENVELOPES"] | None = "AUTOMATIC",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the weights of the groups matching the attached armatures selected bones, using the distance between the vertices and the bones

                :param execution_context:
                :param undo:
                :param type: Type, Method to use for assigning weights (optional)

        AUTOMATIC
        Automatic -- Automatic weights from bones.

        ENVELOPES
        From Envelopes -- Weights from envelopes with user defined radius.
                :return: Result of the operator call.
        """

class weight_gradient(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["LINEAR", "RADIAL"] | None = "LINEAR",
        xstart: int | None = 0,
        xend: int | None = 0,
        ystart: int | None = 0,
        yend: int | None = 0,
        flip: bool | None = False,
        cursor: int | None = 5,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Draw a line to apply a weight gradient to selected vertices

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :param xstart: X Start, (in [-inf, inf], optional)
        :param xend: X End, (in [-inf, inf], optional)
        :param ystart: Y Start, (in [-inf, inf], optional)
        :param yend: Y End, (in [-inf, inf], optional)
        :param flip: Flip, (optional)
        :param cursor: Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
        :return: Result of the operator call.
        """

class weight_paint(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
        | None = None,
        mode: typing.Literal["NORMAL", "INVERT"] | None = "NORMAL",
        brush_toggle: typing.Literal["None", "SMOOTH", "ERASE", "MASK"] | None = "None",
        pen_flip: bool | None = False,
        override_location: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Paint a stroke in the current vertex groups weights

                :param execution_context:
                :param undo:
                :param stroke: Stroke, (optional)
                :param mode: Stroke Mode, Action taken when a paint stroke is made (optional)

        NORMAL
        Regular -- Apply brush normally.

        INVERT
        Invert -- Invert action of brush for duration of stroke.
                :param brush_toggle: Temporary Brush Toggle Type, Brush to use for duration of stroke (optional)

        None
        None -- Apply brush normally.

        SMOOTH
        Smooth -- Switch to smooth brush for duration of stroke.

        ERASE
        Erase -- Switch to erase brush for duration of stroke.

        MASK
        Mask -- Switch to mask brush for duration of stroke.
                :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used (optional)
                :param override_location: Override Location, Override the given "location" array by recalculating object space positions from the provided "mouse_event" positions (optional)
                :return: Result of the operator call.
        """

class weight_paint_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Toggle weight paint mode in 3D view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class weight_sample(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Use the mouse to sample a weight in the 3D view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class weight_sample_group(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select one of the vertex groups available under current mouse position

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class weight_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Fill the active vertex group with the current paint weight

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
