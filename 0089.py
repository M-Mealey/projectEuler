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
    str = ""
    if n >= 1000:
        str += "M" + int_to_roman(n-1000)
    elif n>= 900:
        str += "CM" + int_to_roman(n-900)
    elif n >= 500:
        str += "D" + int_to_roman(n-500)
    elif n >= 400:
        str += "CD" + int_to_roman(n-400)
    elif n >= 100:
        str += "C" + int_to_roman(n-100)
    elif n >= 90:
        str += "XC" + int_to_roman(n-90)
    elif n >= 50:
        str += "L" + int_to_roman(n-50)
    elif n >= 40:
        str += "XL" + int_to_roman(n-40)
    elif n >= 10:
        str += "X" + int_to_roman(n-10)
    elif n >= 9:
        str += "IX" + int_to_roman(n-9)
    elif n >= 5:
        str += "V" + int_to_roman(n-5)
    elif n >= 4:
        str += "IV" + int_to_roman(n-4)
    elif n>0:
        str += "I" + int_to_roman(n-1)
    return str

print(int_to_roman(5))

# test cases from https://www.cuemath.com/numbers/roman-numerals-1-to-1000/
test_numerals = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X", 11: "XI", 12: "XII",
    13: "XIII", 14: "XIV", 15: "XV", 16: "XVI", 17: "XVII", 18: "XVIII", 19: "XIX", 20: "XX", 21: "XXI", 22: "XXII",
    23: "XXIII", 24: "XXIV", 25: "XXV", 26: "XXVI", 27: "XXVII", 28: "XXVIII", 29: "XXIX", 30: "XXX", 31: "XXXI",
    32: "XXXII", 33: "XXXIII", 34: "XXXIV", 35: "XXXV", 36: "XXXVI", 37: "XXXVII", 38: "XXXVIII", 39: "XXXIX", 40: "XL",
    41: "XLI", 42: "XLII", 43: "XLIII", 44: "XLIV", 45: "XLV", 46: "XLVI", 47: "XLVII", 48: "XLVIII", 49: "XLIX",
    50: "L", 55: "LV", 60: "LX", 65: "LXV", 70: "LXX", 75: "LXXV", 80: "LXXX", 85: "LXXXV", 90: "XC", 95: "XCV",
    100: "C", 105: "CV", 185: "CLXXXV", 290: "CCXC", 395: "CCCXCV", 500: "D", 605: "DCV", 285: "CCLXXXV", 390: "CCCXC",
    495: "CDXCV", 600: "DC", 705: "DCCV", 385: "CCCLXXXV", 490: "CDXC", 595: "DXCV", 700: "DCC", 805: "DCCCV",
    485: "CDLXXXV", 590: "DXC", 695: "DCXCV", 800: "DCCC", 905: "CMV", 585: "DLXXXV", 690: "DCXC", 795: "DCCXCV",
    900: "CM", 1000: "M"}


for k in test_numerals:
    s1 = int_to_roman(k)
    s2 = test_numerals[k]
    if s1 != s2:
        print(f"ERROR: {k}")
        print(s1)
        print(s2)
        print()
