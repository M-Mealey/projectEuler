"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

name_list = []

with open("resources/names.txt") as f:
    data = f.read().split(',')
    data = [x[1:-1] for x in data]
    data.sort()
    name_list = data


def score_name(n):
    letter_sum = 0
    for ch in n:
        letter_sum += ord(ch) - 64
    return letter_sum


def euler_problem_22():
    name_score_sum = 0
    for i in range(len(name_list)):
        name = name_list[i]
        name_score_sum += (i + 1) * score_name(name)

    print(name_score_sum)


if __name__ == "__main__":
    euler_problem_22()
