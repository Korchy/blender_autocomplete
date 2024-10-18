"""
This module contains utility functions to handle custom previews.

It behaves as a high-level 'cached' previews manager.

This allows scripts to generate their own previews, and use them as icons in UI widgets
('icon_value' for UILayout functions).


--------------------

```__/__/__/scripts/templates_py/ui_previews_custom_icon.py```

"""

import typing
import collections.abc
import typing_extensions
import bpy.types

class ImagePreviewCollection:
    """Dictionary-like class of previews.This is a subclass of Python's built-in dict type,
    used to store multiple image previews.
    """

    def clear(self):
        """Clear all previews."""

    def close(self):
        """Close the collection and clear all previews."""

    def load(
        self,
        name: str | None,
        filepath: bytes | str | None,
        filetype: str | None,
        force_reload: bool | None = False,
    ) -> bpy.types.ImagePreview:
        """Generate a new preview from given file path.

        :param name: The name (unique id) identifying the preview.
        :type name: str | None
        :param filepath: The file path to generate the preview from.
        :type filepath: bytes | str | None
        :param filetype: The type of file, needed to generate the preview in ['IMAGE', 'MOVIE', 'BLEND', 'FONT'].
        :type filetype: str | None
        :param force_reload: If True, force running thumbnail manager even if preview already exists in cache.
        :type force_reload: bool | None
        :return: The Preview matching given name, or a new empty one.
        :rtype: bpy.types.ImagePreview
        """

    def new(self, name: str | None) -> bpy.types.ImagePreview:
        """Generate a new empty preview.

        :param name: The name (unique id) identifying the preview.
        :type name: str | None
        :return: The Preview matching given name, or a new empty one.
        :rtype: bpy.types.ImagePreview
        """

def new() -> ImagePreviewCollection:
    """

    :return: a new preview collection.
    :rtype: ImagePreviewCollection
    """

def remove(pcoll: ImagePreviewCollection | None):
    """Remove the specified previews collection.

    :param pcoll: Preview collection to close.
    :type pcoll: ImagePreviewCollection | None
    """
