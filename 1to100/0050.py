"""
Project Euler Problem 50
========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from local_helpers import is_prime

longest_sequence = 0
best_prime = 0

prime_list = [x for x in range(5000) if is_prime(x)]
for i in range(len(prime_list)):
    j = i+1
    total = prime_list[i]
    while total < 1000000:
        if j > len(prime_list)-1:
            break
        total += prime_list[j]
        if total<1000000 and is_prime(total) and j-i+1 > longest_sequence:
            best_prime = total
            longest_sequence = j-i+1
        j += 1

print(best_prime)