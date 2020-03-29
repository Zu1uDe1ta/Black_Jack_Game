import random
import os

# Blackjack game 
# Compare the sums of the cards between D v P  
# If P card sum is greater than 21 = BUST
# If P card sum is less than 21 = Option Hit or Stay
# If P option Stay compare sum of D v P 
# If P sum < 21 && > D sum then P wins!
# If P sum < D sum then P loses

def calc_hand(hand):
	sum = 0

	non_aces = [card for card in hand if card != 'A']
	aces = [card for card in hand if card == 'A']


	for card in non_aces:
		if card in 'JQK':
			sum += 10
		else:
			sum += int(card)

	for card in aces: 
		if sum <= 10:
			sum += 11
		else: 
			sum += 1

	return sum

cards = [
'2♡', '3♡', '4♡', '5♡', '6♡', '7♡', '8♡', '9♡', '10♡', 'J♡', 'Q♡', 'K♡', 'A♡',
'2♢', '3♢', '4♢', '5♢', '6♢', '7♢', '8♢', '9♢', '10♢', 'J♢', 'Q♢', 'K♢', 'A♢',
'2♧", '3♧', '4♧', '5♧', '6♧', '7♧', '8♧', '9♧', '10♧', 'J♧', 'Q♧', 'K♧', 'A♧',
'2♧", '3♧', '4♧', '5♧', '6♧', '7♧', '8♧', '9♧', '10♧', 'J♧', 'Q♧', 'K♧', 'A♧',
'2♤", '3♤', '4♤', '5♤', '6♤', '7♤', '8♤', '9♤', '10♤', 'J♤', 'Q♤', 'K♤', 'A♤',
]


 	
random.shuffle(cards)

dealer = []
you = []
player2 = []

player.append(cards.pop())
you.append(cards.pop())
dealer.append(cards.pop())
player.append(cards.pop())
you.append(cards.pop())
dealer.append(cards.pop())

print(player, you, dealer)


# player makes a decision stand or hit
while True: 
# to clear the screen
	os.system('clear')
#let's show what cards they players have
	print("Delaer Cards: [][?]".format(dealer[0]))
	print("Your Cards [{}]({})".format("][".join(player), 000000))

	break
