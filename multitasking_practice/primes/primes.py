import math
from time import perf_counter
from typing import NamedTuple

PRIMES = [
    2,
    142702110479723,
    299593572317531, 
    3333333333333301, 
    3333333333333333, 
    3333335652092209, 
    4444444444444423, 
    4444444444444444, 
    4444444488888889, 
    5555553133149889, 
    5555555555555503, 
    5555555555555555, 
    6666666666666666, 
    6666666666666719, 
    6666667141414921, 
    7777777536340681, 
    7777777777777753,
    7777777777777777,
    9999999999999917, 
    9999999999999999,
]


def is_prime(n: int) -> bool:
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


class Result(NamedTuple):
    prime: bool
    elapsed: float


def check(n: int) -> Result:
    t0 = perf_counter()
    prime = is_prime(n)
    return Result(prime, perf_counter() - t0)