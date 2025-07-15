import asyncio
import itertools

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
    await asyncio.sleep(3)
    return 42


async def supervisor_async():
    spinner = asyncio.create_task(aspin("Loading..."))
    print(f"spinner object: {spinner}")
    result = await slow()
    spinner.cancel()
    return result


def spinner_with_coroutines():
    result = asyncio.run(supervisor_async())
    print(f"Answer: {result}")




if __name__ == "__main__":
    spinner_with_coroutines()