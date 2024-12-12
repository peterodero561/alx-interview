#!/usr/bin/python3
'''Python prime game to determine a winner using given number'''


def isWinner(x, nums):
    '''method to choose who is winnner btwn Maria and Ben'''
    def sieve(n):
        """Generates a list of prime numbers up to n using
        the Sieve of Eratosthenes."""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    # Find the maximum n in nums to precompute primes
    max_n = max(nums)
    primes = sieve(max_n)

    def calculate_moves(n):
        """Calculates the number of moves possible for a given n."""
        numbers = list(range(1, n + 1))
        used = [False] * (n + 1)
        moves = 0

        for i in range(2, n + 1):
            if primes[i] and not used[i]:
                moves += 1
                # Mark i and its multiples as used
                for j in range(i, n + 1, i):
                    used[j] = True

        return moves

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1  # No primes available, Ben wins
        else:
            moves = calculate_moves(n)
            # Maria wins if the number of moves is odd, Ben wins if it's even
            if moves % 2 == 1:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
