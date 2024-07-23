from colorama import Fore, Back, Style, init

# Initialize colorama
init()

# Print colored text
print(Fore.RED + 'This is red text')
print(Fore.GREEN + 'This is green text')
print(Back.YELLOW + 'This is text with yellow background')
print(Style.BRIGHT + 'This is bright text')
print(Style.RESET_ALL + 'Back to normal text')

txt="Success. Let's visit https://pixe.la/@yourusername , it is your profile page!"

sentence=txt.split(". ")
print(sentence[1])
print(f"\t\t :> {Fore.GREEN}{sentence[1]}{Style.RESET_ALL}")