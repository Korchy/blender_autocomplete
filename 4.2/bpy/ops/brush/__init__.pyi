import typing
import collections.abc
import typing_extensions
import bpy.types

def add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add brush by mode type

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def add_gpencil(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add brush for Grease Pencil

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def curve_preset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    shape: typing.Literal["SHARP", "SMOOTH", "MAX", "LINE", "ROUND", "ROOT"]
    | None = "SMOOTH",
):
    """Set brush shape

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param shape: Mode
    :type shape: typing.Literal['SHARP','SMOOTH','MAX','LINE','ROUND','ROOT'] | None
    """

def reset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Return brush to defaults based on current tool

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def scale_size(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    scalar: float | None = 1.0,
):
    """Change brush size by a scalar

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param scalar: Scalar, Factor to scale brush size by
    :type scalar: float | None
    """

def sculpt_curves_falloff_preset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    shape: typing.Literal["SHARP", "SMOOTH", "MAX", "LINE", "ROUND", "ROOT"]
    | None = "SMOOTH",
):
    """Set Curve Falloff Preset

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param shape: Mode
    :type shape: typing.Literal['SHARP','SMOOTH','MAX','LINE','ROUND','ROOT'] | None
    """

def stencil_control(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Literal["TRANSLATION", "SCALE", "ROTATION"] | None = "TRANSLATION",
    texmode: typing.Literal["PRIMARY", "SECONDARY"] | None = "PRIMARY",
):
    """Control the stencil brush

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Tool
    :type mode: typing.Literal['TRANSLATION','SCALE','ROTATION'] | None
    :param texmode: Tool
    :type texmode: typing.Literal['PRIMARY','SECONDARY'] | None
    """

def stencil_fit_image_aspect(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_repeat: bool | None = True,
    use_scale: bool | None = True,
    mask: bool | None = False,
):
    """When using an image texture, adjust the stencil size to fit the image aspect ratio

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_repeat: Use Repeat, Use repeat mapping values
    :type use_repeat: bool | None
    :param use_scale: Use Scale, Use texture scale values
    :type use_scale: bool | None
    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil
    :type mask: bool | None
    """

def stencil_reset_transform(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mask: bool | None = False,
):
    """Reset the stencil transformation to the default

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil
    :type mask: bool | None
    """
