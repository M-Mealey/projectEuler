"""
Project Euler Problem 79
========================

A common security method used for online banking is to ask the user for
three random characters from a passcode. For example, if the passcode was
531278, they may asked for the 2nd, 3rd, and 5th characters; the expected
reply would be: 317.

The text file keylog.txt contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the
file so as to determine the shortest possible secret passcode of unknown
length.
"""

with open("resources/keylog.txt") as f:
    data = f.read().split()

# I solved this on paper and each digit is only used once, so this solution will assume that
# idea: the true first digit will always appear first, create function that scans all entries,
# finds which things only appear first then remove them from each of the login attempts and repeat
# Eventually attempt list should be empty and we have the password.


def get_first(ls):
    first_digits = set()
    not_first = set()
    for i in ls:
        first_digits.update(i[0])
        not_first.update(i[1:])
    solutions = first_digits - not_first
    if len(solutions) > 1:
        print("OH NO")
    else:
        return solutions.pop()


def remove_char(ls, ch):
    new_list = []
    for i in range(len(ls)):
        if ch in ls[i]:
            if len(ls[i]) > 1:
                new_list.append(ls[i][1:])
        else:
            new_list.append(ls[i])
    return new_list


pw = ""
while len(data) > 0:
    next_char = get_first(data)
    pw += next_char
    data = remove_char(data, next_char)


def euler_problem_79():
    print(pw)


if __name__ == "__main__":
    euler_problem_79()
