from colorama import Fore, Back, Style, init

# Initialize colorama
init()

# Print colored text
print(Fore.RED + 'This is red text')
print(Fore.YELLOW + 'This is yelo text')
print(Fore.GREEN + 'This is green text')
print(Fore.LIGHTBLUE_EX + 'This is light blue text')
print(Fore.LIGHTCYAN_EX + 'This is light cyan text')
print(Fore.LIGHTRED_EX + 'This is light red text')
print(Fore.LIGHTYELLOW_EX + 'This is light yellow text')
print(Fore.MAGENTA + 'This is  magenda text')
print(Fore.LIGHTBLACK_EX+ 'This is  light blacck text')
# print(Fore.+ 'This is  light blacck text')
print(Back.YELLOW + 'This is text with yellow background')
print(Style.BRIGHT + 'This is bright text')
print(Style.RESET_ALL + 'Back to normal text')

txt="Success. Let's visit https://pixe.la/@yourusername , it is your profile page!"

sentence=txt.split(". ")
print(sentence[1])
print(f"\t\t :> {Fore.GREEN}{sentence[1]}{Style.RESET_ALL}")

print(f"{Fore.MAGENTA}Code with Abubakar{Style.RESET_ALL}")