

import requests
import json,os
from datetime import datetime
from colorama import init, Fore, Back, Style
from  history import History_WT_CWA
from common import HEAD
head=HEAD()
# initialize the colorama module
init()

class Water_Tracker_CWA:
    def __init__(self):
        Pixel_endpoint=""
        Sheety_endpoint=""
            
    def Home_Screen(self):
        #display header  
        head.header(heading=None)
        
        # Getting value from the user
        print("1: Enter Water Track")
        print("2: Show Water History ")
        print("3: Exit ")
        ask=input("Enter your choice:")
        try:
            ask=int(ask)
            if ask==1:
                self.input_screen()
            elif ask==2:
                History_screen=History_WT_CWA()
                History_screen.History()
            elif ask==3:
                print("Closing the program....")
                exit()
            else:
                print("Invalid input ")
        except ValueError as e:
            print("Invalid input ",e)
            

    def input_screen(self):
        
        # displaying header
        head.header(heading="Input Screen")
        print("from input screen")
        self.output_screen()
    
    
    def output_screen(self):
        
        head.header(heading="Output Screen")
        print("from output screen")
        
        


    
   
    
        
        
        
        
        
        
# screen=Water_Tracker_CWA()        
# screen.Home_Screen()
# screen.input_screen()
if __name__=="__main__":
    screen=Water_Tracker_CWA()        
    screen.Home_Screen()
    input("Press Enter to exit.")

    

