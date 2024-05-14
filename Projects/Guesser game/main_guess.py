import random
import os
import logo
import time
def clear_console():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def guess():
    computer_guess = random.randint(1, 100)
    return computer_guess

def user_guess():
    number = int(input("Make a guess: \n"))
    return number





def easy():
    attempts = 10
    print(f"You've got {attempts} attempts")
    cmp_num = guess()
    while attempts != 0:
        user_num = user_guess() 

        # this var store value minus to the user score
        #  this use for print particular statement if user V les than 5 and belongs to that area
        less_range=cmp_num-user_num
        high_range=user_num-cmp_num
        if less_range>=1 and less_range<5  and not attempts==0:
            print("You are just about reach to your guess")
        elif high_range>=1 and high_range  and not attempts==0<5:
            print("You are little higher to your guess")
        else:
            if user_num not in range(1, 101):
                print("Try again. Enter a correct number.")
                continue  # Continue without decrementing attempts for an invalid guess.
            elif user_num == cmp_num:
                print(logo.logo_win)
                break
            elif user_num > cmp_num and not cmp_num-user_num==5  and not attempts==0 and not user_num-cmp_num==5 or not less_range or not high_range:
                # print(cmp_num)
                print("Try again, your guess is too high.")
            elif user_num < cmp_num and  not cmp_num-user_num==5  and not attempts==0 and not user_num-cmp_num==5 or not less_range or not high_range :
                # print(cmp_num)
                print("Try again, your guess is too low.")
            
        attempts -= 1
        if user_num < cmp_num and cmp_num-user_num==5  and not attempts==0:
            print("You are closer to your guess")
        elif user_num > cmp_num and  user_num-cmp_num==5  and not attempts==0:
            print("You are little bit higher to your guess")
        elif attempts !=0 :
            print(f"You have {attempts} attempts remaining to guess the number")
        elif attempts==5:
            print("Wait please..")
            time.sleep(8)
            clear_console()
            print(f"You have {attempts} attempts remaining to guess the number")
        elif attempts == 0:
            print(logo.logo_over)
            print("Out of attempts. The number was:", cmp_num)
         
    



def difficult():
    attempts = 5
    cmp_num = guess()
    print(f"You've got {attempts} attempts")
    while attempts != 0:

        user_num = user_guess() 
          # this var store value minus to the user score
        #  this use for print particular statement if user V les than 5 and belongs to that area
        less_range=cmp_num-user_num
        high_range=user_num-cmp_num
        attempts -= 1
        if less_range>=1 and less_range<5  and not attempts==0:
            print("You are just about reach to your guess")
            # print(f"You have {attempts} attempts remaining to guess the number")
        elif high_range>=1 and high_range<5  and not attempts==0:
            print("You are little higher to your guess")
            # print(f"You have {attempts} attempts remaining to guess the number")
        else:
            if user_num not in range(1, 101):
                print("Try again. Enter a correct number.")
                continue  # Continue without decrementing attempts for an invalid guess.
            elif user_num == cmp_num:
                print(logo.logo_win)
                break
            elif user_num > cmp_num and not attempts==0 and not cmp_num-user_num==5 and not user_num-cmp_num==5 or not less_range or not high_range:
                # print(cmp_num)
                print("Try again, your guess is too high.")
            elif user_num < cmp_num and not attempts==0 and  not cmp_num-user_num==5 and not user_num-cmp_num==5 or not less_range or not high_range :
                # print(cmp_num)
                print("Try again, your guess is too low.")
            
        if user_num < cmp_num and cmp_num-user_num==5  and not attempts==0:
            print("You are closer to your guess")
            print(f"You have {attempts} attempts remaining to guess the number")
        elif user_num > cmp_num and  user_num-cmp_num==5  and not attempts==0:
            print("You are little bit higher to your guess")
            print(f"You have {attempts} attempts remaining to guess the number")
        elif attempts !=0 :
            print(f"You have {attempts} attempts remaining to guess the number")
        elif attempts == 0:
            print(logo.logo_over)
            print("Out of attempts. The number was:", cmp_num)
        



#  Printing Start from here
def play_game():
    again_run = True
    while again_run:
        game_run = True
        clear_console()
        print(logo.logo_welcome)
        while game_run:
            print("Welcome to the number guessing Game in Python")
            print("I'm thinking of a number between 1 and 100.")
            choice = input("Select Difficulty: Type 'easy' or 'hard': ").lower()
            if choice == "easy":
                easy()
            elif choice == "hard":
                difficult()
            else:
                clear_console()
                print("Try again. Enter a correct difficulty.")
                time.sleep(3)

            # Ask the user if they want to play again after each round
            choice = input("Type 'p' to re-play your game or 's' to stop your game ").lower()
            if choice == "s" and game_run:
                again_run = False  # Set again_run to False to exit the outer loop and stop the game
                game_run = False  # Set game_run to False to exit the inner loop and stop the current round
                clear_console()
                print(logo.logo_bye)
                print("Thanks for playing! Goodbye.")
            elif choice == 'p' and game_run:
                clear_console()
                break  # Exit the inner loop and restart the game

# Call play_game() to start the game
play_game()
