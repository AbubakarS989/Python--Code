# Filter
# filter()
# this fuc, filter the function according to the condition and store them as a object
def filter_fun(value):
    return value%2==0

lst=[2,4,5,6,7,8,9,23,5,78,67]
even=filter(filter_fun,lst)
even_2=filter(lambda x:x%2==0,lst)

print(even)  
print(even_2) 
# <filter object at 0x000001B183330730>
# <filter object at 0x000001B183330640>
# this is actually an object, we can iterate through it or convert it into a list

print(list(even))
[2, 4, 6, 8, 78]
print(list(even_2))
[2, 4, 6, 8, 78]