list_fruits = []

# Find Fruit with index
def find_f_name():
    if len(list_fruits) ==0:
        print("You don't have fruits .Please add before finding it.")
    else:
        f_name=input("Enter your fruit name.")
        if f_name in list_fruits:
            print(f"Here is your fruit : {f_name}")
        else:
            print(f"You don't have {f_name} in your bucket list")   
            
# Find Fruit with index
def find_f_index():
    if len(list_fruits) ==0:
        print("You don't have fruits .Please add before finding it.")
    else:
        index=int(input("Enter your fruit order."))
        print(f"Here is your fruit : {list_fruits[index-1]}")
            

# Add Fruits
def add_fruits():
    game_on = True
    while game_on:
        fruits_name = input(f"Enter Fruit name or type 'of' to exit:")
        if fruits_name == "of":
            # list_fruits.remove("of")
            game_on = False
        else:
            list_fruits.append(fruits_name)


#  remove fruits
def remove_fruits():
    if len(list_fruits) ==0 or list_fruits=="of":
        print("You don't have fruits .Please add before removing it.")
    else:
        name=input("Enter name of fruit to remove it:")
        # is_have=list_fruits[name]
        for is_have  in list_fruits:
            if name == is_have:
                list_fruits.remove(name)
                print(f"You'r {name} is remove from the bucket.")
            else:
                print(f"Sorry, you don't have {is_have}")



print_list = True
while print_list:
    user_input = int(
        input(
            "1: Add Fruits\n2: Remove Fruits\n3: Find Fruit with order number\n4: Find fruit with name.\n5: Exit the program \nSelect Your Option:"
        )
    )
    if user_input == 1:
        add_fruits()
    elif user_input == 2:
        remove_fruits()
    elif user_input==3:
        find_f_index()
    elif user_input==4:
        find_f_name()
    elif user_input == 5:
        print_list = False


# # for name in list_fruits:
# #     print(name)

# # i=0
# # while True:
# #     i+=1
# #     print("Hi",i)
# #     if i==102:
# #         continue
# for i in range(1,100):
#     # i=+1
#     print("helo",i)
#     if i ==4:
#         print("hi",i)
#         continue
#         print("dbfjdbs")
