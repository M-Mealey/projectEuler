"""
Project Euler Problem 98
========================

By replacing each of the letters in the word CARE with 1, 2, 9, and 6
respectively, we form a square number: 1296 = 36^2. What is remarkable is
that, by using the same digital substitutions, the anagram, RACE, also
forms a square number: 9216 = 96^2. We shall call CARE (and RACE) a square
anagram word pair and specify further that leading zeroes are not
permitted, neither may a different letter have the same digital value as
another letter.

Using words.txt, a 16K text file containing nearly two-thousand common English
words, find all the square anagram word pairs (a palindromic word is NOT
considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""

# start by making set of all anagrams: dict with key of letters in order, value is set(?) of words with those letters
# then go through dict, for each key:
# if only one value, skip this (no anagrams)
#   find all unique letter to digit mappings, for each:
#   find values for each,  make list, then filter to only square numbers
#       to check squares, pre-generate set of all squares less than 9876543210, use set lookup
#   if list len > 1, then update largest square found
import itertools
import math

with open('resources/words.txt') as f:
    word_list = f.read()[1:-1].split('","')


anagrams = {}
for word in word_list:
    alpha_word = "".join(sorted(word))
    if alpha_word in anagrams:
        an_list = anagrams[alpha_word]
        an_list.append(word)
    else:
        an_list = [word]
        anagrams[alpha_word] = an_list

max_square = 9876543210
square_lookup = set()
for i in range(1, math.isqrt(max_square)+1):
    square_lookup.add(i*i)

def is_square(x):
    return x in square_lookup


digits = ['0','1','2','3','4','5','6','7','8','9']
# returns largest square made, 0 if none found
def find_largest_anagram_square(k, ls):
    unique_letters = sorted(list(set([ch for ch in k])))
    #print(unique_letters)
    largest_square = 0
    possible_digit_assignments = itertools.permutations(digits, len(unique_letters))
    for p in possible_digit_assignments:
        digit_assignment = dict(zip(unique_letters, p))
        numbers = []
        for word in ls:
            num_word = "".join([digit_assignment[ch] for ch in word])
            if num_word[0] != '0': # no leading zeros
                numbers.append(int(num_word))
        square_numbers = [n for n in numbers if is_square(n)]
        if len(square_numbers) > 1:
            largest_square = max(largest_square, max(square_numbers))
    return largest_square

largest_square = 0
for k in anagrams:
    if len(anagrams[k]) > 1:
        largest_square = max(largest_square, find_largest_anagram_square(k, anagrams[k]))

def euler_problem_98():
    print(largest_square)

if __name__ == "__main__":
    euler_problem_98()