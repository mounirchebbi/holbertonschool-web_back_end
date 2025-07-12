#!/usr/bin/env python3

"""
6-sum_mixed_list.py

This module calculate the sum of a mixed list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function takes a list of integers and floats and returns their sum.

    Parameters:
        mxd_lst (List[Union[int, float]])
    Returns:
        float: The sum of the numbers in mxd_lst.
    """
    return float(sum(mxd_lst))
