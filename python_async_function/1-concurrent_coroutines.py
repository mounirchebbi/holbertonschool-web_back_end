#!/usr/bin/env python3
"""
Module of async routine to run multiple wait_random coroutines concurrently.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): maximum delay for wait_random

    Returns:
        List[float]: list of delays in ascending order
    """
    delays: List[float] = []
    for coroutine in asyncio.as_completed([wait_random(max_delay)
                                           for _ in range(n)]):
        delay = await coroutine
        delays.append(delay)
    return delays
