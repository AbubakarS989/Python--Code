import requests
import json, os
from datetime import datetime
from colorama import init, Fore, Back, Style
from common import HEAD 

init()
# initialize the colorama module

class History_WT_CWA:
    def __init__(self):
        self.Pixel_endpoint = ""
        self.Sheety_endpoint = ""
    
    def History(self):
        head = HEAD()
        head.header(heading="History Screen")  
     
if __name__ == "__main__":
    screen = History_WT_CWA()
    screen.History()  
    input("Press Enter to exit.")
