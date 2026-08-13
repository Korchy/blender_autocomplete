"""
This module contains utility functions to handle custom previews.

It behaves as a high-level 'cached' previews manager.

This allows scripts to generate their own previews, and use them as icons in UI widgets
('icon_value' for UILayout functions).


--------------------

```__/__/__/scripts/templates_py/UI/previews_custom_icon.py```

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

class ImagePreviewCollection(dict[str, bpy.types.ImagePreview]):
    """Dictionary-like class of previews.This is a subclass of Pythons built-in dict type,
    used to store multiple image previews.
    """

    def clear(self) -> None:
        """Clear all previews."""

    def close(self) -> None:
        """Close the collection and clear all previews."""

    def load(
        self,
        name: str | None,
        filepath: bytes | str | None,
        file_type: typing.Literal["IMAGE", "MOVIE", "BLEND", "FONT", "OBJECT_IO"]
        | None,
        force_reload: bool | None = False,
    ) -> bpy.types.ImagePreview:
        """Generate a new preview from given file path.

        :param name: The name (unique id) identifying the preview.
        :param filepath: The file path to generate the preview from.
        :param file_type: The type of file, needed to generate the preview.
        :param force_reload: If True, force running thumbnail manager even if preview already exists in cache.
        :return: The Preview matching given name, or a new empty one.
        """

    def new(self, name: str | None) -> bpy.types.ImagePreview:
        """Generate a new empty preview.

        :param name: The name (unique id) identifying the preview.
        :return: The Preview matching given name, or a new empty one.
        """

def new() -> ImagePreviewCollection:
    """

    :return: a new preview collection.
    """

def remove(pcoll: ImagePreviewCollection | None) -> None:
    """Remove the specified previews collection.

    :param pcoll: Preview collection to close.
    """
