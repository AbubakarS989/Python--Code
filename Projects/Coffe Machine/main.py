#  Here we create a coffee machine
import os
from resources import MENU, resources



profit = 0


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def process_coins():
    '''' Returns the total amount of inserted money by the user '''
    print("Please insert coins:")
    total=int(input("How many quarters : "))*0.25
    total+=int(input("How many dimes : "))*0.1
    total+=int(input("How many nickles : "))*0.05
    total+=int(input("How many pennies : "))*0.01
    return total




def is_resource_sufficient(oder_ingredients):
    '''Return the True if resources are enough to make a coffee
        otherwise it return False  '''
    # is_enough=True
    
    for item in oder_ingredients:
        if oder_ingredients[item] >= resources[item]:
            print(f"Sorry there is  not enough {item }")            
            return False    
    return True


def is_transaction_Successful(money_received ,cost_of_drink):
    ''' Return True if money is accepted, or Return False if money is not sufficient'''
    if money_received>=cost_of_drink:
        change=round(money_received-cost_of_drink,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=cost_of_drink
        return True
    # if money_received !=0:
    #     print("Transaction Successful")
    #     return True
    else:   
        print("Sorry, that's not enough money. Money is refunded.")
        return False


def make_a_coffee(drink_name,oder_ingredients):
    ''' Deduct the required ingredients from the resources'''
    for item in oder_ingredients:
        resources[item]-= oder_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy it !"    )


run_game = True
while run_game:
    # clear_console()
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    # print(MENU[user_choice])
    # print(resources)

    if user_choice == "off":
        run_game = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif user_choice !='off' and user_choice !='report' and user_choice not in MENU:
        print("Chose right option.") 
        break
    else:
        drink = MENU[user_choice]
        # print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_Successful(payment,drink['cost']):
                make_a_coffee(user_choice,drink["ingredients"])
              