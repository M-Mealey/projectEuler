"""
Project Euler Problem 34
========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

# The largest sum possible with 8 digits, 99999999, is represented by 8 * 9! = 8 * 362880 = 2903040
# The sum is only 7 digits, so it's impossible for a number with 8 or more digits to be a solution
# The range of

# For a given number of digits n, the range of possible sums of digits' factorials for an n-digit number
# is from n * 1! = n * 1 = n to n * 9! = n * 362880
# n     low     high
# 2     2       725760
# 3     3       1088640
# 4     4       1451520
# 5     5       1814400
# 6     6       2177280
# 7     7       2540160
# 8     8       2903040
# 9     9       3265920
# 10    10      3628800

# This shows that there aren't any solutions where n>7, because the upper bound of values
# for the sum of factorials of digits grows too slowly. Therefore, only numbers with 2 to 7
# digits need to be checked

import math

# naive solution, check every number under 8 digits
answer = 0
for i in range(10, 10000000):
    sum = 0
    number = i
    while number >0:
        sum += math.factorial(number%10)
        number = number//10
    if sum==i:
        answer += i



def euler_problem_34():
    print(answer)

if __name__ == "__main__":
    euler_problem_34()