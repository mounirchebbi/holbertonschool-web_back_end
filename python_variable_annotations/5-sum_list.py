#!/usr/bin/env python3

"""
5-sum_list.py

This module calculate the sum of a list of float numbers.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of floats and returns their sum.

    Parameters:
        input_list (List[float])
    Returns:
        float: The sum of the float numbers in input_list.
    """
    return sum(input_list)
