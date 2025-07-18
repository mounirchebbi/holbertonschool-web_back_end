#!/usr/bin/env python3
"""
Asynchronous generator that yields random numbers between 0 and 10.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields a random float between 0 and 10,
    10 times, with a 1-second delay between yields.

    Returns:
        AsyncGenerator[float, None]: yields 10 random float values
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
