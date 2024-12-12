#!/usr/bin/python3
'''Prime game code: determines if a given number
is prime and plays with the number'''


def is_prime(num):
    '''Determines if the given num parameter is a prime number'''
    if num == 1:
        return False
    elif num % 2 == 0 and num != 2:
        return False
    elif num % 3 == 0 and num != 3:
        return False
    else:
        n = 5
        while n < num:
            if num % n == 0 and num != n:
                return False
            n += 2
        return True


def isWinner(x, nums):
    '''Determins a winner among Maria and Ben
    params:
        x-number of rounds to play the game
        nums-an array of numbers to choose prime number from
    Return:
        the winner btwn Maria and Ben
    '''
    if nums == []:
        return None
    if x == 0:
        return None

    count = 0
    for _ in range(x):
        for i in nums:
            if i == 0:
                break
            new_list = []
            for j in range(1, i+1):
                new_list.append(j)
            for k in new_list:
                if is_prime(k):
                    count += 1

    if count == 0:
        return None
    elif (count % 2 == 0):
        return 'Ben'
    else:
        return 'Maria'
