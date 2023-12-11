#!/usr/bin/env python3
""" 0-basic_async_syntax module """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ waits for random delay time and returns """
    max_delay = max_delay if max_delay <= 10 else 10
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
