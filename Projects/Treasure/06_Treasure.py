import time
import os
from left_path import fun_left_path

#  Here we create a function that clear the console ,when user passes the each level

def clear_console():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


#  welcome window

def welcome_win():
    clear_console()
    print("-------------------------------------------------------------------")
    print("                  Welcome to the python Treasure Game. ")
    print("-------------------------------------------------------------------")
    print("Your today's task is to find a treasure that's buried somewhere on land.")
    print("Now, you are on the road, and you have two paths to start your journey:\nLeft 'L' and Right 'R'.")



#  Here we call our all functions
welcome_win()
fun_left_path()

































































# if path == "l":
#     value = 0
#     print("You are on your way to your destination...")
#     time.sleep(5)
#     print("-------------------------------------------------------------------")
#     print(f" Location: Lahore                                    Score:{value}")
#     print("-------------------------------------------------------------------")
#     print("You chose the left path to start your journey.\nYou have reached Lahore.")
#     print("Which way would you like to travel further?")
#     print("-------------------------------------------------------------------\n")
#     print("1: An old tunnel that has been closed for years.")
#     print("2: A bridge that is under construction.")
#     print("3: A sea that is filled with polluted water.")
#     print("-------------------------------------------------------------------")

#     # Level 1 choice starts here
#     level_1 = int(input("Enter number to choose one of them: "))

