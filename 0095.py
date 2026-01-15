"""
Project Euler Problem 95
========================

The proper divisors of a number are all the divisors excluding the number
itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As
the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of
the proper divisors of 284 is 220, forming a chain of two numbers. For
this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with
12496, we form an amicable chain of five numbers:

                12496 14288 15472 14536 14264 ( 12496 ...)

Find the smallest member of the longest amicable chain with no element
exceeding one million.
"""

# probably better to make array of 1M elements, iterate 1 to 1M, for each number add it to the element at
# each of its multiples' indexes
# start with array of 1s: (all will have 1 as a divisor except 0 and 1]
# [0, 0, 1, 1, 1, 1, 1, 1, 1, 1 ...]
# next number is 2
# [0, 1, 1, 1, 3, 1, 3, 1, 3, 1, ...]
# 3
# [0, 1, 1, 1, 2, 1, 5, 1, 2, 4 ...]
# then find loops using Floyd's cycle detection algorithm: https://en.wikipedia.org/wiki/Cycle_detection

max_value = 1000000

divisor_sums = [1 for _ in range(max_value)]
divisor_sums[0] = 0
divisor_sums[1] = 0
for i in range(2, max_value//2 + 1):
    next_multiple = i + i
    while next_multiple < 1000000:
        divisor_sums[next_multiple] += i
        next_multiple += i

# iterate over array in order looking for cycles
# if value of 0 or >1M is encountered, stop there, no cycle
longest_cycle_found = 0
smallest_cycle_member = 0
all_numbers_checked = set()
for i in range(2, 1000000):
    if i in all_numbers_checked:
        continue
    numbers_this_cycle = set()
    numbers_this_cycle.add(i)
    next_num = divisor_sums[i]
    while next_num > 1 and next_num < 1000000 and next_num not in numbers_this_cycle and next_num not in all_numbers_checked:
        numbers_this_cycle.add(next_num)
        next_num = divisor_sums[next_num]
    if 1 < next_num < 1000000 and next_num not in all_numbers_checked and next_num in numbers_this_cycle: #cycle found, starts/ends at next_num
        # make a set with ONLY numbers in the cycle
        cycle_start = next_num
        cycle_len = 1
        min_elem = cycle_start
        next_num = divisor_sums[cycle_start]
        while next_num != cycle_start:
            cycle_len += 1
            min_elem = min(min_elem, next_num)
            next_num = divisor_sums[next_num]
        if cycle_len > longest_cycle_found:
            longest_cycle_found = cycle_len
            smallest_cycle_member = min_elem
        #the_cycle = set()
        #the_cycle.add(next_num)
        #next = divisor_sums[next_num]
        #while next != next_num:
        #    the_cycle.add(next)
        #    next = divisor_sums[next]
        #if len(the_cycle) > longest_cycle_found:
        #    longest_cycle_found = len(the_cycle)
        #    smallest_cycle_member = min(the_cycle)
        # @TODO: is set or iteration faster?
        all_numbers_checked.update(numbers_this_cycle)
print(smallest_cycle_member)




