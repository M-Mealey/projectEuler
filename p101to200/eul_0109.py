"""
Project Euler Problem 109
=========================

In the game of darts a player throws three darts at a target board which
is split into twenty equal sized sections numbered one to twenty.

The score of a dart is determined by the number of the region that the
dart lands in. A dart landing outside the red/green outer ring scores
zero. The black and cream regions inside this ring represent single
scores. However, the red/green outer ring and middle ring score double and
treble scores respectively.

At the centre of the board are two concentric circles called the bull
region, or bulls-eye. The outer bull is worth 25 points and the inner bull
is a double, worth 50 points.

There are many variations of rules but in the most popular game the
players will begin with a score 301 or 501 and the first player to reduce
their running total to zero is a winner. However, it is normal to play a
"doubles out" system, which means that the player must land a double
(including the double bulls-eye at the centre of the board) on their final
dart to win; any other dart that would reduce their running total to one
or lower means the score for that set of three darts is "bust".

When a player is able to finish on their current score it is called a
"checkout" and the highest checkout is 170: T20 T20 D25 (two treble 20s
and double bull).

There are exactly eleven distinct ways to checkout on a score of 6:

                                +--------+
                                |D3|  |  |
                                |--+--+--|
                                |D1|D2|  |
                                |--+--+--|
                                |S2|D2|  |
                                |--+--+--|
                                |D2|D1|  |
                                |--+--+--|
                                |S4|D1|  |
                                |--+--+--|
                                |S1|S1|D2|
                                |--+--+--|
                                |S1|T1|D1|
                                |--+--+--|
                                |S1|S3|D1|
                                |--+--+--|
                                |D1|D1|D1|
                                |--+--+--|
                                |D1|S2|D1|
                                |--+--+--|
                                |S2|S2|D1|
                                +--------+

Note that D1 D2 is considered different to D2 D1 as they finish on
different doubles. However, the combination S1 T1 D1 is considered the
same as T1 S1 D1.

In addition we shall not include misses in considering combinations; for
example, D3 is the same as 0 D3 and 0 0 D3.

Incredibly there are 42336 distinct ways of checking out in total.

How many distinct ways can a player checkout with a score less than 100?
"""

# number of way to checkout is number of possible final targets and
# for each final target, the number of ways to checkout with 2 or less?
TARGETS = {"S1": 1, "S2": 2, "S3": 3, "S4": 4, "S5": 5, "S6": 6, "S7": 7, "S8": 8, "S9": 9,
           "S10": 10, "S11": 11, "S12": 12, "S13": 13, "S14": 14, "S15": 15, "S16": 16, "S17": 17,
           "S18": 18, "S19": 19, "S20": 20, "S25": 25,
           "D1": 2, "D2": 4, "D3": 6, "D4": 8, "D5": 10, "D6": 12, "D7": 14, "D8": 16, "D9": 18,
           "D10": 20, "D11": 22, "D12": 24, "D13": 26, "D14": 28, "D15": 30, "D16": 32, "D17": 34,
           "D18": 36, "D19": 38, "D20": 40, "D25": 50,
           "T1": 3, "T2": 6, "T3": 9, "T4": 12, "T5": 15, "T6": 18, "T7": 21, "T8": 24, "T9": 27,
           "T10": 30, "T11": 33, "T12": 36, "T13": 39, "T14": 42, "T15": 45, "T16": 48, "T17": 51,
           "T18": 54, "T19": 57, "T20": 60
           }

def ways_to_checkout(x):
    """ find the number of ways to checkout with a score of x """
    final_targets = {t for t in TARGETS if t[0]=='D' and TARGETS[t] <= x }
    print(final_targets)


def solve():
    """ solve problem 109 """
    return -1

if __name__ == "__main__":
    print(solve())
    print(ways_to_checkout(6))
