import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class BHead4:
    """BHead4(code: bytes, len: int, old: int, SDNAnr: int, nr: int)"""

class BlendFileHeader:
    """BlendFileHeader represents the first 12-17 bytes of a blend file.It contains information about the hardware architecture, which is relevant
    to the structure of the rest of the file.
    """

    def create_block_header_struct(self) -> None: ...

class BlendHeaderError:
    """Common base class for all non-exit exceptions."""

    args: typing.Any

class BlockHeader:
    """A .blend file consists of a sequence of blocks whereby each block has a header.
    This class can parse a header block in a specific .blend file.Note the binary representation of this header is different for different files.
    This class provides a unified interface for these underlying representations.
    """

    addr_old: typing.Any
    code: typing.Any
    count: typing.Any
    sdna_index: typing.Any
    size: typing.Any

class BlockHeaderStruct:
    """BlockHeaderStruct(struct: _struct.Struct, type: Type[Union[_blendfile_header.BHead4, _blendfile_header.SmallBHead8, _blendfile_header.LargeBHead8]])"""

    size: typing.Any

    def parse(self, data) -> None:
        """

        :param data:
        """

class LargeBHead8:
    """LargeBHead8(code: bytes, SDNAnr: int, old: int, len: int, nr: int)"""

class SmallBHead8:
    """SmallBHead8(code: bytes, len: int, old: int, SDNAnr: int, nr: int)"""
