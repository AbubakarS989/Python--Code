import pandas
# TODO Description
# NATO Alphabet project
# A name : ANGE
# A for Alfa
# N for November
# G for Grass
# E for Environment

#Just like above, we are going to find related word of each letter  of a given word


# Step1: Getting data from the file
data=pandas.read_csv(r"Projects\Nato Alphabet\nato_phonetic_alphabet.csv")

# Step2: Create new dic to store data as key value pairs
dict_data={}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# code 
# Dictionary Comprehensive
# dict_dta={row.letter:row.code for (index,row) in data.iterrows()}
# print(dict_dta)


# My idea
# Keyword Method with iterrows()

for (index, row) in data.iterrows():
    # append data  key value pairs in dictionary
    # print(index 
    dict_data[row.letter]=row.code
# print(dict_data)

# print(dict_data[0][0])



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.



# list Comprehensive
user=input("Enter your name:\n")
# name_list=[dict_dta[letter.upper()] for letter in user]
# print(name_list)


# my idea
name_list=[letter.upper() for letter in user]
answer=[]
for key in dict_data.keys():
    if key in name_list:
        answer.append(dict_data[key])
print(answer)






