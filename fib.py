"""
fib.py — Fibonacci helpers
"""
from typing import List

def fib_sequence(n: int) -> List[int]:
    """
    Return a list with the first n Fibonacci numbers starting from 1, 1, 2, ...
    """
    if n <= 0:
        return []
    if n == 1:
        return [1]
    seq = [1, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq
