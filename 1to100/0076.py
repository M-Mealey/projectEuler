"""
Project Euler Problem 76
========================

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least
two positive integers?
"""

# copied coin solving logic from problem 31, but it's inefficient
p_amounts = [x for x in range(1,100)]

def solve(coins, x):
    if len(coins) == 1: # base case 2
        return x%coins[0] == 0
    next_coin = coins[-1]
    remaining_coins = coins[:-1]
    ways = 0
    remaining_amt = x
    while remaining_amt >= 0:
        ways += solve(remaining_coins, remaining_amt)
        remaining_amt -= next_coin
    return ways

def euler_problem_76():
    print(solve(p_amounts, 100))

if __name__ == "__main__":
    euler_problem_76()