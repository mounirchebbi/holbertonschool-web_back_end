#!/usr/bin/env python3

"""
9-element_length.py

This module calculate the length of each element in a list.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes an iterable of sequences and returns a list of tuples.

    Parameters:
        lst (Iterable[Sequence])
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples each tuple contains
         a sequence and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
