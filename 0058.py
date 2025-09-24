"""
Project Euler Problem 58
========================

Starting with 1 and spiralling anticlockwise in the following way, a
square spiral with side length 7 is formed.

                           37 36 35 34 33 32 31
                           38 17 16 15 14 13 30
                           39 18  5  4  3 12 29
                           40 19  6  1  2 11 28
                           41 20  7  8  9 10 27
                           42 21 22 23 24 25 26
                           43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers
lying along both diagonals are prime; that is, a ratio of 8/13 62%.

If one complete new layer is wrapped around the spiral above, a square
spiral with side length 9 will be formed. If this process is continued,
what is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?
"""
from helpers import is_prime
# like problem 28
# ring 0 is 1x1, ring 1 is 3x3, ring 2 is 5x5, ring 3 is 7x7, etc.
# a 1001 by 1001 grid has 501 "rings" (inc ring 0), ring 500 is 1001x1001
# ring x is (2x+1)x(2x+1), contains 8x numbers
prime_count = 0
count = 1
end_of_ring = 1 # tracks end of previous ring
side_len = 1
for r in range(1,400):
    # each corner is 2r steps up from the last corner, where r is the ring # the corner is in
    if is_prime(end_of_ring + 2*r):
        prime_count += 1
    if is_prime(end_of_ring + 4*r):
        prime_count += 1
    if is_prime(end_of_ring + 6*r):
        prime_count += 1
    if is_prime(end_of_ring + 8*r):
        prime_count += 1
    count += 4
    side_len = 2*r + 1
    if prime_count / count <= 0.1:
        break
    end_of_ring = end_of_ring + 8*r
print(f"{prime_count}/{count}")
print(side_len)

