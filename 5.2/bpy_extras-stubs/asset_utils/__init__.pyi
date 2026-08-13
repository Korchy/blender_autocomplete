"""
Helpers for asset management tasks.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

class AssetBrowserPanel:
    """Mixin class for panels that should only show in the asset browser."""

    @classmethod
    def asset_browser_panel_poll(cls, context: bpy.types.Context) -> bool:
        """Check if the panel should be shown in the asset browser.

        :param context: The context.
        :return: True when the panel should be visible.
        """

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        """Poll for asset browser visibility.

        :param context: The context.
        :return: True when the panel should be visible.
        """

class AssetMetaDataPanel:
    """Mixin class for panels that display asset metadata in the asset browser."""

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        """Poll for asset browser with active asset metadata.

        :param context: The context.
        :return: True when the asset browser has active asset data.
        """

class SpaceAssetInfo:
    """Utility class for checking if a space is an asset browser."""

    @classmethod
    def is_asset_browser(cls, space_data: bpy.types.Space) -> bool:
        """Check if the given space is an asset browser.

        :param space_data: The space to check.
        :return: True when the space is an asset browser.
        """

    @classmethod
    def is_asset_browser_poll(cls, context: bpy.types.Context) -> bool:
        """Poll whether the active space is an asset browser.

        :param context: The context.
        :return: True when the active space is an asset browser.
        """
