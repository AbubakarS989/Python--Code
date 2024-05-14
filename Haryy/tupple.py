tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if 342 in tup:
  print("Yes 342 is present in this tuple")

tup2 = tup[1:4]
print(tup2)

details = ("Ahmad", 18, "Ali", 9)
print(details[1])

tup3 = (1, 2, 3, 4, 5, 6, 7, 8, 10, 123)
print(tup3[2:8])
print(tup3[2:8:1])

