from art_Blackjack import logo
import random
import os
def clear_console():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def compare(user_score, computer_score):
    if user_score==computer_score:
        return "It's a Draw"
    elif computer_score ==0:
        return "Loose , opponent has Blackjack"
    elif user_score==0:
        return "Win with a Blackjack"
    elif user_score>21:
        return "You went over, you lose"
    elif computer_score>21:
        return " Opponent went over, you win"
    elif user_score>computer_score:
        return "You win"
    else :
        return "You lose"    


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def play_game():
    print(logo)
    user_card = []
    computer_card = []
    is_game_over = False
    for _ in range(2):
        user_card.append(deal_card())

    for _ in range(2):
        computer_card.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass.")
            if user_should_deal=="y":
                # here we add another card in user card
                user_card.append(deal_card())
            else:
                is_game_over=True
    while computer_score != 0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)

    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear_console()
    play_game()