

import os
import json
from datetime import datetime
import requests
from colorama import Fore, Back, Style, init  # For Colors
# Initializer of colorama
init()


#? List of functions Created in this file:
# 1:  graph_id_note() 
# 2:  New_Graph()
# 3:  view_graph()
# 4:  update_graph()
# 6:  delete_graph()
# 7: word_check()



class Graphs_Setup:
     
    
    def __init__(self):
        
        
        self.Graph_name_update=""
        self.Graph_unit=""
        self.pixela_endpoint = f"https://pixe.la/v1/users/"
    
    
    
        
    def graph_id_note(self):
        """
        Important Notes that will display where is needed
        """
        
        
        
        print(f"""{Fore.RED}Note 2:{Style.RESET_ALL}
            \t[Saved] Make Sure you save your {Fore.GREEN}graph id{Style.RESET_ALL}.
            \tIt will always required  as you perform any act.
              """)
        print(f"""{Fore.RED}Note 3:{Style.RESET_ALL}
            \t[Validation Rule] Make Sure you follow the rules of {Fore.GREEN}graph id{Style.RESET_ALL}
            \tAllowed: [a-z] [0-9]
            \tLength: [1-16]
            \tIf you exceed the length, y'll got an error.
              """)
        
        
        
    def New_Graph(self, user_name, token):
        """
        Input 1
        Input 2
        Input 3
        Input 4
        """
        
        self.user_name = user_name
        self.Token = token
        print(f"------------- {Fore.GREEN}Welcome to Habit Tracker{Style.RESET_ALL} -------------------\n")
        print(f"-------------  {Fore.LIGHTMAGENTA_EX}Create New Graph{Style.RESET_ALL} -------------------\n")
        print(f"-------------  {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL} -------------------\n")
        print(f"""{Fore.RED}Note 1:{Style.RESET_ALL}
            \t[Required] You have to Create Graph to show track record in graphical way.
            \tOtherwise, no data will be accepted further.
              """)
        
        self.graph_id_note()
        
        print(f"-------------  {Fore.YELLOW}Enter All Required Values of Graph{Style.RESET_ALL} -------------------\n")
        User_Graph_ID = input("Enter  New your Graph ID   please [ID can't Change after submit]:")
        Graph_name = input("Enter New  Graph Name please:")
        Graph_unit = input("""Enter type of unit that your quantity should be tracked,[Kilogram, Calory , Hours ] :""").lower()
        Graph_type = input("Enter  type of quantity [ int [1,2..] or float [2.3,5.3]  ]: ").lower()
        color_code = int(input(f"""Select your graph color{Fore.LIGHTYELLOW_EX}
1: Green
2: Red
3: Blue
4: Yellow
5: Purple
6: Black{Style.RESET_ALL}
Enter Value: """))
        
        
        try:
            if color_code == 1:
                color = "shibafu"
            elif color_code == 2:
                color = "momiji"
            elif color_code == 3:
                color = "sora"

            elif color_code == 4:
                color = "ichou"

            elif color_code == 5:
                color = "ajisai"

            elif color_code == 6:
                color = "kuro"

        except TypeError as e:
            print("You Entered Wrong Type of Value.")
            
            
        graph_params = {
            "id": User_Graph_ID,
            "name": Graph_name,
            "unit": Graph_unit,
            "type": Graph_type,
            "color": color,
        }
        
        
        self.header = {
            "X-USER-TOKEN": self.Token
        }
        
        
        # New Graph Definition Endpoint
        new_graph_endpoint = f"{self.pixela_endpoint}{self.user_name}/graphs"
        
        
        r = requests.post(url=new_graph_endpoint,json=graph_params, headers=self.header)
        data = r.text
        print(r.json())

        # print(screen.word_check(data))
        print(self.word_check(data))



    def view_graph(self, username):
        """
        [Input]: Username
        Provide the link of graph pic
        """
        
        
        print(f"------------- {Fore.LIGHTMAGENTA_EX}View your Graph{Style.RESET_ALL}  -------------------\n")
        print(f"-------------  {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL} -------------------\n")
        
        
        self.user_name = username
        self.graph_id = input("Enter your Graph id : ")
        
        
        view_graph_Endpoint = f"{self.pixela_endpoint}{self.user_name}/graphs/{self.graph_id}"
        urls = view_graph_Endpoint
        
        
        try: 
            r = requests.get(url=view_graph_Endpoint)
            
            print(f"------------              {Fore.LIGHTYELLOW_EX} Code With Abubakar{Style.RESET_ALL}                -----------------\n")
            print(f"Check out the [{Fore.RED}link{Style.RESET_ALL}] to view graph:\n")
            print(f"\t\t :> {Fore.YELLOW}{urls}{Style.RESET_ALL}")

        except requests.exceptions.HTTPError as e:
            print(f"Failed to Delete an account:{e} ")



    def update_graph(self,username,token):
        """
        [Input] 1: Username
        [Input] 2: Token
        """
        
        
        self.user_name = username
        self.Token = token
        
        # PUT /v1/users/<username>/graphs/<graphID>
        self.graph_id = input("Enter your Graph id : ")
        print(f"------------- {Fore.LIGHTMAGENTA_EX}Update your Graph{Style.RESET_ALL}  -------------------\n")
        print(f"-------------  {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL} -------------------\n")
        print(f"""1: Change Graph Name.
2: Change Graph color.
3: Change Graph Unit.
4: Exit.""")
        
        ask = input("Enter Your Choice: ")
        try:
            ask = int(ask)
            if ask==1:
                self.graph_id_note()
                self.Graph_name_update = input("Enter your Update Graph Name please:")
            elif ask == 2:
                color_code = input(f"""{Fore.LIGHTYELLOW_EX}Select your graph color:
1: Green
2: Red
3: Blue
4: Yellow
5: Purple
6: Black{Style.RESET_ALL}
Enter Value: """)
                try:
                    color_code = int(color_code)
                    if color_code == 1:
                        color = "shibafu"
                    elif color_code == 2:
                        color = "momiji"
                    elif color_code == 3:
                        color = "sora"
                    elif color_code == 4:
                        color = "ichou"
                    elif color_code == 5:
                        color = "ajisai"
                    elif color_code == 6:
                        color = "kuro"
                except TypeError as e:
                    print("Enter Valid Option.")
            elif ask == 3 :
                self.Graph_unit = input("""Enter type of unit that your quantity should be tracked,[Kilogram, Calory , Hours ] :""").lower()
        except TypeError as e:
            print("Enter Valid Option.")
        
            
        graph_params = {
            "name": self.Graph_name_update,
            "unit": self.Graph_unit,
            "color": color,
        }
        
        
        self.header = {
            "X-USER-TOKEN": self.Token
        }
        
        
        # To make my code general, I take graph id for each time the user perform any action 
        self.graph_id = input("Enter your Graph id : ")
        
        
        # Update Graph Definition Endpoint
        update_graph_endpoint = f"{self.pixela_endpoint}{self.user_name}/graphs/{self.graph_id}"
        r = requests.put(url=update_graph_endpoint,json=graph_params, headers=self.header)
        
        data = r.text
        # print(r.text)
        
        
        plain_text=self.word_check(data)
        if plain_text == "Success":
            print(f"\n--------------  {Fore.GREEN}Your Value is Updated {plain_text}fully.{Style.RESET_ALL} -----------------\n")
            print(f"-------------------         {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}        ----------------------\n")
        else:
            print(f"{Fore.GREEN}Failed to Update your Account{Style.RESET_ALL}")
    
    
    
    def delete_graph(self, username, token):
        """
        [Input] 1: Username
        [Input] 2: Token
        """
        self.user_name = username
        self.Token = token
        self.header = {
            "X-USER-TOKEN": self.Token
        }
        
        print(f"-------------       {Fore.GREEN}    Habit Tracker{Style.RESET_ALL} -------------------\n")
        print(f"------------- {Fore.LIGHTMAGENTA_EX}Delete Your Graph {Style.RESET_ALL} -------------------\n")
        print(f"-------------  {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL} -------------------\n")
        
        
        self.graph_id = input("Enter your Graph id : ")
        del_graph_endpoint = f"{self.pixela_endpoint}{self.user_name}/graphs/{self.graph_id}"
        
        # print(del_graph_endpoint)
        
        
        ask = input(f"{Fore.LIGHTRED_EX}Are you Sure to delete your graph?{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}[yes/no{Style.RESET_ALL} ").lower()
        if ask == "yes":
            try:
                r = requests.delete(url=del_graph_endpoint,headers=self.header)
                print(r.text)
                data = r.text
                plain_text = self.word_check(data)
                
                
                if plain_text == "Success":
                    print(f"--------------  {Fore.RED}Your Graph is Deleted {plain_text}fully.{Style.RESET_ALL} -------------------\n")
                    print(f"------------               {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}                -----------------\n")
                else:
                    print(f"{Fore.LIGHTRED_EX}Failed to Delete an account{Style.RESET_ALL}")
            except requests.exceptions.HTTPError as e:
                print(f"{Fore.RED}Failed to Delete an account:{Style.RESET_ALL}{e} ")
        elif ask == "no":
            print(f"{Fore.GREEN}The request has been canceled.{Style.RESET_ALL}")



    def word_check(self, data):
        """
        It Slice the sentence and store into list
        Then return [Success] word 
        Basically used for confirmation from Api request
        """
        
        self.data = data
        # To check the response of request
        # Response Example:
        # {"message":"Success. Let's visit https://pixe.la/@yourusername , it is your profile page!","isSuccess":true}
        # so get the keyword [Success] from the text, I create this function to use multiple times
        lst = []
        for i in range(12, 19):
            lst.append(data[i])
        # now join the list items to convert  into plain text
        plain_text = "".join(lst)
        return plain_text


# screen=Graphs_Setup()
# screen.New_Graph()
