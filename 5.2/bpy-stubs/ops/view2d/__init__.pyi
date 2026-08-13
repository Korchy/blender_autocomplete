import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class edge_pan(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        inside_padding: float | None = 1.0,
        outside_padding: float | None = 0.0,
        speed_ramp: float | None = 1.0,
        max_speed: float | None = 500.0,
        delay: float | None = 1.0,
        zoom_influence: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pan the view when the mouse is held at an edge

        :param execution_context:
        :param undo:
        :param inside_padding: Inside Padding, Inside distance in UI units from the edge of the region within which to start panning (in [0, 100], optional)
        :param outside_padding: Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning (in [0, 100], optional)
        :param speed_ramp: Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge (in [0, 100], optional)
        :param max_speed: Max Speed, Maximum speed in UI units per second (in [0, 10000], optional)
        :param delay: Delay, Delay in seconds before maximum speed is reached (in [0, 10], optional)
        :param zoom_influence: Zoom Influence, Influence of the zoom factor on scroll speed (in [0, 1], optional)
        :return: Result of the operator call.
        """

class ndof(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Use a 3D mouse device to pan/zoom the view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class pan(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        deltax: int | None = 0,
        deltay: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Pan the view

        :param execution_context:
        :param undo:
        :param deltax: Delta X, (in [-inf, inf], optional)
        :param deltay: Delta Y, (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class reset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset the view

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class scroll_down(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        deltax: int | None = 0,
        deltay: int | None = 0,
        page: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Scroll the view down

        :param execution_context:
        :param undo:
        :param deltax: Delta X, (in [-inf, inf], optional)
        :param deltay: Delta Y, (in [-inf, inf], optional)
        :param page: Page, Scroll down one page (optional)
        :return: Result of the operator call.
        """

class scroll_left(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        deltax: int | None = 0,
        deltay: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Scroll the view left

        :param execution_context:
        :param undo:
        :param deltax: Delta X, (in [-inf, inf], optional)
        :param deltay: Delta Y, (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class scroll_right(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        deltax: int | None = 0,
        deltay: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Scroll the view right

        :param execution_context:
        :param undo:
        :param deltax: Delta X, (in [-inf, inf], optional)
        :param deltay: Delta Y, (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class scroll_up(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        deltax: int | None = 0,
        deltay: int | None = 0,
        page: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Scroll the view up

        :param execution_context:
        :param undo:
        :param deltax: Delta X, (in [-inf, inf], optional)
        :param deltay: Delta Y, (in [-inf, inf], optional)
        :param page: Page, Scroll up one page (optional)
        :return: Result of the operator call.
        """

class scroller_activate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Scroll view by mouse click and drag

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class smoothview(bpy.ops._BPyOpsSubModOp):
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Undocumented, consider contributing.

        :param execution_context:
        :param undo:
        :param xmin: X Min, (in [-inf, inf], optional)
        :param xmax: X Max, (in [-inf, inf], optional)
        :param ymin: Y Min, (in [-inf, inf], optional)
        :param ymax: Y Max, (in [-inf, inf], optional)
        :param wait_for_input: Wait for Input, (optional)
        :return: Result of the operator call.
        """

class zoom(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        deltax: float | None = 0.0,
        deltay: float | None = 0.0,
        use_cursor_init: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Zoom in/out the view

        :param execution_context:
        :param undo:
        :param deltax: Delta X, (in [-inf, inf], optional)
        :param deltay: Delta Y, (in [-inf, inf], optional)
        :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used (optional)
        :return: Result of the operator call.
        """

class zoom_border(bpy.ops._BPyOpsSubModOp):
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
        zoom_out: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Zoom in the view to the nearest item contained in the border

        :param execution_context:
        :param undo:
        :param xmin: X Min, (in [-inf, inf], optional)
        :param xmax: X Max, (in [-inf, inf], optional)
        :param ymin: Y Min, (in [-inf, inf], optional)
        :param ymax: Y Max, (in [-inf, inf], optional)
        :param wait_for_input: Wait for Input, (optional)
        :param zoom_out: Zoom Out, (optional)
        :return: Result of the operator call.
        """

class zoom_in(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        zoomfacx: float | None = 0.0375,
        zoomfacy: float | None = 0.0375,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Zoom in the view

        :param execution_context:
        :param undo:
        :param zoomfacx: Zoom Factor X, (in [-inf, inf], optional)
        :param zoomfacy: Zoom Factor Y, (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class zoom_out(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        zoomfacx: float | None = -0.0375,
        zoomfacy: float | None = -0.0375,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Zoom out the view

        :param execution_context:
        :param undo:
        :param zoomfacx: Zoom Factor X, (in [-inf, inf], optional)
        :param zoomfacy: Zoom Factor Y, (in [-inf, inf], optional)
        :return: Result of the operator call.
        """
