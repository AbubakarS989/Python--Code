
def formate(statement): 
# make first letter uppercase of each word
    print(statement.title())
    print(statement.upper())
    low=print(statement.lower())
    return  f"{low}"
    return  f"{low}"
    # return print("hey")
statement=input("Enter your statement: ")
formate(statement)



#  count length of given statement and don't count the spaces btw them.
# without using length function.
def length_count(length_given):
    count=0
    for i in length_given:
        if ' 'in i:
            count-=1 
        count+=1
        # print(i)
    length_is=count
    print(f"Your statement length is :{length_is}")

length_given=input("Enter your statement to calculate your length:")
length_count(length_given)




def check_string(given_statement):
    '''check user write something or not        '''
    if given_statement=="":
        return print("Empty string")

    return print("Something is written in the string.")


check_string(input("Enter ur statement: "))