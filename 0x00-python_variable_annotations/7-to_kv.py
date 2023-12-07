#!/usr/bin/python3
""" returns a tuple. """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v * v))
