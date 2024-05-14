from game_data import data
from art import logo ,vs as Compare
import random,os

def clear_console():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def persons(data):
    per_name=data['name']
    per_des=data['description']
    per_country=data['country']
    return f"{per_name} is a {per_des} from {per_country} "



def play_game():
    print(logo)
    score=0
    game_run = True
    person1 =get_random_account()
    person2 = get_random_account()
    while game_run:
        while person2 == person1:
            person1 = get_random_account()

        print(f"Compare : {persons(person1)}")
        # print(persons(person1))
        print(Compare)
        print(f"Against: {persons(person2)}")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        follower1 = person1['follower_count']
        follower2 = person2['follower_count']
        # print(follower1)
        # print(follower2)
       
    #     clear console and print game logo 
    #    checking the number
        clear_console()
        print(logo)

        if choice == 'a':
            if follower1 > follower2: 
                score+=1
                correct=1
                print(f"You're right! Current score: {score}.")
            
            else:
                print(f"You're wrong! Final score: {score}.")
                game_run=False  
        elif choice == 'b':
            if follower2 > follower1:
                correct=2
                score+=1
                print(f"You're right! Current score: {score}.")
                
            else:
                print(f"You're wrong! Final score: {score}.")
                game_run=False  

        else:
            print(f"You're wrong! Final score: {score}.")
            game_run=False  

        #  here we swipe that person if the one of the a guess is correct
        if game_run==True:
            if correct ==1:
                person1=person1
                person2=get_random_account()
            elif correct==2:   
                person1=person2     
                person2=get_random_account()      
        else:
            break

        # import time
        # time.sleep(5)

    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again == "yes":
        clear_console()
        play_game()
    elif play_again=='no':
        print("Thanks for playing! Goodbye.")

clear_console()
play_game()



# for da in data:
#     print(f"{da}\n")

# for I in range(len(data)):
#     print(data[I]["follower_count"])
#     print(data[I]["description"])
#     print(data[I]["country"])
#     print("\n")



# print(len(data))
# print(type(data[1]['follower_count']))

# print(random_a)


