#!/usr/bin/env python3
"""
Module defining task_wait_n which spawns multiple asyncio.Tasks concurrently.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the given max_delay and collects
    the delays in the order they complete.

    Args:
        n (int): number of tasks to run
        max_delay (int): maximum delay passed to task_wait_random

    Returns:
        List[float]: list of delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
