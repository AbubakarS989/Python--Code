from game_data import data
from art import logo ,vs as Compare
import random
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



def play_game():
    game_run = True
    current_score = 0
    print(logo)
    while game_run:
        i=random.choice(data)
        b=random.choice(data)
        # i, b = random.sample(range(len(data)), 2)
        if i==b:
           i=random.choice(data)

        print(f"Compare A: {i['name']} is a {i['description']} from {i['country']}")
        print(Compare)
        print(f"Against: {b['name']} is a {b['description']} from {b['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        follower1=i['follower_count']
        follower2=b['follower_count']
       
        # print(follower1)
        # print(follower2)
        if choice == 'a':
            if follower1 > follower2: 
                current_score += 1
                print(f"You're right! Current score: {current_score}.")
            if follower2 > follower1:
                current_score += 1
                print(f"You're right! Current score: {current_score}.")
        elif choice == 'b':
            if follower1 > follower2:
                current_score += 1
                print(f"You're right! Current score: {current_score}.")
            if follower2 > follower1:
                current_score += 1
                print(f"You're right! Current score: {current_score}.")

        else:
            game_run = False
            print(f"You're wrong! Final score: {current_score}.")

    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again != "yes":
        play_again()
    else:
        print("Thanks for playing! Goodbye.")

play_game()



# for A in range(1,50):
#     CompareA=data[A]['follower_count']
#     print(CompareA)
#     # i+=1