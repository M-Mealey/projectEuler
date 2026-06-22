"""
Project Euler Problem 31
========================

In England the currency is made up of pound, -L-, and pence, p, and there
are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, -L-1 (100p) and -L-2 (200p).

It is possible to make -L-2 in the following way:

  1 * -L-1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can -L-2 be made using any number of coins?
"""
import time


def find_combinations(coins, x):
    """ find the number of ways the coins with values in list coins can combine to a total of x """
    if len(coins) == 1:  # base case 2
        return x % coins[0] == 0
    next_coin = coins[-1]
    remaining_coins = coins[:-1]
    ways = 0
    remaining_amt = x
    while remaining_amt >= 0:
        ways += find_combinations(remaining_coins, remaining_amt)
        remaining_amt -= next_coin
    return ways


def find_combinations_dynamic(coins, x):
    """ find the ways to make x with given coins using dynamic programming approach
    https://www.geeksforgeeks.org/understanding-the-coin-change-problem-with-dynamic-programming/
    """
    ways_array = [0 for _ in range(x+1)]
    ways_array[0] = 1
    for c in coins:
        for i, ways in enumerate(ways_array):
            if i-c >= 0:
                ways_array[i] = ways + ways_array[i-c]
    return ways_array[x]


def time_solutions():
    """ time the difference between the regular and dynamic programming solutions"""
    p_amounts = [1, 2, 5, 10, 20, 50, 100, 200]
    start1 = time.perf_counter()
    find_combinations(p_amounts, 200)
    end1 = time.perf_counter()
    print(f"solution 1: {end1 - start1}")

    start2 = time.perf_counter()
    find_combinations_dynamic(p_amounts, 200)
    end2 = time.perf_counter()
    print(f"solution 2: {end2 - start2}")


def solve():
    """ solve problem 31 """
    p_amounts = [1, 2, 5, 10, 20, 50, 100, 200]
    return find_combinations_dynamic(p_amounts, 200)


if __name__ == "__main__":
    print(solve())
