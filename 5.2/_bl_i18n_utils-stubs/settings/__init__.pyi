import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class I18nSettings:
    """Class allowing persistence of our settings!
    Saved in JSON format, so settings should be JSONable objects!
    """

    BLENDER_I18N_PO_DIR: typing.Any
    BLENDER_I18N_ROOT: typing.Any
    FILE_NAME_POT: typing.Any
    POTFILES_SOURCE_DIR: typing.Any
    PRESETS_DIR: typing.Any
    PY_SYS_PATHS: typing.Any
    TEMPLATES_DIR: typing.Any
    WORK_DIR: typing.Any

    def from_dict(self, mapping) -> None:
        """

        :param mapping:
        """

    def from_json(self, string) -> None:
        """

        :param string:
        """

    def load(self, fname, reset=False) -> None:
        """

        :param fname:
        :param reset:
        """

    def save(self, fname) -> None:
        """

        :param fname:
        """

    def to_dict(self) -> None: ...
    def to_json(self) -> None: ...

class PyGettextKeyword: ...
