"""
Project Euler Problem 112
=========================

Working from left-to-right if no digit is exceeded by the digit to its
left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing
a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just
over half of the numbers below one-thousand (525) are bouncy. In fact, the
least number for which the proportion of bouncy numbers first reaches 50%
is 538.

Surprisingly, bouncy numbers become more and more common and by the time
we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is
exactly 99%.
"""

def is_bouncy(x):
    """ check if int x it bouncy. Return bool """
    if x < 100:
        return False
    is_inc, is_dec = True, True
    d = x%10
    x = x//10
    while x > 0:
        last_d = d
        d = x%10
        x = x//10
        if d > last_d:
            is_inc = False
        if d < last_d:
            is_dec = False
    return not (is_inc or is_dec)

def solve():
    """ solve problem 112 """
    bouncy_count = 269
    i = 538
    while bouncy_count/i < .99:
        i += 1
        if is_bouncy(i):
            bouncy_count += 1
    return i

if __name__ == "__main__":
    print(solve())
