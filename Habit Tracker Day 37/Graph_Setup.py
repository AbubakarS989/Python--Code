

from datetime import datetime
import requests
import json , os



class Graphs_Setup:
    def __init__(self):
        self.graph_endpoint=f"https://pixe.la/v1/users/"


    def New_Graph(self):
        print("------------- Welcome to Habit Tracker -------------------\n")
        print("-------------  Create New Graph -------------------\n")
        print("""Note:
            \t[Required] You have to Create Graph to show track record in graphical way.
            \tOtherwise, no data will be accepted further.
              """)
        Graph_name=input("Enter your graph name please:")
        

# Create screen
screen=Graphs_Setup()
screen.New_Graph()