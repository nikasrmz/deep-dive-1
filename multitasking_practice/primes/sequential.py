"""
sequential.py: baseline for comparing sequential, multiprocessing,
and threading code for CPU-intensive work.
"""
from time import perf_counter
from typing import NamedTuple
from primes import check, is_prime, PRIMES


def main() -> None:
    print(f'Checking {len(PRIMES)} numbers sequentially:')
    t0 = perf_counter()
    
    for n in PRIMES:
        prime, elapsed = check(n)
        label = 'P' if prime else ' '
        print(f'{n:16} {label} {elapsed:9.6f}s')
    
    elapsed = perf_counter() - t0
    print(f'Total time: {elapsed:.2f}s')


if __name__ == '__main__':
 main()