"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

ones_digit = ["one", "two", "three", "four",
              "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_digit = ["twenty", "thirty", "forty", "fifty",
              "sixty", "seventy", "eighty", "ninety"]

# sum for 1 to 9
sum_ones = 0
for s in ones_digit:
    sum_ones += len(s)

# sum for 10 to 19
sum_teens = 0
for s in teens:
    sum_teens += len(s)

# sum for 20 to 99
sum_tens = 0
for s in tens_digit:
    sum_tens += 10*len(s) + sum_ones

# sum of lengths of all numbers up to 99 (inclusive)
sum_to_99 = sum_ones + sum_teens + sum_tens

# sum for 100 to 999
sum_hundreds = 0
for s in ones_digit:
    sum_hundreds += 100*len(s) + 100*len("hundred") + 99*len("and") + sum_to_99


def euler_problem_17():
    print(sum_to_99 + sum_hundreds + len("onethousand"))


if __name__ == "__main__":
    euler_problem_17()
