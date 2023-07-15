#!/usr/bin/python3
"""
    Function to get the minimum number of operations
"""


from math import sqrt


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    if n < 2:
        return 0
    prime_list = []
    while n % 2 == 0:
        prime_list.append(2)
        n /= 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_list.append(i)
            n /= i
    if n > 2:
        prime_list.append(n)
    return int(sum(prime_list))
