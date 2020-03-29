import os
import random


def calc_hand(hand):
    non_aces = [c for c in hand if c != 'A']
    aces = [c for c in hand if c == 'A']

    sum = 0

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

while True:
    cards = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    ]

    random.shuffle(cards)

    dealer = []
    player = []

    player.append(cards.pop())
    dealer.append(cards.pop())
    player.append(cards.pop())
    dealer.append(cards.pop())

    first_hand = True
    standing = False

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        player_score = calc_hand(player)
        dealer_score = calc_hand(dealer)

        if standing:
            print('Dealer Cards: [{}] ({})'.format(']['.join(dealer), dealer_score))
        else:
            print('Dealer Cards: [{}][?]'.format(dealer[0]))

        print('Your Cards:   [{}] ({})'.format(']['.join(player), player_score))
        print('')

        if standing:
            if dealer_score > 21:
                print('Dealer busted, you win!')
            elif player_score == dealer_score:
                print('Push, nobody wins')
            elif player_score > dealer_score:
                print('You beat the dealer, you win!')
            else:
                print('You lose :(')

            print('')
            input('Play again? Hit enter to continue')
            break

        if first_hand and player_score == 21:
            print('Blackjack! Nice!')
            print('')
            input('Play again? Hit enter to continue')
            break

        if player_score > 21:
            print('You busted!')
            print('')
            input('Play again? Hit enter to continue')
            break

        print('What would you like to do?')
        print(' [1] Hit')
        print(' [2] Stand')

        print('')
        choice = input('Your choice: ')
        print('')

        first_hand = False

        if choice == '1':
            player.append(cards.pop())
        elif choice == '2':
            standing = True
            while calc_hand(dealer) <= 16:
                dealer.append(cards.pop())




############
# BlackJack or 21 game
import random
# THE PLANNING PHASE
cards = []

 # Dealer cards
dealer_cards = []
 # Player cards
player_cards = []
# Deal the cards
# Display the cards
# Dealer Cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has X &", dealer_cards[1])

# Player Cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have ", player_cards)
 
 # Sum of the Dealer cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")

# Sum of the Player cards
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit?  "))
    if action_taken == "hit":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
        else:
            print("You win!")
            break

if sum(player_cards) > 21:
    print("You BUSTED! Dealer wins.")
elif sum(player_cards) == 21:
    print("You have BLACKJACK! You Win!! 21")

 # Compare the sums of the cards between D v P  
 # If P card sum is greater than 21 = BUST
 # If P card sum is less than 21 = Option Hit or Stay
 # If P option Stay compare sum of D v P 
 # If P sum < 21 && > D sum then P wins!
 # If P sum < D sum then P loses

"""
# player makes a decision stand or hit
while True: 
# to clear the screen
    os.system('clear')
#let's show what cards they players have
    print("Delaer Cards: [][?]".format(dealer[0]))
    print("Your Cards [{}]({})".format("][".join(player), 000000))

    break

# BlackJack or 21 game
import random
# THE PLANNING PHASE
cards = []

 # Dealer cards
dealer_cards = []
 # Player cards
player_cards = []
# Deal the cards
# Display the cards
# Dealer Cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has X &", dealer_cards[1])

# Player Cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have ", player_cards)

 # Sum of the Dealer cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")

# Sum of the Player cards
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit?  "))
    if action_taken == "hit":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
        else:
            print("You win!")
            break

if sum(player_cards) > 21:
    print("You BUSTED! Dealer wins.")
elif sum(player_cards) == 21:
    print("You have BLACKJACK! You Win!! 21")
"""