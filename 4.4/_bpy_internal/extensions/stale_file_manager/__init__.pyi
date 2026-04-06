import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class StaleFiles:
    def filepath_add(self, path_abs, *, rename) -> None:
        """

        :param path_abs:
        :param rename:
        """

    def is_empty(self) -> None: ...
    def is_modified(self) -> None: ...
    def state_load(self, *, check_exists) -> None:
        """

        :param check_exists:
        """

    def state_load_add_and_store(self, *, paths) -> None:
        """

        :param paths:
        """

    def state_load_remove_and_store(self, *, paths) -> None:
        """

        :param paths:
        """

    def state_remove_all(self) -> None: ...
    def state_store(self, *, check_exists) -> None:
        """

        :param check_exists:
        """
