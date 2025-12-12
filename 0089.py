"""
Project Euler Problem 89
========================

The rules for writing Roman numerals allow for many ways of writing each
number. However, there is always a "best" way of writing a particular number.

For example, the following represent all of the legitimate ways of writing
the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the least
number of numerals.

The 11K text file roman.txt contains one thousand numbers written in valid,
but not necessarily minimal, Roman numerals; that is, they are arranged in
descending units and obey the subtractive pair rule (see FAQ for the
definitive rules for this problem).

Find the number of characters saved by writing each of these in their
minimal form.

Note: You can assume that all the Roman numerals in the file contain no
more than four consecutive identical units.

FAQ Link: http://projecteuler.net/about=roman_numerals
"""

# From the FAQ:
#
# Traditional Roman numerals are made up of the following denominations:
#
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
#
# In order for a number written in Roman numerals to be considered valid there are three basic rules which must be followed.
#
# Numerals must be arranged in descending order of size.
# M, C, and X cannot be equalled or exceeded by smaller denominations.
# D, L, and V can each only appear once.

# given an integer, returns string of roman numeral in minimal form
def int_to_roman(n):
    if n > 1000:
        return "M" + int_to_roman(n-1000)
    elif n > 500:
        return "D" + int_to_roman(n-500)
    elif n > 100:
        return "C" + int_to_roman(n-100)
    elif n > 50:
        return "L" + int_to_roman(n-50)
    elif n>10:
        return "X" + int_to_roman(n-10)
    elif n>5:
        return "V" + int_to_roman(n-5)
    elif n>0:
        return "I" + int_to_roman(n-1)
    else:
        return ""

print(int_to_roman(49))