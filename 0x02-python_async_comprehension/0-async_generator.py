#!/usr/bin/env python3
""" 0-async_generator module """

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """ An async generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
