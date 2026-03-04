"""
Project Euler Problem 36
========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

# checks if base 10 int x is a palindrome, returns True or False


def is_palindrome_b10(x):
    x_string = str(x)
    for d in range(len(x_string)//2):
        if x_string[d] != x_string[-1-d]:
            return False
    return True


def is_palindrome_b2(x):
    x_bin_str = bin(i)[2:]
    for d in range(len(x_bin_str)//2):
        if x_bin_str[d] != x_bin_str[-1-d]:
            return False
    return True


# naive way: iterate over all numbers less than 1M, check if both representations are palindromes
sum = 0
for i in range(1000000):
    if is_palindrome_b10(i) and is_palindrome_b2(i):
        sum += i
# print(sum)

# More efficient way: use math to generate all binary palindromes, then check if their
# base 10 representation is a palindrome
# 1 million in binary: 11110100001001000000[2], 20 digits
# can get all binary palindromes by making list of all binary numbers with 10 or less digits,
# then "flipping" them and appending that to the first half, then also adding both middle digits
# eg. 1 => 11, 101, 111
# 10 => 1001, 10001, 10101
# 11 => 1111, 11011, 11111
# 100 => 100001, 1000001, 1001001
# keep doing this until 976[10] = 1111010000[2], the first 10 digits of 1 million in binary.

# 1[10] == 1[2] is a valid answer that this method won't find, so sum starts at 1
sum = 1

second_solutions = []
for i in range(1, 977):
    bin_str = bin(i)[2:]
    bin_palindromes = [bin_str + bin_str[::-1], bin_str +
                       '0' + bin_str[::-1], bin_str + '1' + bin_str[::-1]]
    for pal in bin_palindromes:
        pal_b10 = int(pal, 2)
        if pal_b10 < 1000000 and is_palindrome_b10(pal_b10):
            second_solutions.append(pal_b10)
            sum += pal_b10

# print(sum)
# @TODO: measure speed of each


def euler_problem_36():
    print(sum)


if __name__ == "__main__":
    euler_problem_36()
