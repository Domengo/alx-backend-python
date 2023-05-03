#!/usr/bin/env python3
"""_summary_

    Returns:
        _type_: _description_
    """
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''''calculates the runtime of wait_n'''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
