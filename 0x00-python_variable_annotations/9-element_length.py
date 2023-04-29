#!/usr/bin/env python3
'''Annotate the below function’s parameters
and return values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]'''

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Return a list of tuples containing the element and its length."""
    return [(i, len(i)) for i in lst]
