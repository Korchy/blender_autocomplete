import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class MotionPathButtonsPanel:
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def draw_settings(self, _context, avs, mpath, bones=False):
        """

        :param _context:
        :param avs:
        :param mpath:
        :param bones:
        """
        ...

class MotionPathButtonsPanel_display:
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def draw_settings(self, _context, avs, mpath, bones=False):
        """

        :param _context:
        :param avs:
        :param mpath:
        :param bones:
        """
        ...
