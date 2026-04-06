import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class MotionPathButtonsPanel:
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def draw_settings(self, _context, avs, mpath, bones=False) -> None:
        """

        :param _context:
        :param avs:
        :param mpath:
        :param bones:
        """

class MotionPathButtonsPanel_display:
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def draw_settings(self, _context, avs, mpath, bones=False) -> None:
        """

        :param _context:
        :param avs:
        :param mpath:
        :param bones:
        """
