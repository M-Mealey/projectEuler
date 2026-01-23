"""
Project Euler Problem 30
========================

Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

  1634 = 1^4 + 6^4 + 3^4 + 4^4
  8208 = 8^4 + 2^4 + 0^4 + 8^4
  9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""

# 9**5 = 59049
# 6 digit max = 6*(9^5) = 354294
# 7 digit max = 7*59049 = 413343
# Therefore, possible answers have max of 6 digits

# naive solution: iterate over all numbers, find sum of 5th power of digits
solutions = []
for x in range(2, 1000000):
    digit_sum = (x%10)**5
    digit_sum += ((x//10)%10)**5
    digit_sum += ((x // 100) % 10) ** 5
    digit_sum += ((x // 1000) % 10) ** 5
    digit_sum += ((x // 10000) % 10) ** 5
    digit_sum += ((x // 100000) % 10) ** 5
    if digit_sum==x:
        solutions.append(x)

# solutions = [4150, 4151, 54748, 92727, 93084, 194979]
print(sum(solutions))

