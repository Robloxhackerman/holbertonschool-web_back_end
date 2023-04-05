#!/usr/bin/env python3
"""
Write a function (do not create an async function, use the regular
function syntax to do this) task_wait_random that takes an integer
max_delay and returns a asyncio.Task.
"""

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    """

    :param max_delay:
    :return:
    """
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
