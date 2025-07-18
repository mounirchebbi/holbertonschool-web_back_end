#!/usr/bin/env python3
"""
Pagination helper module
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed)
        page_size (int): The number of items per page

    Returns:
        Tuple[int, int]: A tuple of (start_index, end_index)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "data.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches the dataset from CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline='') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset.

        Args:
            page (int): The current page number (1-indexed)
            page_size (int): The number of items per page

        Returns:
            List[List]: A list of dataset rows corresponding to the page
        """
        assert isinstance(page, int) and page > 0,
        "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0,
        "page_size must be a positive integer"

        start, end = index_range(page, page_size)
        data = self.dataset()

        return data[start:end] if start < len(data) else []
