#!/usr/binpython3
'''Prime game code'''

def is_prime(num):
    '''Determines if the given num parameter is a prime number'''


def has_prime(nums):
    '''Determines if the nums array parameter given has a Prime number'''
    for num in nums:
        if is_prime(num):
            return True
    return False


def isWinner(x, nums):
    '''Determins a winner among Maria and Ben
    params:
        x-number of rounds to play the game
        nums-an array of numbers to choose prime number from
    Return:
        the winner btwn Maria and Ben
    '''
    count = 0
    for _ in range(x):
        if has_prime(nums):
            count += 1
    if (count % 2 = 0):
        return 'Winner: Ben'
    else:
        return 'Winner: Maria'
