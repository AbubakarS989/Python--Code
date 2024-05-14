PlaceHolder="[name]"


with open("Projects\Mail Merge Project\main.txt","r") as names:
    # print data in a type of list
    name=names.readlines()

# print(name)

with open("Projects\Mail Merge Project\letter.txt","r") as letter:
    # read the entire file
    letter_content=letter.read()
    # we get through a list 
    for identity in name:
        # find [name] in the letter file  and replace that to name of each person
        # \n is remove here using strip()
        strip_name=identity.strip()
        # replace(), replace the content present in (Place holder ) and change that (Place holder) content with strip content
        new_letter=letter_content.replace(PlaceHolder,strip_name)
        print(new_letter)
        with open(f"Projects\Mail Merge Project\letter_to_{strip_name}.txt","w") as complete_letter:
            complete_letter.write(new_letter)

    
    # print(new_letter.strip())



# txt="i hlo"
# txt=  txt.replace("hlo","hi")
# print(line,txt)

