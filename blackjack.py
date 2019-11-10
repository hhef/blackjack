import random
import os


def new_card(hand, deck):
    card = hand.append(deck[0])
    deck.remove(deck[0])


def hand_score(hand):
    score = 0
    non_aces = [card for card in hand if card != "A"]
    aces = [card for card in hand if card == "A"]
    for card in non_aces:
        if card in 'JQK':
            score += 10
        else:
            score += int(card)

    for card in aces:
        if score <= 10:
            score += 11
        else:
            score += 1
    return score


deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
random.shuffle(deck)
dealer_hand = []
player_hand = []

new_card(dealer_hand, deck)
new_card(player_hand, deck)
new_card(dealer_hand, deck)
new_card(player_hand, deck)

standing = False
first_hand = True

while True:
    os.system("cls" if os.name == 'nt' else 'clear')
    if not deck:
        deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

    player_score = hand_score(player_hand)
    dealer_score = hand_score(dealer_hand)
    if standing:
        print(f"Your cards: [{']['.join(dealer_hand)}] - ({dealer_score})")
    else:
        print(f"Dealer cards: [{dealer_hand[0]}][X]")
    print(f"Your cards: [{']['.join(player_hand)}] - ({player_score})")
    print('')

    if standing:
        if dealer_score > 21 or player_score > dealer_score:
            print("You win")
        elif player_score == dealer_score:
            print("It's a tie")
        else:
            print("You lost")

        break
    if first_hand and player_score == 21:
        print("Blackjack! You win")
        break

    first_hand = False

    if player_score > 21:
        print("You lost")
        break

    print("What would you like to do?")
    print("'Hit' if want another card")
    print("'Stand' to stay with your hand")

    print('')
    choice = input("Your choice: ")
    print('')
    if choice.lower() == "hit":
        new_card(player_hand, deck)
    elif choice.lower() == "stand":
        standing = True
        while hand_score(dealer_hand) <= 16:
            new_card(dealer_hand, deck)
