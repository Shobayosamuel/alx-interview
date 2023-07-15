#!/usr/bin/python3
"""
    Function to get the minimum number of operations
"""


from math import sqrt


def minOperations(n):
    """Return the minimum number of operations"""
    factors = []
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            factors.append(i)
        n //= i
    if n > 1:
        factors.append(n)
    return sum(factors)
