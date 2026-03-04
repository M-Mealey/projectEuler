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

p_amounts = [1, 2, 5, 10, 20, 50, 100, 200]


def solve(coins, x):
    if len(coins) == 1:  # base case 2
        return x % coins[0] == 0
    next_coin = coins[-1]
    remaining_coins = coins[:-1]
    ways = 0
    remaining_amt = x
    while remaining_amt >= 0:
        ways += solve(remaining_coins, remaining_amt)
        remaining_amt -= next_coin
    return ways

# TODO: Try with dynamic programming? https://www.geeksforgeeks.org/understanding-the-coin-change-problem-with-dynamic-programming/


def euler_problem_31():
    print(solve(p_amounts, 200))


if __name__ == "__main__":
    euler_problem_31()