#     if level_1 == 1:
#         print("You are on your way to your destination...")
#         time.sleep(5)
#         clear_console()
#         print("\n-------------------------------------------------------------------")
#         print(f"Location: Lahore Tunnel                                Score:{value}")
#         print("---------------------------------------------------------------------")
#         print("\n\n         Oops! You died due to encountering snakes in the tunnel.")
#         print("         The tunnel has been closed for a long time.")
#         print("                       GAME OVER !!\n\n")
#         print(f"                      Your Prize is ${value}")
#         print("-------------------------------------------------------------------")
#         print("                You should try again to test your luck!")
#         print("                 Thanks for playing. Wish you a great day!")
#         print("-------------------------------------------------------------------")
#     elif level_1 == 2:
#         print("You are on your way to your destination...")
#         time.sleep(5)
#         clear_console()
#         print("-------------------------------------------------------------------")
#         print(f"Location: Lahore Bridge                              Score:{value}")
#         print("-------------------------------------------------------------------")
#         print("\n\n         Oops! You died due to the collapse of the bridge.")
#         print("         The bridge was blasted by the constructors to rebuild it.")
#         print("                       GAME OVER !!\n\n")
#         print(f"                    Your Winning Prize is ${value}")
#         print("-------------------------------------------------------------------")
#         print("                You should try again to test your luck!")
#         print("                 Thanks for playing. Wish you a great day!")
#         print("-------------------------------------------------------------------")
#     elif level_1 == 3:
#         print("You are on your way to your destination...")
#         time.sleep(5)        
#         value = 20000
#         clear_console()
#         print("\n\n---------------------------------------------------------------------")
#         print(f"Location: Inside City                                    Score:{value}")
#         print("-----------------------------------------------------------------------")
#         print("\n            Congratulations! You have passed the first level.")
#         print("                   Now, you have reached inside the city.")
#         print("\nWhich way would you like to travel further?")
#         print("-------------------------------------------------------------------")
#         print("1: A road , which is very slippery")
#         print("2: By Bicycle, riding through a mudded road.")
#         print("3: By Airplane, that passes through stormy weather.")
#         print("-------------------------------------------------------------------")
#         # Level 2 starts here
#         level_2 = int(input("Enter number to choose one of them: "))
#         if level_2 == 1:
#             print("You are on your way to your destination...")
#             time.sleep(5)
#             clear_console()        
#             print("\n\n-------------------------------------------------------------------")
#             print(f"Location: Inside City on road                            Score:{value}")
#             print("-----------------------------------------------------------------------")
#             print("\n\n            Oops! You died due to a road accident.")
#             print("       The road was slippery,  your car collided with a truck.\n")
#             print("                         GAME OVER !!\n")
#             print("-------------------------------------------------------------------")
#             print(f"                    Your Winning Prize is ${value}")
#             print("                You should try again to test your luck!")
#             print("                Thanks for playing. Wish you a great day!")
#             print("-------------------------------------------------------------------")
#         elif level_2 ==2:
#             print("You are on your way to your destination...")
#             time.sleep(5)        
#             clear_console()
#             value +=20000
#             print("\n\n---------------------------------------------------------------------")
#             print(f"Location: Village                                        Score:{value}")
#             print("-----------------------------------------------------------------------")
#             print("\n            Congratulations! You have passed the second level.")
#             print("                   Now, you have reached the village ")
#             print("\nWhich way would you like to travel further?")
#             print("-------------------------------------------------------------------")
#             print("1: A town filled with hunting dogs, their barks echoing throughout,\n   making their presence felt everywhere.")
#             print("2: Picture an apartment nestled beneath the surface, hidden from \n   view, with a convenient pathway leading to the outside world.")
#             print("3: Visualize a cavern, its entrance beckoning individuals to     \n   venture inside and discover its mysteries.  ")
#             print("-------------------------------------------------------------------")
#             # Level 3 starts here
#             level_3= int(input("Enter number to choose one of them: "))
#             if level_3==1:
#                 print("You are on your way to your destination...")
#                 time.sleep(5) 
#                 clear_console()
#                 value +=20000
#                 print("\n\n----------------------------------------------------------------------")
#                 print(f"Location: Island                                         Score:{value}")
#                 print("-----------------------------------------------------------------------")
#                 print("\n            Congratulations! You have passed the third level.")
#                 print("                   Now, you have reached the village ")
#                 print("\nWhich way would you like to travel further?")
#                 print("-------------------------------------------------------------------")
#                 print("1: Cave 1 , A Fight for Survival")
#                 print("2: Cave 2 , A Struggle for Escape")
#                 print("3: Cave 3 , that takes  you to an  forest ")
#                 print("-------------------------------------------------------------------")
#                 # Level 4 starts here
#                 level_4= int(input("Enter number to choose one of them: "))
#                 if level_4==1:
#                     print("You are on your way to your destination...")
#                     time.sleep(5)
#                     clear_console()
#                     print("\n\n-------------------------------------------------------------------")
#                     print(f"Location:A Fight for Survival                            Score:{value}")
#                     print("-----------------------------------------------------------------------")
#                     print("\n\nOops! You tragically lost your life in a relentless attack by a Reptiles")
#                     print(''' Within the depths of the foreboding cave, you  encountered a swarm of deadly
# reptiles. Overwhelmed by their relentless assault, you succumbed
# to their venomous strikes,and died there.\n ''')
#                     print("                          GAME OVER!!\n")
#                     print(f"                Your Winning Prize is ${value}\n")
#                     print("-------------------------------------------------------------------")
#                     print("                You should try again to test your luck!")
#                     print("                Thanks for playing. Wish you a great day!")
#                     print("-------------------------------------------------------------------")
#                 elif level_4==2:
#                     print("You are on your way to your destination...")
#                     time.sleep(10)
#                     clear_console()
#                     print("\n\n-------------------------------------------------------------------")
#                     print(f"Location: Treasure                                       Score:{value}")
#                     print("-----------------------------------------------------------------------")
#                     print("                     Congratulations!!\n")
#                     print("\n          You have finally reached your destination!\n          You have discovered a hidden treasure!")
                   
