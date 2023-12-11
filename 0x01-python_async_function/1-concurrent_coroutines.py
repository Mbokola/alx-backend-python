#!/usr/bin/env python3
""" 1-concurrent_coroutines module """

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """ Multiple coroutines """
    delays: List = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
