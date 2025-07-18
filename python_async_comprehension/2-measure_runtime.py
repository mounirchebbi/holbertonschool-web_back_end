#!/usr/bin/env python3
"""
Module: 2-measure_runtime

This module defines a coroutine to measure how long it takes to run
async_comprehension four times in parallel.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures total runtime to execute async_comprehension 4 times in parallel.

    Returns:
        float: Total elapsed time in seconds.
    """
    start_time = time.perf_counter()

    # Run 4 async_comprehension calls concurrently
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    return end_time - start_time
