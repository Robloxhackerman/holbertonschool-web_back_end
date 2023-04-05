#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """

    :return:
    """
    tasks = []
    start = time.time()
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
