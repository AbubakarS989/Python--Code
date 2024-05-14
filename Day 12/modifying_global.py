#  modifying global variable

user_score=23

# def score():
# global user_score  this create global vr into local
#     user_score=34
#     print(user_score)


# score()
# print(user_score)

def score():
#    print( user_score+12)
    return user_score+12


user_score=score()
print(user_score) # answer is 35 instead of 23



# Global Constant
#  for making constant use Upper case Vr name
PI=3.14159
print(PI)

