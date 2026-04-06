import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import gpu.types

def batch_for_shader(
    shader: gpu.types.GPUShader,
    type: str,
    content: dict[
        str,
        gpu.types.Buffer
        | collections.abc.Sequence[float]
        | collections.abc.Sequence[int]
        | collections.abc.Sequence[collections.abc.Sequence[float]]
        | collections.abc.Sequence[collections.abc.Sequence[int]],
    ],
    *,
    indices=None,
) -> gpu.types.GPUBatch:
    """Return a batch already configured and compatible with the shader.

        :param shader: shader for which a compatible format will be computed.
        :param type: "POINTS, LINES, TRIS or LINES_ADJ".
        :param content: Maps the name of the shader attribute with the data to fill the vertex buffer.
    For the dictionary values see documentation for `gpu.types.GPUVertBuf.attr_fill` data argument.
        :return: compatible batch
    """
