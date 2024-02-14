#!/usr/bin/python3
"""Prime Game
"""
def is_prime(x):
    """Find prime
    """
    return x > 1 and x % 2 != 0 and x % 3 != 0


def isWinner(x, nums):
    """Find winner
    """
    rounds = x
    array = nums
    if rounds > len(array):
        return
    this_round = {'Ben': 0, 'Mariah': 0}
    overall = {'Ben': 0, 'Mariah': 0}
    for run in range(rounds):
        arr = [x for x in range(1, array[run] + 1)]
        copy = arr.copy()
        player = 'Mariah'
        for index in range(len(arr)):
            # One game a loop
            if player == 'Ben':
                player = 'Mariah'
            else:
                player = 'Ben'

            if is_prime(arr[index]):
                arr[index] = 1
                this_round[player] += 1
                for x in arr:
                    if x != 1 and x % arr[index] == 0:
                        arr[arr.index(x)] = 1
                        this_round[player] += 1
            else:
                continue
        if this_round['Ben'] > this_round['Mariah']:
            overall['Ben'] += 1
        elif this_round['Mariah'] > this_round['Ben']:
            overall['Mariah'] += 1
        else:
            overall['Ben'] += 1
            overall['Mariah'] += 1
    winner = ''
    if overall['Ben'] > overall['Mariah']:
        winner = 'Ben'
    elif overall['Mariah'] > overall['Ben']:
        winner = 'Mariah'
    else:
        winner = None
    return winner
