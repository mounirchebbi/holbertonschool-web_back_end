#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay time waited, as a float.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
