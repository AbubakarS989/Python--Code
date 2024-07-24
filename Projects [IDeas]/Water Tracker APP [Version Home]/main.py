

import requests
import json,os
from datetime import datetime
from colorama import init, Fore, Back, Style
from  history import History_WT_CWA
# initialize the colorama module
init()

class Water_Tracker_CWA:
    def __init__(self):
        Pixel_endpoint=""
        Sheety_endpoint=""
    
    def Home_Screen(self):
        
        print("----------------------------------------------")
        print("-------------  Water Tracker [Home] ----------")
        print("----------------------------------------------")
        print("-------------  Code With Abubakar   ----------")
        print("----------------------------------------------\n")
        
    
        print("1: Enter Water Track")
        print("2: Show Water History ")
        print("3: Exit ")
        ask=int(input("Enter your choice:"))
        try:
            if ask==1:
                self.input_screen()
            elif ask==2:
                History_screen=History_WT_CWA()
                History_screen.History()
            elif ask==3:
                print("Closing the program....")
                exit()
        except ValueError as e:
            print("Invalid input ",e)
    
            
                
            
               
       
    def input_screen(self):
        pass         
        
        
        

        
        
        
        
        
        
        
screen=Water_Tracker_CWA()        
screen.Home_Screen()
        
        
    
    

        



















