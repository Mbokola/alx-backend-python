#!/usr/bin/env python3
""" 9-element_length module """

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ 9-element_length module """
    return [(i, len(i)) for i in lst]
