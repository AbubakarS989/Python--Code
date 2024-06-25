# Map
# map()
vals=[1,2,3,4]
addition=map(lambda x: x+2,vals)
print(list(addition))

items={"A":1,"B":2,"C":3}
multiple=map(lambda key:items[key]*key,items )
print(list(multiple))
