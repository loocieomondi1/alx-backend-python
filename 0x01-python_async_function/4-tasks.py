#!/usr/bin/env python3
""" code is nearly identical to wait_n except task_wait_random is being called
"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random
from typing import List
import bisect


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ async function"""
    ret = []
    for i in range(n):
        n = await task_wait_random(max_delay)
        bisect.insort(ret, n)
    return ret
