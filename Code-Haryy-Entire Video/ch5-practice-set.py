
#!    CHAPTER 5 – PRACTICE SET
#TODO 1. Write a program to create a dictionary of English words with values as their urdu translation. Provide user with an option to look it up!

urdu_dic={
    "chair":"kursi",
    "door":"Darwaza",
    "tree":"Darakht",
    "electricity":"Bijlii"
}

value=input("-- Welcome to Urdu Dictionary --\nEnter word to get their urdu translation: ")
print(urdu_dic[value.lower()])

#TODO 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
# sets=set()
# v1=int(input("Enter number 1:"))
# sets.add(v1)
# v2=int(input("Enter number 2:"))
# sets.add(v2)
# v3=int(input("Enter number 3:"))
# sets.add(v3)
# v4=int(input("Enter number 4:"))
# sets.add(v4)
# v5=int(input("Enter number 5:"))
# sets.add(v5)
# v6=int(input("Enter number 6:"))
# sets.add(v6)
# v7=int(input("Enter number 7:"))
# sets.add(v7)
# v8=int(input("Enter number 8:"))
# sets.add(v8)
# print(sets)


#TODO 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
sets=set()
sets.add(18)
sets.add("18")
print(sets)
#TODO 4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(s)
print(len(s))
#TODO 5.  What is the type of 's'?
s = {}
print(type(s))
#TODO 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
frd_dict={}
n1,f1=input("Enter your name:\n"),input("Enter your fav lan:")
frd_dict[n1]=f1
n1,f1=input("Enter your name:\n"),input("Enter your fav lan:")
frd_dict[n1]=f1
n1,f1=input("Enter your name:\n"),input("Enter your fav lan:")
frd_dict[n1]=f1
n1,f1=input("Enter your name:\n"),input("Enter your fav lan:")
frd_dict.update({n1:f1})
print(frd_dict)
#TODO 7. If the names of 2 friends are same; what will happen to the program in problem 6?
# the value of next duplicate key is assigned to the previous same key
#TODO 8. If languages of two friends are same; what will happen to the program in problem 6?
# in this case, no effect is on key if any of them to store as same.
#TODO 9. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}

#? no we can't change the list item in set as sets are immutable[can't change after define ]
#?  we can't insert list in set data type as list are mutable and sets are immutable, the result will be in error.   
# for i in s:
#     print(i)


#? but we can add tuple in sets, because tuples are immutable , now both structure have the same data type
s = {8, 7, 12, "Harry", (1,2)}
print(type(s))
