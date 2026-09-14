"""
Project Euler Problem 113
=========================

Working from left-to-right if no digit is exceeded by the digit to its
left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing
a "bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such
that there are only 12951 numbers below one-million that are not bouncy
and only 277032 non-bouncy numbers below 10^10.

How many numbers below a googol (10^100) are not bouncy?
"""

def solve():
    """ solve problem 113 """
    n = 100
    # every decreasing number is an increasing number backwards
    # the only numbers that count as both are all one digit (eg 999999999999)
    # total = 2* number of increasing numbers - all-one-digit numbers

    current_n = 1
    increasing_by_n = {1:9}
    number_dict = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}
    while current_n < n:

        new_number_dict = {}
        for x in range(1,10):
            possible_following_digits = list(range(x, 10))
            count = 0
            for p in possible_following_digits:
                count += number_dict[p]
            new_number_dict[x] = count
        number_dict = new_number_dict
        current_n += 1
        increasing_by_n[current_n] = sum(number_dict.values())

    total_nonbouncy = 0
    for k, v in increasing_by_n.items():
        total_nonbouncy += 2*v - 9 #9 for the 9 same-digit numbers of k digits
        # leading zeroes don't effect increasing numbers, but trailing zeros make new dec numbers
        # every decreasing number can have zeros added until there are n digits
        total_nonbouncy += v * (n-k)

    return total_nonbouncy

if __name__ == "__main__":
    print(solve())

