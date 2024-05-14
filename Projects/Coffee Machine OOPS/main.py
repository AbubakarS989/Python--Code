# from resources import MENU , resources as source
from Coffee_maker import CoffeeMaker
from Money_Machine import MoneyMachine
from menu import Menu


#  creating class of money machine
class Money_machine():
    pass





money_machine=MoneyMachine()
coffee_make=CoffeeMaker()
menu=Menu()


is_on=True
while is_on:
    options=menu.get_items()
    choice=input(f"What would you like {options}") 
    if choice=="off":
        is_on=False
    elif choice=="report":
        money_machine.report()
        coffee_make.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_make.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_make.make_coffee(drink)

# money_machine=Money_Machine()