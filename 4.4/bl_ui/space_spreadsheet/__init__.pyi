import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

class SPREADSHEET_HT_header(bpy.types.Header):
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw(self, context) -> None:
        """

        :param context:
        """

    def draw_collapsed_viewer_path(self, context, layout, viewer_path) -> None:
        """

        :param context:
        :param layout:
        :param viewer_path:
        """

    def draw_full_viewer_path(self, context, layout, viewer_path) -> None:
        """

        :param context:
        :param layout:
        :param viewer_path:
        """

    def draw_spreadsheet_context(self, layout, ctx) -> None:
        """

        :param layout:
        :param ctx:
        """

    def draw_spreadsheet_viewer_path_icon(
        self, layout, space, icon="RIGHTARROW_THIN"
    ) -> None:
        """

        :param layout:
        :param space:
        :param icon:
        """

    def draw_without_viewer_path(self, layout) -> None:
        """

        :param layout:
        """

    def selection_filter_available(self, space) -> None:
        """

        :param space:
        """
