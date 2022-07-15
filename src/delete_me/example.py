"""
Example of a Python Module calculating N-th Fibonacci number.
"""

__all__ = ["fib"]

def fib(n: int) -> int:
    """Calculate N-th Fibonacci number.

    A tiling with squares whose side lengths are successive Fibonacci numbers: 1, 1, 2, 3, 5, 8, 13 and 21.
    In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence,
    such that each number is the sum of the two preceding ones, starting from 0 and 1.
    That is,
        F0 = 0
        F1 = 1
    and
        Fn = F[n - 1] + F[n - 2]
    for n > 1.

    Args:
        n (int): number greater than 1

    Returns:
        int: N-th Fibonacci number
    """
    if not float(n).is_integer():
        raise TypeError(f"Invalid type of n: {type(n)}, expected int")
    if n < 0:
        raise ValueError("Invalid argument fib({n}), expected N > 1")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
