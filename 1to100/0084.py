"""
Project Euler Problem 84
========================

In the game, Monopoly, the standard board is set up in the following way:

             GO   A1  CC1  A2  T1  R1  B1  CH1  B2   B3  JAIL
             H2                                          C1
             T2                                          U1
             H1                                          C2
             CH3                                         C3
             R4                                          R2
             G3                                          D1
             CC3                                         CC2
             G2                                          D2
             G1                                          D3
             G2J  F3  U2   F2  F1  R3  E3  E2   CH2  E1  FP

A player starts on the GO square and adds the scores on two 6-sided dice
to determine the number of squares they advance in a clockwise direction.
Without any further rules we would expect to visit each square with equal
probability: 2.5%. However, landing on G2J (Go To Jail), CC (community
chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the
player to go to directly jail, if a player rolls three consecutive
doubles, they do not advance the result of their 3rd roll. Instead they
proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a
player lands on CC or CH they take a card from the top of the respective
pile and, after following the instructions, it is returned to the bottom
of the pile. There are sixteen cards in each pile, but for the purpose of
this problem we are only concerned with cards that order a movement; any
instruction not concerned with movement will be ignored and the player
will remain on the CC/CH square.

  * Community Chest (2/16 cards):

      1. Advance to GO
      2. Go to JAIL

  * Chance (10/16 cards):

      1. Advance to GO
      2. Go to JAIL
      3. Go to C1
      4. Go to E3
      5. Go to H2
      6. Go to R1
      7. Go to next R (railway company)
      8. Go to next R
      9. Go to next U (utility company)
     10. Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular
square. That is, the probability of finishing at that square after a roll.
For this reason it should be clear that, with the exception of G2J for
which the probability of finishing on it is zero, the CH squares will have
the lowest probabilities, as 5/8 request a movement to another square, and
it is the final square that the player finishes at on each roll that we
are interested in. We shall make no distinction between "Just Visiting"
and being sent to JAIL, and we shall also ignore the rule about requiring
a double to "get out of jail", assuming that they pay to get out on their
next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we
can concatenate these two-digit numbers to produce strings that correspond
with sets of squares.

Statistically it can be shown that the three most popular squares, in
order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO
(3.09%) = Square 00. So these three most popular squares can be listed
with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the
six-digit modal string.
"""
import numpy as np
import itertools

# Can solve with Markov chains, each square is a state, 40 x 40 state space

# go to jail: if landing on 30, go to 10
# so for each column take value in row 30 and add it to row 10, set row 30 to 0
def go_to_jail_transition(tm):
    for c in range(40):
        tm[10][c] += tm[30][c]
        tm[30][c] = 0

# chance: landing on one has a 1/16 chance to send you to each of 10 destinations, 6/16 to stay
chance_destinations = {7: [0, 10, 11, 24, 39, 5, 15, 15, 12, 4],
                       22: [0, 10, 11, 24, 39, 5, 25, 25, 28, 19],
                       36: [0, 10, 11, 24, 39, 5, 5, 5, 12, 33]
                       }
def chance_transition(tm):
    for c in range(40):
        for ch in chance_destinations:
            dest_list = chance_destinations[ch]
            for dest in dest_list:
                tm[dest][c] += (1/16) * tm[ch][c]
            tm[ch][c] = (6/16) * tm[ch][c]

# community chest spaces: 1/16 move to GO (0), 1/16 move to jail (10), 14/16 stay
comm_chest = [2, 17, 33]
def cc_transition(tm):
    for c in range(40):
        for cc in comm_chest:
            tm[0][c] += (1/16) * tm[cc][c]
            tm[10][c] += (1/16) * tm[cc][c]
            tm[cc][c] = (14/16) * tm[cc][c]


#for c in range(40):
#    sum_of_column = np.sum(transition_matrix[:,c])
#    if sum_of_column != 1.0:
#        print(f"ERROR: sum of column {c} is {sum_of_column}")


# a generic create transition matrix, input is d1 and d2, each is a list that represents
# possible rolls for a die
def create_transition_matrix(d1, d2):
    outcomes = list(itertools.product(d1, d2))
    doubles = len([x for x in outcomes if x[0]==x[1]])
    p_3_doubles = (doubles/len(outcomes))**3 # probability of rolling 3 doubles
    max_roll = max([x[0]+x[1] for x in outcomes])
    rolls = [0 for _ in range(max_roll+1)]
    for r in outcomes:
        roll = r[0]+r[1]
        rolls[roll] += 1
    rolls = [x/len(outcomes) for x in rolls]

    transition_matrix = np.zeros((40, 40))
    for c in range(40):
        for i in range(len(rolls)):
            transition_matrix[(i+c)%40][c] = rolls[i] * (1-p_3_doubles)
        transition_matrix[10][c] += p_3_doubles
    go_to_jail_transition(transition_matrix)
    chance_transition(transition_matrix)
    cc_transition(transition_matrix)
    return transition_matrix



# finds steady state of a transition matrix
# input: tm, a transition matrix
# returns: np.array
def find_steady_state(tm):
    T = np.array(tm)
    for i in range(1000):
        T = T @ tm
    return T

# returns index of top 3 most common states based on steady state matrix
# input: tm, a transition matrix
# returns: list with 3 indices
def get_top_3(tm):
    states = list(tm[:,0])
    top_3 = sorted(states)[-3:]
    return [states.index(top_3[x]) for x in [2,1,0]]


if __name__ == "__main__":
    d4 = [1, 2, 3, 4]
    trans_mtx = create_transition_matrix(d4, d4)
    steady_state = find_steady_state(trans_mtx)

    top_3 = get_top_3(steady_state)
    print(f"{top_3[0]:02d}{top_3[1]:02d}{top_3[2]:02d}")

