import random
from hangmanart import logo4
import os

def deal_card():
    """Choose a random card from cards."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    
    if sum(cards)==21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_cards(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
      return "You went over. You lose "
    
    if user_score == computer_score :
        return "Draw"
    elif computer_score == 0:
        return "You lose, Computer has blackjack!!!!"
    elif user_score == 0:
        return "You win with a blackjack..."
    elif user_score>21:
        return "You went over, You lose"
    elif computer_score>21:
        return "Computer went over, You win!!"
    elif user_score>computer_score:
        return "You win!!!"
    else:
        return "You lose.."

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def blackjack():
    print(logo4)
    
    user_cards = []
    computer_cards = []
    game_continues = True

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while game_continues:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"User cards : {user_cards} , User score : {user_score}")
        print(f"Computer card : {computer_cards[0]}")

        if computer_score == 21 or user_score == 21 or user_score > 21:
            game_continues = False
        else:
            hit_or_deal = input("Enter 'y' to add another card or enter 'n' to end the game.")
            if hit_or_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_continues = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"Your cards : {user_cards} and Yoyr core : {user_score}")
    print(f"computer final cards : {computer_cards} and Computer's hand : {computer_score}")
    print(compare_cards(user_score,computer_score))

continuty = True

while continuty:
    direction = input("Do you want to play Blackjack game? Enter 'y' or 'n'.")
    
    if direction == 'y':
        os.system('cls')
        blackjack()
    else: 
        continuty = False