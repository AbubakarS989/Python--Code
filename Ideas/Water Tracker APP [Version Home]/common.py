class HEAD:
    def __init__(self):
        self.heading = ""
        
    def header(self, heading=None):  
        if not heading:
            print("------------------------------------------------------")
            print("-------------  Water Tracker [Home Version] ----------")
            print(f"------------------------------------------------------")
            print("-------------    Code With Abubakar   ----------------")
            print("-----------------------------------------------------\n")
        else:
            print("------------------------------------------------------")
            print("-------------  Water Tracker [Home Version] ----------")
            print(f"------------       {heading}         -------------")
            print("-------------    Code With Abubakar   ----------------")
            print("------------------------------------------------------\n")
