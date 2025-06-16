"""
Project Euler Problem 26
========================

A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

   1/2  =  0.5
   1/3  =  0.(3)
   1/4  =  0.25
   1/5  =  0.2
   1/6  =  0.1(6)
   1/7  =  0.(142857)
   1/8  =  0.125
   1/9  =  0.(1)
  1/10  =  0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that ^1/[7] has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^1/[d] contains the longest recurring
cycle in its decimal fraction part.
"""

    
"""
Finds the longest repeating cycle by factoring each denominator to remove 5s and 2s,
then finding an integer of all 9s that is divisible by the remaining product.
The length of this all-9s number is the length of the repeating cycle.
inspiration taken from https://stackoverflow.com/questions/1315595/algorithm-for-detecting-repeating-decimals
"""
max_len = 0
index_found = 0
for i in range(2, 1000):
    # divide out 2s and 5s, these don't affect length of repeating decimal
    while i>1 and i%2 == 0:
        i = int(i/2)
    while i>4 and i%5 == 0:
        i = int(i/5)
    # find a number that's all 9s and divisible by i
    nines = 9
    while nines%i != 0:
        nines = nines * 10 + 9
    # the number of digits is the length of the repeating cycle
    if len(str(nines)) > max_len:
        max_len = len(str(nines))
        index_found = i

print(index_found)

