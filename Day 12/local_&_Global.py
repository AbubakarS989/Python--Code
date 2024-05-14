# Scope of variable

number = 1


def check():
    number = 2
    print(f"Inside number is {number}")


check()
print(f"outside number is {number}")


# number variable is global Vr , that we can access anywhere in the program
# Local Scope


def sum_num():
    result = 3 + 5
    print(result)


# print(result)
# We can't access inside declare variable outside the function
# those are local variables


# Block scope


score = 33
if 4 > 3:
    new_score = 34
    print(new_score)

# print(new_score)
# we can use var outside if ,while , block that assign in them


# but if we add that block of code in the fun then we can't use the var outside the fun


def player_score():
    if 4 > 3:
        score_add = 30
        print(score_add)


# print(score_add)
# this print an error bec we used var outside the fun
