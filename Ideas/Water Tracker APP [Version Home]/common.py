from colorama import init, Fore, Back,Style

class HEAD:
    def __init__(self):
        self.heading = ""
        
    def header(self, heading=None):  
        if not heading:
            print("------------------------------------------------------")
            print(f"-------------  {Fore.LIGHTYELLOW_EX}Water Tracker [Home Version]{Style.RESET_ALL} ----------")
            print(f"------------------------------------------------------")
            print(f"-------------    {Fore.MAGENTA}Code With Abubakar{Style.RESET_ALL}   ----------------")
            print("-----------------------------------------------------\n")
        else:
            print("------------------------------------------------------")
            print(f"-------------  {Fore.LIGHTYELLOW_EX}Water Tracker [Home Version]{Style.RESET_ALL} ----------")
            print(f"------------       {Fore.LIGHTCYAN_EX}{heading}{Style.RESET_ALL}         -------------")
            print(f"-------------    {Fore.MAGENTA}Code With Abubakar{Style.RESET_ALL}   ----------------")
            print("------------------------------------------------------\n")
