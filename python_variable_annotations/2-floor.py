#!/usr/bin/env python3
"""
2-floor.py

This module provides a function to compute the floor of a given float number.
"""
import math


def floor(n: float) -> int:
    """
    This function takes a float and returns its floor as an integer.

    Parameters:
        n (float)

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
