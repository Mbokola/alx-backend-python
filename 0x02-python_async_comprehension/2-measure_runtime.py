#!/usr/bin/env python3

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime"""
    start = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter() - start

    return end
