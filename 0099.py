"""
Project Euler Problem 99
========================

Comparing two numbers written in index form like 2^11 and 3^7 is not
difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more
difficult, as both numbers contain over three million digits.

Using base_exp.txt, a 22K text file containing one thousand lines with a
base/exponent pair on each line, determine which line number has the
greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example
given above.
"""
import math

with open("resources/base_exp.txt") as f:
    data = f.read().split()

data_with_estimates = [] # list of list, each list contains base, exponent, and power when converted to base 2
largest_exponent = 0
for i in range(len(data)):
    r = data[i]
    values = r.split(',')
    data_entry = [int(values[0]), int(values[1]), math.log2(int(values[0]))*int(values[1])]
    largest_exponent = max(largest_exponent, math.log2(int(values[0]))*int(values[1]))
    data_with_estimates.append(data_entry)

for row in data_with_estimates:
    if row[2] == largest_exponent:
        print(1 + data.index(str(row[0]) + "," + str(row[1])))
