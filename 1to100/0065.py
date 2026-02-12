"""
Project Euler Problem 65
========================

The square root of 2 can be written as an infinite continued fraction.

2 = 1 +          1
        2 +        1
            2 +      1
                2 +    1
                    2 + ...

The infinite continued fraction can be written, 2 = [1;(2)], (2) indicates
that 2 repeats ad infinitum. In a similar way, 23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions
for square roots provide the best rational approximations. Let us consider
the convergents for 2.

1 + 1 = 3/2
    2

1 +   1   = 7/5
    2 + 1
        2

1 +     1     = 17/12
    2 +   1
        2 + 1
            2

1 +       1       = 41/29
    2 +     1
        2 +   1
            2 + 1
                2

Hence the sequence of the first ten convergents for 2 are:
1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378,
...

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.
"""

# generates the list of digits in the continuous fraction list of e, up to x digits
def gen_e_cf_list(x):
    if x < 1:
        return []
    ls = [2]
    for i in range(2, x+1):
        if i%3 == 0:
            ls.append(int(i*2/3))
        else:
            ls.append(1)
    return ls

# calculates convergent from list of coefficients in a continued fraction
# returns 2 ints, numerator and denominator
def calculate_convergent(cf_list):
    if len(cf_list) < 1:
        return 0
    cn = cf_list.pop() # convergent numerator
    cd = 1 # convergent denominator
    while len(cf_list) > 0:
        cn, cd = cd, cn # 1/current fraction
        cn += cf_list.pop() * cd # add next coefficient
    return cn, cd

num, den = calculate_convergent(gen_e_cf_list(100))
total = sum([int(x) for x in str(num)])

def euler_problem_65():
    print(total)

if __name__ == "__main__":
    euler_problem_65()
