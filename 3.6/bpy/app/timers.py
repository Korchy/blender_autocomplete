import sys
import typing

GenericType = typing.TypeVar("GenericType")


def is_registered(function: typing.Optional[int]) -> bool:
    ''' Check if this function is registered as a timer.

    :param function: Function to check.
    :type function: typing.Optional[int]
    :rtype: bool
    :return: True when this function is registered, otherwise False.
    '''

    pass


def register(function: typing.Optional[typing.Callable],
             first_interval: typing.Optional[float] = 0,
             persistent: typing.Optional[bool] = False):
    ''' Add a new function that will be called after the specified amount of seconds. The function gets no arguments and is expected to return either None or a float. If ``None`` is returned, the timer will be unregistered. A returned number specifies the delay until the function is called again. ``functools.partial`` can be used to assign some parameters.

    :param function: The function that should called.
    :type function: typing.Optional[typing.Callable]
    :param first_interval: Seconds until the callback should be called the first time.
    :type first_interval: typing.Optional[float]
    :param persistent: Don't remove timer when a new file is loaded.
    :type persistent: typing.Optional[bool]
    '''

    pass


def unregister(function: typing.Optional[typing.Any]):
    ''' Unregister timer.

    :param function: Function to unregister.
    :type function: typing.Optional[typing.Any]
    '''

    pass
