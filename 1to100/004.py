"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

"""
Determines if input int is a palindrome, returns True or False
"""
def is_palindrome(x):
    is_pal = True
    num_str = str(x)
    current_digit = 1
    while is_pal and current_digit <= len(num_str)//2:
        if num_str[current_digit-1] != num_str[-current_digit]:
            is_pal = False
        current_digit += 1
    return is_pal

"""
Finds the largest palindrome that is a product of x and a smaller 3-digit number
Returns int of largest palindrome found, or 0 if none found
"""
def largest_palindrome_x(x):
    palindrome_found = False
    largest_pal = 0
    other_factor = x
    while not palindrome_found and other_factor >= 100:
        product = x * other_factor
        if is_palindrome(product):
            largest_pal = product
            palindrome_found = True
        other_factor -= 1
    return largest_pal

"""
Finds largest palindrome that is the product of two 3-digit numbers. 
"""
def largest_palindrome():
    x = 999
    largest_found = 0
    while largest_found <= x*x:
        largest_found = max(largest_found, largest_palindrome_x(x))
        x -= 1
    return largest_found


def euler_problem_4():
    print(largest_palindrome())

if __name__ == "__main__":
    euler_problem_4()