

import pandas
data=pandas.read_csv(r"Projects\Nato Alphabet\nato_phonetic_alphabet.csv")
dict_data={}
dict_dta={row.letter:row.code for (index,row) in data.iterrows()}
print(dict_dta)



user=input("Enter your name:\n")
name_list=[dict_dta[letter.upper()] for letter in user]
print(name_list)

