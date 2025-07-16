import math
import asyncio
import itertools
import time
from pydecora import timeit
# ------ Spinner with coroutines ------

async def aspin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


async def slow():
    result = await is_prime(5_000_111_000_222_021)
    return result


async def supervisor_async():
    spinner = asyncio.create_task(aspin("Loading..."))
    print(f"spinner object: {spinner}")
    result = await slow()
    spinner.cancel()
    return result


def spinner_with_coroutines():
    result = asyncio.run(supervisor_async())
    print(f"Answer: {result}")


@timeit(log_level=30)
async def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True



if __name__ == "__main__":
    spinner_with_coroutines()