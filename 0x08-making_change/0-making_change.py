#!/usr/bin/python3
'''determine the fewest number of coins needed to
meet a given amount total.'''


def makeChange(coins, total):
    '''make change for a given total'''
    if total <= 0:
        return 0
    if not coins:
        return -1

    # Initialize the dp array with a high value
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make a total of 0

    # Iterate over each coin
    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    # If dp[total] is still the initialized value,
    return dp[total] if dp[total] <= total else -1
