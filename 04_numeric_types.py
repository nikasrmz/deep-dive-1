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


# print(format(0.1, '.25f'))
x = 0.1 + 0.1 + 0.1
y = 0.3
print(x == y)

# print(math.isclose(x, y))

