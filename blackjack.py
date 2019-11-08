import random
import os


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


deck = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
]

random.shuffle(deck)

dealer_hand = []
player_hand = []

dealer_hand.append(deck.pop())  # zmienić bo on zabiera element z lity i oddaje go znowu ale trzeba zakonczyc talie kart
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())

standing = False
first_hand = True

while True:
    os.system("cls" if os.name == 'nt' else 'clear')

    player_score = hand_score(player_hand)
    dealer_score = hand_score(dealer_hand)
    if standing:
        print(f"Your cards: [{']['.join(dealer_hand)}] - ({dealer_score})")
    else:
        print(f"Dealer cards: [{dealer_hand[0]}][X]")
    print(f"Your cards: [{']['.join(player_hand)}] - ({player_score})")
    print('')

    if standing:
        if dealer_score > 21:
            print("You win")
        elif player_score == dealer_score:
            print("It's a tie")
        elif player_score > dealer_score:
            print("You win")
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
        player_hand.append(deck.pop())
    elif choice.lower() == "stand":
        standing = True
        while hand_score(dealer_hand) <= 16:
            dealer_hand.append(deck.pop())
