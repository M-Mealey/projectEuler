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
# In order for a number written in Roman numerals to be considered valid
# there are three basic rules which must be followed.
#
# Numerals must be arranged in descending order of size.
# M, C, and X cannot be equalled or exceeded by smaller denominations.
# D, L, and V can each only appear once.

numeral_values = {"M": 1000, "D": 500,
                  "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
subtractive_pairs = {"CM": 900, "CD": 400,
                     "XC": 90, "XL": 40, "IX": 9, "IV": 4}

def int_to_roman(n):
    """ given an integer, returns string of roman numeral in minimal form """
    num_str = ""
    all_values = numeral_values | subtractive_pairs
    all_values = dict(sorted(all_values.items(), key=lambda item: -item[1],))
    for chs, val in all_values.items():
        if val <= n:
            num_str = chs + int_to_roman(n-val)
            break
    return num_str

def get_subtractive_pair_values(num):
    """ totals the value of all subtractive pairs present in a numeral,
    returns numeral with those pairs removed """
    value = 0
    for pair, p_val in subtractive_pairs.items():
        if pair in num:
            value += p_val
            num = num.replace(pair, "")
    return value, num


def get_int_value(num):
    """ get the integer value of a given numeral """
    if len(num) == 0:
        return 0
    val, n = get_subtractive_pair_values(num)
    for ch in n:
        val += numeral_values[ch]
    return val

### BEGIN TEST CASES ###
# @TODO: move to test file :)
# test cases from https://www.cuemath.com/numbers/roman-numerals-1-to-1000/
test_numerals = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
                 10: "X", 11: "XI", 12: "XII", 13: "XIII", 14: "XIV", 15: "XV", 16: "XVI",
                 17: "XVII", 18: "XVIII", 19: "XIX", 20: "XX", 21: "XXI", 22: "XXII", 23: "XXIII",
                 24: "XXIV", 25: "XXV", 26: "XXVI", 27: "XXVII", 28: "XXVIII", 29: "XXIX",
                 30: "XXX", 31: "XXXI", 32: "XXXII", 33: "XXXIII", 34: "XXXIV", 35: "XXXV",
                 36: "XXXVI", 37: "XXXVII", 38: "XXXVIII", 39: "XXXIX", 40: "XL", 41: "XLI",
                 42: "XLII", 43: "XLIII", 44: "XLIV", 45: "XLV", 46: "XLVI", 47: "XLVII",
                 48: "XLVIII", 49: "XLIX", 50: "L", 55: "LV", 60: "LX", 65: "LXV", 70: "LXX",
                 75: "LXXV", 80: "LXXX", 85: "LXXXV", 90: "XC", 95: "XCV", 100: "C", 105: "CV",
                 185: "CLXXXV", 290: "CCXC", 395: "CCCXCV", 500: "D", 605: "DCV", 285: "CCLXXXV",
                 390: "CCCXC", 495: "CDXCV", 600: "DC", 705: "DCCV", 385: "CCCLXXXV", 490: "CDXC",
                 595: "DXCV", 700: "DCC", 805: "DCCCV", 485: "CDLXXXV", 590: "DXC", 695: "DCXCV",
                 800: "DCCC", 905: "CMV", 585: "DLXXXV", 690: "DCXC", 795: "DCCXCV",
                 900: "CM", 1000: "M"}


for k, num_k in test_numerals.items():
    if int_to_roman(k) != num_k:
        print(f"ERROR: {k}")



for x, test_str in test_numerals.items():
    test_int_val = get_int_value(test_str)
    if test_int_val != x:
        print(f"ERROR: {x}")
        print(test_int_val)
        print()
### END TESTS ###



def solve(input_files=("resources/roman.txt",)):
    """ solve problem 89 """
    with open(input_files[0], 'r', encoding='utf-8') as f:
        data = f.read().split("\n")
        characters_saved = 0
        for numeral in data:
            numeral_as_int = get_int_value(numeral)
            minimal_numeral = int_to_roman(numeral_as_int)
            diff = len(numeral) - len(minimal_numeral)
            if diff < 0:
                print("THIS SHOULDN'T HAPPEN")
                print(numeral)
            characters_saved += diff
        return characters_saved


if __name__ == "__main__":
    print(solve())
