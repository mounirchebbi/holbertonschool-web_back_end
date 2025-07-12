#!/usr/bin/env python3

"""
8-make_multiplier.py

This module provides a function creator that generates multiplier functions.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies floats by a given multiplier.

    Parameters:
        multiplier (float)
    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product with the multiplier
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
