from __future__ import print_function
import random
import os
from builtins import input
import time
from termcolor import colored, COLORS

# Blackjack game 
# Compare the sums of the cards between D v P  
# If P card sum is greater than 21 = BUST
# If P card sum is less than 21 = Option Hit or Stay
# If P option Stay compare sum of D v P 
# If P sum < 21 && > D sum then P wins!
# If P sum < D sum then P loses



cards = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
]
rank = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")

class Card(object):
    """Represents an individual playing card"""
    def value(self):
        """Computes the value of a card according to Blackjack rules"""
        if self.ace():
            value = 11
        else:
            try:
                value = int(self.rank)
            except ValueError:
                value = 10
        return value

    def calc_hand(hand):
	    sum = 0

dealer = []
you = []
player = []

player.append(cards.pop())
you.append(cards.pop())
dealer.append(cards.pop())
player.append(cards.pop())
you.append(cards.pop())
dealer.append(cards.pop())

print(player, you, dealer)





random.shuffle(cards)











#if __name__ == '__main__':
    # main()
