#!/usr/bin/env python3
""" coroutine will collect 10 random numbers using an async comprehension over async_generator, then return the 10
random numbers. """
import asyncio
from typing import List, Any

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[Any]:
    return [i async for i in async_generator()]
