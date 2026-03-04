"""
Project Euler Problem 78
========================

Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can separated into piles in
exactly seven different ways, so p(5)=7.

                            OOOOO

                            OOOO   O

                            OOO   OO

                            OOO   O   O

                            OO   OO   O

                            OO   O   O   O

                            O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""
max_number = 100000
perms = [1]+[0]*max_number
pent_numbers = [int((x*(3*x-1))/2) for x in range(1000)] + \
    [int((x*(3*x+1))/2) for x in range(1000)]
pent_numbers = [x for x in pent_numbers if x > 0]
pent_numbers.sort()

# Solve using pentagonal number theorem: https://en.wikipedia.org/wiki/Pentagonal_number_theorem
# note that (-1)**(k//2) is used instead of (-1)**(k-1). This is because the list of "indexes" for the generalized
# pentagonal numbers would normally be [1, -1, 2, -2, 3, -3, ...], but here I'm using the list indices
# applying (-1)**(k-1) to each item in [1, -1, 2, -2, 3, -3, ...] yields [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, ...]
# which is equal to (-1)**(k//2) applied to [0, 1, 2...]
for n in range(1, max_number+1):
    for k in range(len(pent_numbers)):
        if pent_numbers[k] > n:
            break
        perms[n] += (-1)**(k//2) * perms[n-pent_numbers[k]]


def euler_problem_78():
    for p in perms:
        if p % 1000000 == 0:
            print(perms.index(p))
            break


if __name__ == "__main__":
    euler_problem_78()
