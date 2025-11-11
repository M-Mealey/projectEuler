65"""
Project Euler Problem 77
========================

It is possible to write ten as the sum of primes in exactly five different
ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over
five thousand different ways?
"""
from helpers import is_prime
# copied coin solving logic from problem 31, but it's inefficient
p_amounts = [x for x in range(2,1000) if is_prime(x)]

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

# need to do dynamic programming approach: start with 10, calculate how many ways to write 11, etc
for x in range(11, 10000):
    # increase set by 1
    # check if len is at least 5000


