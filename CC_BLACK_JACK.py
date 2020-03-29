import random
import os


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



	return

cards = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    ]

random.shuffle(cards)

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


# player makes a decision stand or hit
while True: 
# to clear the screen
	os.system('clear')
#let's show what cards they players have
	print("Delaer Cards: [][?]".format(dealer[0]))
	print("Your Cards [{}]({})".format("][".join(player), 000000))

	break
