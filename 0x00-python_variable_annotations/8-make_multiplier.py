#!/usr/bin/python3
""" returns a function that multiplies a float by multiplier. """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier."""
    def callable(number: float) -> float:
        """ Number x multiplier """
        return number * multiplier
    return callable
