import typing
import collections.abc
import typing_extensions

class StaleFiles:
    def filepath_add(self, path_abs, *, rename):
        """

        :param path_abs:
        :param rename:
        """

    def is_empty(self): ...
    def is_modified(self): ...
    def state_load(self, *, check_exists):
        """

        :param check_exists:
        """

    def state_load_add_and_store(self, *, paths):
        """

        :param paths:
        """

    def state_load_remove_and_store(self, *, paths):
        """

        :param paths:
        """

    def state_remove_all(self): ...
    def state_store(self, *, check_exists):
        """

        :param check_exists:
        """
