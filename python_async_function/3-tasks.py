#!/usr/bin/env python3
"""
Module that provides a regular function to create an asyncio.Task
for the wait_random coroutine.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay passed to wait_random

    Returns:
        asyncio.Task: A Task object wrapping the wait_random coroutine
    """
    return asyncio.create_task(wait_random(max_delay))
