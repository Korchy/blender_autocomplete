import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class ValidatingParser:
    """Wrapper around cattrs, caching the cattrs converter."""

    def dumps(self, model_instance) -> None:
        """Convert the model instance to JSON, returning it as string.

        :param model_instance:
        """

    def parse_and_validate(self, model_class, json_payload) -> None:
        """Parse & validate the JSON data, returning an instance of the given model class.

        :param model_class:
        :param json_payload:
        """
