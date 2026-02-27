"""
Project Euler Problem 52
========================

It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

multiples = [1, 2, 3, 4, 5, 6]


def int_to_digit_list(n):
    return [(n % (10 ** b)) // (10 ** (b - 1)) for b in range(len(str(n)), 0, -1)]

# given an array, checks that all rows are equal length


def check_row_len(arr):
    for row in arr:
        if len(row) != len(arr[0]):
            return False
    return True

# given an array, checks that all rows are equal length


def check_row_digits(arr):
    for row in arr:
        if row != arr[0]:
            return False
    return True


def euler_problem_52():
    for x in range(1, 1000000):
        x_mult = [int_to_digit_list(x * m) for m in multiples]
        for r in x_mult:
            r.sort()
        if not check_row_len(x_mult):
            continue
        if check_row_digits(x_mult):
            print(x)
            break


if __name__ == "__main__":
    euler_problem_52()
