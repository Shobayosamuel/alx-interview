#!/usr/bin/python3
"""Function to determine the fewest number of coin"""


def makeChange(coins, total):
    """Return the fewest number of coin"""
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        val = total // coin
        count += val
        total -= coin * val
    
    return count if total == 0 else -1
