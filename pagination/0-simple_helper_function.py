#!/usr/bin/env python3
"""
Defines a simple helper function for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start and end index
    for the given pagination parameters.

    Args:
        page (int): current page number (1-indexed)
        page_size (int): number of items per page

    Returns:
        Tuple[int, int]: (start index, end index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
