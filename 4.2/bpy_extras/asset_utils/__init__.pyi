"""
Helpers for asset management tasks.

"""

import typing
import collections.abc
import typing_extensions

class AssetBrowserPanel:
    bl_space_type: typing.Any

    @classmethod
    def asset_browser_panel_poll(cls, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class AssetMetaDataPanel:
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class SpaceAssetInfo: ...
