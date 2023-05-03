import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        List[float]: _description_
    """

    results = await asyncio.gather(*tuple(map(lambda _: task_wait_random(
        max_delay), range(n))))
    return sorted(results)
