#!/usr/bin/env python3

"""
7-to_kv.py

This module create a tuple from a string and a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string and an integer or float, and returns a tuple.

    Parameters:
        k (str)
        v (Union[int, float])
    Returns:
        Tuple[str, float]: A tuple.
    """
    return (k, float(v ** 2))
