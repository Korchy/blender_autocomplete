import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

def load_image(
    imagepath,
    dirname: str = "",
    place_holder: bool = False,
    recursive: bool = False,
    ncase_cmp: bool = True,
    convert_callback: typing.Any | None = None,
    verbose=False,
    relpath: None | str | None = None,
    check_existing: bool = False,
    force_reload: bool = False,
) -> None | bpy.types.Image:
    """Return an image from the file path with options to search multiple paths
    and return a placeholder if its not found.

        :param dirname: is the directory where the image may be located - any file at
    the end will be ignored.
        :param place_holder: if True a new place holder image will be created.
    this is useful so later you can relink the image to its original data.
        :param recursive: If True, directories will be recursively searched.
    Be careful with this if you have files in your root directory because
    it may take a long time.
        :param ncase_cmp: on non windows systems, find the correct case for the file.
        :param convert_callback: a function that takes an existing path and returns
    a new one. Use this when loading image formats blender may not support,
    the CONVERT_CALLBACK can take the path for a GIF (for example),
    convert it to a PNG and return the PNGs path.
    For formats blender can read, simply return the path that is given.
        :param relpath: If not None, make the file relative to this path.
        :param check_existing: If true,
    returns already loaded image data-block if possible
    (based on file path).
        :param force_reload: If true,
    force reloading of image (only useful when check_existing
    is also enabled).
        :return: an image or None
    """
