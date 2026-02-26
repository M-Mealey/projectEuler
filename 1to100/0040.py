"""
Project Euler Problem 40
========================

An irrational decimal fraction is created by concatenating the positive
integers:

                  0.123456789101112131415161718192021...
                               ^

It can be seen that the 12th digit of the fractional part is 1.

If d[n] represents the n-th digit of the fractional part, find the value
of the following expression.

    d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
"""

# Given last integer appended x, digit pointer pointer, and target index d
# returns the digit at index d in the irrational integer


def get_digit(x, pointer, d):
    while pointer > d:
        x = x//10
        pointer -= 1
    return x % 10


d_list = [1, 10, 100, 1000, 10000, 100000, 1000000]
digit_pointer = 0
x = 1
product = 1
while digit_pointer < 1000000:
    digit_pointer += len(str(x))
    if digit_pointer >= d_list[0]:
        product *= get_digit(x, digit_pointer, d_list[0])
        d_list.pop(0)
    x += 1


def euler_problem_40():
    print(product)


if __name__ == "__main__":
    euler_problem_40()
