#!/usr/bin/env python3
"""
Module to measure the average runtime per coroutine call of wait_n.
"""

import time
import asyncio
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per call.

    Args:
        n (int): number of times to call wait_random
        max_delay (int): maximum delay for wait_random

    Returns:
        float: total_time / n (average time per coroutine)
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
