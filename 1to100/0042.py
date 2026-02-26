"""
Project Euler Problem 42
========================

The n-th term of the sequence of triangle numbers is given by, t[n] =
1/2n(n+1); so the first ten triangle numbers are:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""
word_list = []
with open('resources/words.txt') as f:
    word_list = f.read()[1:-1].split('","')

# get an upper bound on word value so we know how many triangle numbers to generate
max_word_len = max((len(w) for w in word_list))
max_value = max_word_len * 27
# generate list of triangle numbers
triangle_numbers = [1]
n = 2
while triangle_numbers[-1] < max_value:
    next_triangle_number = int((n*(n+1))/2)
    triangle_numbers.append(next_triangle_number)
    n += 1

triangle_word_count = 0
for word in word_list:
    value = sum([ord(c) - 64 for c in word])
    if value in triangle_numbers:
        triangle_word_count += 1


def euler_problem_42():
    print(triangle_word_count)


if __name__ == "__main__":
    euler_problem_42()