#                     print("\n")
#                     while True:
#                         user_input = input("Press Enter to see your Treasure or 'q' to quit: ")
#                         time.sleep(5)
#                         clear_console()
#                         if user_input == "":
#                             print("Continuing program execution...")
#                             print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
#                             value+=20000
#                             winning=1000000
#                             total=1000000+value
#                             # Add your code here for the desired actions to be performed
#                             print(f"             Your Bonus Amount   : ${value}")
#                             print(f"             Your Winning Amount : ${winning}")
#                             print(f"             Your Total Amount   : ${total}")
#                             print(f"      Treasure Amount: Ten Lakh and Eighty Thousands\n")
#                             print("-------------------------------------------------------------------")
#                             print("              Thank you for playing. Wishing you a great day!")  
#                             print("-------------------------------------------------------------------")
#                             break
#                         elif user_input.lower() == "q":
#                             print("Quitting program...")
#                             break
#                         else:
#                             print("Invalid input. Please try again.")
#                 elif level_4==3:
#                     print("You are on your way to your destination...")
#                     time.sleep(5)
#                     clear_console()
#                     print("\n\n-------------------------------------------------------------------")
#                     print(f"Location:Forest                                          Score:{value}")
#                     print("-----------------------------------------------------------------------")
#                     print("\n\n Oops! Your life was tragically  finished  by a fierce lion attack.")
#                     print('''As you venture deep into the untamed forest , a sudden encounter with
# a pride of hungry lions brought a swift and tragic end to your journey.\n''')
#                     print("                         GAME OVER !!\n")
#                     print(f"                Your Winning Prize is ${value}\n")
#                     print("-------------------------------------------------------------------")
#                     print("                You should try again to test your luck!")
#                     print("                Thanks for playing. Wish you a great day!")
#                     print("-------------------------------------------------------------------")
#                 else:    
#                         print("Invalid path. Please select a valid option.")
            
#             elif level_3==2:
#                 print("You are on your way to your destination...")
#                 time.sleep(5)
#                 clear_console()
#                 print("\n\n-------------------------------------------------------------------")
#                 print(f"Location: Village in the Underground Apartment           Score:{value}")
#                 print("-----------------------------------------------------------------------")
#                 print("\n\nOops! You  died  due to  tragically claimed by an electric short circuit.")
#                 print('''Unaware of the hidden peril, you entered the secluded underground apartment.
# Little  you know, the pathway you followed led you to room where fire is 
# burning , where you met you untimely demise, forever consumed by the depths.\n''')
#                 print("                         GAME OVER !!\n")
#                 print(f"                Your Winning Prize is ${value}\n")
#                 print("-------------------------------------------------------------------")
#                 print("                You should try again to test your luck!")
#                 print("                Thanks for playing. Wish you a great day!")
#                 print("-------------------------------------------------------------------")
#             elif level_3==3:
#                 print("You are on your way to your destination...")
#                 time.sleep(5)
#                 clear_console()
#                 print("\n\n-------------------------------------------------------------------")
#                 print(f"Location: Village in the Creepy Cave                     Score:{value}")
#                 print("-----------------------------------------------------------------------")
#                 print("\n\nOops! Your life was tragically lost in a cave explosion.")
#                 print('''Unaware of the impending peril, you courageously ventured into the 
# captivating cave. Suddenly, a mighty blast reverberated through the 
# tunnels, triggering the catastrophic collapse of the cave, tragically
# ending your life beneath  the weight of the rubble.\n''')
#                 print("                         GAME OVER !!\n")
#                 print(f"                Your Winning Prize is ${value}\n")
#                 print("-------------------------------------------------------------------")
#                 print("                You should try again to test your luck!")
#                 print("                Thanks for playing. Wish you a great day!")
#                 print("-------------------------------------------------------------------")
#             else:    
#                 print("Invalid path. Please select a valid option.")

#         elif level_2==3:
#             print("You are on your way to your destination...")
#             time.sleep(5)
#             clear_console()     
#             print("\n\n-------------------------------------------------------------------")
#             print(f"Location: Inside City in the Airplane                    Score:{value}")
#             print("-----------------------------------------------------------------------")
#             print("\n\n            Oops! You died due to a faulty engine.")
#             print("       Airplane became unstable and a flash hit the engine\n")
#             print("                         GAME OVER !!\n")
#             print(f"                Your Winning Prize is ${value}\n")
#             print("-------------------------------------------------------------------")
#             print("                You should try again to test your luck!")
#             print("                Thanks for playing. Wish you a great day!")
#             print("-------------------------------------------------------------------")
#         else:
#             print("Invalid path. Please select a valid option.")
            

