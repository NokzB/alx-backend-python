#!/usr/bin/env python3
"""Solution for task 0"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generates a random sequence of 10 numbers."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
