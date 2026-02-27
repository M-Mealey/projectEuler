"""
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
from local_helpers import is_prime

# highest number to search
max_number = 1000
primes = [p for p in range(2, max_number) if is_prime(p)]

# keep list of how many prime combos there are for each number
prime_combos = [0 for _ in range(max_number + 1)]

# for each prime, iterate over indexes in solution list
# solutions for index i += solutions for index i - (prime), like appending the prime to the sum
# no risk of double-counting because this goes in ascending order
for p in primes:
    # counting prime number itself as one way to write sum
    prime_combos[p] += 1
    for i in range(p, max_number):
        prime_combos[i] += prime_combos[i-p]


def euler_problem_77():
    # print first index with more than 5000 combos
    for pc in prime_combos:
        if pc > 5000:
            print(prime_combos.index(pc))
            break


if __name__ == "__main__":
    euler_problem_77()
