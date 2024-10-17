#!/usr/bin/python3
'''
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that calculates
the fewest number of operations needed to result in exactly n H
characters in the file.
'''


def prime_factors(num):
    '''get prime factorization of a givrn number'''
    factors = []

    # check number of 2 in factorization
    while num % 2 == 0:
        factors.append(2)
        num //= 2

    # check for odd numbers starting from 3
    factor = 3
    while factor * factor <= num:
        while num % factor == 0:
            factors.append(factor)
            num //= factor
        factor += 2

    # if num is still a prime number > 2
    if num > 2:
        factors.append(num)
    return factors


def minOperations(n):
    '''calculates the fewest number of operations needed to result
    in exactly n H characters in the file.'''

    factors = prime_factors(n)
    return sum(factors)
