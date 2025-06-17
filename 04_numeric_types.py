from typing import List
import math

def different_base_numbers():
    a = 0b1010
    b = 0o12
    c = int('11', 9)
    print(a == b == c)


# different_base_numbers()


def from_base_10(n: int, base: int) -> List[int]:
    if n < 0:
        print("enter non-negative number")
    if base < 2:
        print("base must be >= 2")
    if n <= 1:
        return [n]
    digits = []
    while n > 0:
        # m = n % base
        # n = n // base
        n, m = divmod(n, base)
        digits.insert(0, m)
    return digits


# print(from_base_10(10, 3))
    

def encode(digits: List[int], digit_map: str) -> str:
    if max(digits) > len(digit_map):
        raise ValueError('base not supported')
    # encoding = ''
    # for digit in digits:
    #     encoding += digit_map[digit]
    # return encoding
    return ''.join([digit_map[digit] for digit in digits])

# print(encode([15, 15], '0123456789ABCDEF'))


def rebase_base_10(number: int, base: int) -> int:
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError("base not supported")
    sign = 1 if number >= 0 else -1

    number *= sign

    digits = from_base_10(number, base)
    result = encode(digits, digit_map)

    if sign == -1:
        return "-" + result

    return result

n = rebase_base_10(-123512, 16)
# print(n)
# print(int(n, base=16))

def weird_floats():
    print(format(0.1, '.25f'))
    x = 0.1 + 0.1 + 0.1
    y = 0.3
    print(x == y)

    print(math.isclose(x, y))

def trunc_floor_ceil():
    print(math.trunc(10.5) == math.floor(10.5))
    print(math.trunc(-10.5) == math.floor(-10.5))

    print(math.trunc(10.5) == math.ceil(10.5))
    print(math.trunc(-10.5) == math.ceil(-10.5))

def round_test():
    # round() - Banker's rounding: rounding to closest multiple, prioritizing least significant digit that is even. ex:
    print(round(15, -1))
    print(round(25, -1))
    # Both 20s

def standard_round(number: float):
    return int(number + math.copysign(0.5, number))

# print(standard_round(-10.5))
# print(standard_round(10.5))


# ---------- decimals ----------

def global_vs_local_context():
    import decimal
    g_ctx = decimal.getcontext()
    print(g_ctx)

    g_ctx.rounding = decimal.ROUND_HALF_UP

    with decimal.localcontext() as ctx:
        ctx.rounding = decimal.ROUND_HALF_UP


# global_vs_local_context()

def constructors():
    import decimal
    from decimal import Decimal
    # -3.1415
    pi = Decimal((1, (3, 1, 4, 1, 5), -4))
    print(pi)

    with decimal.localcontext() as ctx:
        ctx.prec = 2
        a = Decimal('0.12345')
        b = Decimal('0.12345')
        print(a, b, a + b)

    print(type(Decimal(10) + 1)) 

# constructors()

def div_and_mod():
    from decimal import Decimal
    a = 10
    b = -10
    d_a = Decimal(a)
    d_b = Decimal(b)
    print(a // 3)
    print(b // 3)
    print(d_a // 3)
    print(d_b // 3)
    print('----')
    print(a % 3)
    print(b % 3)
    print(d_a % 3)
    print(d_b % 3)

# div_and_mod()

def performance():
    import sys
    from decimal import Decimal
    a = 2.5
    b = Decimal('2.5')
    print(sys.getsizeof(a))
    print(sys.getsizeof(b))

    import time

    def run_float(n=1):
        for i in range(n):
            a = 2.5

    def run_decimal(n=1):
        for i in range(n):
            a = Decimal('2.5')

    n = 10000000

    start = time.perf_counter()
    run_float(n)
    after_float = time.perf_counter()
    run_decimal(n)
    end = time.perf_counter()

    print(after_float - start)
    print(end - after_float)


# performance()

def useful_checkers():
    print(issubclass(bool, int))
    print(isinstance(True, bool))
    print(isinstance(True, int))

# useful_checkers()

def bool_comparisons():
    a = True
    b = 1 
    print(a == b)  # compares the values that the objects represent
    print(a is b)  # compares whether both variables point to the exact same object (memory address)

# bool_comparisons()

"""
    In python, EVERY variable is a pointer to some memory, even simple integers.
"""

"""
    Code:
        if (lst is not None) and (len(lst) > 0):
    is exactly the same as:
        if lst: 
"""

"""
   X or Y   --  returns X if X is true, else Y
   X and Y  --  returns X if X is false, else Y
"""

def default_value_variables():
    a = ""
    b = a or "default value"
    print(b)
    a = None
    b = a or "default value"
    print(b)
    a = "value"
    b = a or "default value"
    print(b)

# default_value_variables()

def division(x, y):
    return y and x/y

# print(division(1, 2))
# print(division(1, 0))

# return first element of given string or ''
def first_elem(s):
    return (s or '') and s[0]

# print(first_elem('abc'))


def equal_floats(a: float, b: float, rel_tol: float = 1e-9, abs_tol: float = 0):
    return (max(a, b) * rel_tol <= abs(a - b)) or abs(a - b) < abs_tol

def get_email(user):
    return user and user.get('contact') and user['contact'].get('email') or None

print(get_email())
