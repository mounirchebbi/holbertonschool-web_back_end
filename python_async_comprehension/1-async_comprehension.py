#!/usr/bin/env python3
"""
Module: 1-async_comprehension

Defines a coroutine that asynchronously collects 10 random float numbers
from an async generator using an asynchronous list comprehension.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Uses an async comprehension to collect 10 random float numbers
    yielded by the async_generator coroutine.

    Returns:
        List[float]: A list of 10 random float numbers between 0 and 10.
    """
    return [i async for i in async_generator()]
