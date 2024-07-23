

from datetime import datetime
import requests
import json , os
# from New_Account import Account_Settings_HBT_CWA




class Graphs_Setup:
    def __init__(self):
        self.pixela_endpoint=f"https://pixe.la/v1/users/"
        


    def New_Graph(self,user_name,token):
        self.user_name=user_name
        self.Token=token
        print("------------- Welcome to Habit Tracker -------------------\n")
        print("-------------  Create New Graph -------------------\n")
        print("""Note 1:
            \t[Required] You have to Create Graph to show track record in graphical way.
            \tOtherwise, no data will be accepted further.
              """)
        print("""Note 2:
            \t[Saved] Make Sure you save your graph id.
            \tIt will always required  as you perform any act.
              """)
        print("""Note 3:
            \t[Validation Rule] Make Sure you follow the rules
            \tAllowed: [a-z] [0-9] 
            \tLength: [1-16]  
            \tIf you exceed the length, y'll got an error.
              """)
        print("-------------  Enter All Required Values of Graph -------------------\n")
        User_Graph_ID=input("Enter your Graph ID   please:")
        Graph_name=input("Enter your Graph Name please:")
        Graph_unit=input("""Enter type of unit that your quantity should be tracked,
[Kilogram, Calory , Hours ] :""").lower()
        Graph_type=input("Enter your type of quantity [ int [1,2..] or float [2.3,5.3]  ]: ").lower()
        color_code=int(input("""Select your graph color
1: Green
2: Red
3: Blue
4: Yellow
5: Purple
6: Black
Enter Value: """))
        try:
            if color_code==1:
                color="shibafu"    
            elif color_code==2:
                color="momiji"    
            elif color_code==3:
                color="sora"    
                
            elif color_code==4:
                color="ichou"    
                
            elif color_code==5:
                color="ajisai"    
                
            elif color_code==6:
                color="kuro"    
                
        except TypeError as e:
            print("You Entered Wrong Type of Value.")
            
            
        graph_params={
                "id":User_Graph_ID,
                "name":Graph_name,
                "unit":Graph_unit,
                "type":Graph_type,
                "color":color,
            }
        self.header={
            "X-USER-TOKEN":self.Token
        }
        # New Graph Defination Endpoint 
        new_graph_endpoint=f"{self.pixela_endpoint}{self.user_name}/graphs"
        r=requests.post(url=new_graph_endpoint,json=graph_params,headers=self.header)
        # Create screen
        data=r.text
        print(r.json())
        # screen=Account_Settings_HBT_CWA()
        
        # print(screen.word_check(data))
        print(self.word_check(data))
        
        
    def delete_graph(self,username,token):
        self.user_name=username
        self.Token=token
        self.header={
            "X-USER-TOKEN":self.Token
        }
        self.graph_id = input("Enter your Graph id : ")
        del_graph_endpoint=f"{self.pixela_endpoint}{self.user_name}/graphs/{self.graph_id}"
        print(del_graph_endpoint)
        ask = input("Are you Sure to delete your Account? [yes/no]").lower()
        if ask == "yes":
            try:
                r=requests.delete(url=del_graph_endpoint,headers=self.header)
                print(r.text)
                data=r.text
                plain_text=self.word_check(data)
                if plain_text=="Success":
                    print(f"--------------  Your Graph is Deleted {plain_text}fully. -------------------\n")
                    print("------------               Code With Abubakar                -----------------\n")
                else:
                    print("Failed to Delete an account")
            except requests.exceptions.HTTPError as e:
                print(f"Failed to Delete an account:{e} ")
        elif ask == "no":
            print("The request has been canceled.")

        
    # delete_graph
    # view_graph
    # update_graph
        
    def word_check(self,data):
        self.data=data
        # To check the response of request 
        # Response Example:
        # {"message":"Success. Let's visit https://pixe.la/@yourusername , it is your profile page!","isSuccess":true}
        # so get the keyword [Success] from the text, i create this function to use multiple times
        lst=[]    
        for i in range(12,19):
            lst.append(data[i])
        # now join the list items to convert  into plain text
        plain_text="".join(lst)
        return plain_text    
        

# screen=Graphs_Setup()
# screen.New_Graph()