"""
Project Euler Problem 54
========================

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

  * High Card: Highest value card.
  * One Pair: Two cards of the same value.
  * Two Pairs: Two different pairs.
  * Three of a Kind: Three cards of the same value.
  * Straight: All cards are consecutive values.
  * Flush: All cards of the same suit.
  * Full House: Three of a kind and a pair.
  * Four of a Kind: Four cards of the same value.
  * Straight Flush: All cards are consecutive values of same suit.
  * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players
have a pair of queens, then highest cards in each hand are compared (see
example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

Consider the following five hands dealt to two players:

        Hand   Player 1            Player 2              Winner
        1      5H 5C 6S 7S KD      2C 3S 8S 8D TD        Player 2
               Pair of Fives       Pair of Eights
        2      5D 8C 9S JS AC      2C 5C 7D 8S QH        Player 1
               Highest card Ace    Highest card Queen
        3      2D 9C AS AH AC      3D 6D 7D TD QD        Player 2
               Three Aces          Flush with Diamonds
               4D 6S 9H QH QC      3D 6D 7H QD QS
        4      Pair of Queens      Pair of Queens        Player 1
               Highest card Nine   Highest card Seven
               2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
        5      Full House          Full House            Player 1
               With Three Fours    with Three Threes

The file poker.txt contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated
cards), each player's hand is in no specific order, and in each hand there
is a clear winner.

How many hands does Player 1 win?
"""

# Ace can also be 1, but the only situation in this problem where you would count it as 1 is if it's in a straight
# so that special case can be handled separately
card_values = {'2':2, '3':3, '4': 4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

hands = []
with open("resources/poker.txt") as f:
    hands = f.read().split('\n')[:-1]

p1_win_count = 0

def check_flush(hand):
    return hand[0][1]==hand[1][1] and hand[0][1]==hand[2][1] and hand[0][1]==hand[3][1] and hand[0][1]==hand[4][1]

def check_straight(hand):
    if hand == [2, 3, 4, 5, 14]: # special case, A can be 1 in a straight
        return True
    if [c - hand[0] for c in hand] == [0,1,2,3,4]:
        return True
    return False

# returns
def count_multiples(hand):
    cards = {}
    for c in hand:
        cards[c] = cards.get(c, 0) + 1
    return dict(sorted(cards.items(), key = lambda item: item[1], reverse=True))

# returns 2 values: score and tiebreaker info
def grade_hand(hand):
    card_int_values = [card_values[c[0]] for c in hand]
    card_int_values.sort()
    # suit only matters for flush, so check for 3 flush types together
    # for straights: ties are broken on simple high card, tiebreaker is max card
    # for simple flush: tiebreaker is list of card values, descending
    if check_flush(hand):
        if card_int_values == [10, 11, 12, 13, 14]:
            # for royal straight and all other straights, tiebreaker is simple highest card.
            return 9, [max(card_int_values)] # royal flush
        elif check_straight(card_int_values):
            return 8, [max(card_int_values)] # straight flush
        else:
            return 5, sorted(card_int_values, reverse=True) # simple flush
    elif check_straight(card_int_values):
        return 4, [max(card_int_values)] # simple straight
    else:
        # for other hands, tiebreaker is list of card values by frequency they occur, cards with the same frequency
        # are sorted by descending values
        card_int_values = list(sorted(card_int_values, reverse=True))
        card_counts = count_multiples(card_int_values)
        tiebreaker = list(card_counts.keys())
        vals = sorted(list(card_counts.values()), reverse=True)
        if 4 in vals:
            return 7 , tiebreaker # 4 of a kind
        elif 3 in vals:
            if 2 in vals:
                return 6, tiebreaker # full house
            return 3, tiebreaker # 3 of a kind
        elif 2 in vals:
            if vals  == [2,2,1]:
                return 2, tiebreaker # 2 pairs
            return 1, tiebreaker # 1 pair
        return 0, tiebreaker # high card

def resolve_tiebreaker(t1, t2):
    if t1[0] == t2[0]:
        return resolve_tiebreaker(t1[1:], t2[1:])
    else:
        return t1[0] > t2[0]

for h in hands:
    p1_cards, p2_cards = h.split()[:5], h.split()[5:]
    p1_cards.sort()
    p2_cards.sort()
    score1, tie1 = grade_hand(p1_cards)
    score2, tie2 = grade_hand(p2_cards)
    if score1 > score2:
        p1_win_count += 1
    elif score1 == score2:
        if resolve_tiebreaker(tie1, tie2):
            p1_win_count += 1

def euler_problem_54():
    print(p1_win_count)

if __name__ == "__main__":
    euler_problem_54()