#!/usr/bin/env python3
""" 0-async_generator module """

from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator:
    """ An async generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
