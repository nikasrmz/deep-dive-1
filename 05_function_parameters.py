import time
from typing import Dict

def extended_unpacking():
    s = {1, -1, 0, 'd'}
    print(s)

    l = [1, 2, 3, 'python']

    a = l[0]
    b = l[1:-1]
    c = l[-1][0]
    d = l[-1][1:]
    a, b, c, d = l[0], l[1:-1], l[-1][0], list(l[-1][1:])
    print(a, b, c, d)
    a, *b, (c, *d) = l
    print(a, b, c, d)


def star_args():
    def func1(a, b, *args):
        print(a)
        print(b)
        print(args)

    # func1(10, 20)
    # func1(10, 20, 30, 40, 50)

    def avg(*args):
        if not args:
            return 0
        count = len(args)
        total = sum(args)
        return total/count
    
    def avg2(*args):
        count = len(args)
        total = sum(args)
        return count and total/count
    
    def func2(a, b, c):
        print(a, b, c)

    def func3(*args, d):
        print(args, d)

    def func4(*, d):
        print(d)

    def func5(a, b, *, d):
        print(a, b, d)

    def func6(a, b=2, *args, d):
        print(a, b, args, d)


    # func3(1, 2, 3, 4, d=5)
    # func4(d=1)
    # func5(1, 2, d=3)
    func6(1, 2, 3, 4, 5, 6, d=7)

    def checkout_toll(vehicle, *, is_peak_hour=False):
        if vehicle == "car":
            toll = 5
        elif vehicle == 'truck':
            toll = 7
        else:
            toll = 3
        if is_peak_hour:
            toll += 2
        print(toll)

    # checkout_toll("car") 
    # checkout_toll("car", is_peak_hour=True) 
    # checkout_toll("bike", is_peak_hour=True) 
    timer(checkout_toll, "car", is_peak_hour=True)


def star_star_kwargs():
    def format_dict(**kwargs):
        print(*sorted([f"{key}={value}" for key, value in kwargs.items()]), sep='; ')

    # format_dict(name="Alice", age=30, city="Tbilisi")

    params = {"a": 5, "b": "3", "error_value": 0}

    def safe_add(a, b, *, error_value=None):
        try:
            return a + b
        except TypeError:
            return error_value
        
    
    print(safe_add(**params))


def timer(fn, *args, **kwargs):
    start = time.perf_counter()
    res = fn(*args, **kwargs)
    print(time.perf_counter() - start, "elapsed")
    return res



star_args()


class A:
    val: int = 0

def func(x, a=A()):
    a.val += x
    print(a.val)

func(1)
func(2, A())
func(3)

def factorial(n: int, cache: Dict[int, int]={}):
    if n <= 1: 
        return 1
    if n in cache:
        return cache[n]
    result = n * factorial(n - 1)
    cache[n] = result
    return result

