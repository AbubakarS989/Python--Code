# First import libraries

import os
import mysql.connector
from dotenv import load_dotenv
# load the environment variables
load_dotenv()

#? connect to sql database
try:
    db=mysql.connector.connect(
        host="localhost",
        user=os.environ["USER"], #it store in my env file
        passwd=os.environ["PASSWORD"],
        database="yt_test" #enter your database name after created
    )
except EOFError as e:
    print(e)



# create cursor 
my_cursor=db.cursor()

# NOw create a database 

my_cursor.execute("CREATE DATABASE IF NOT EXISTS yt_test")

# Table query
create_table_query="""
CREATE TABLE IF NOT EXISTS data(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    class INT
);
"""
#Execute the query
try:
    my_cursor.execute(create_table_query)
    print("Table is created successfully.")
except EOFError as e:
    print(e)
    
    

# Insert data into table 
# i use loop to insert multiple values at onces

#? method 1: to insert data
# for _ in range(0,3):
#     name=input("Enter your name: ")
#     class_=input("Enter your class: ")
#     sql="INSERT INTO data (name,class) VALUES (%s,%s)"
#     # insert tuple
#     values=(name,class_,)
#     my_cursor.execute(sql,values)
    
# our data is storing successfully.
# now use method 2 to insert data
# ? method w2: to insert data
for _ in range(0,3):
    name=input("Enter your name: ")
    class_=input("Enter your class: ")

    sql=f"INSERT INTO data (name,class) VALUES ('{name}','{class_}')"
    my_cursor.execute(sql)





db.commit()
my_cursor.close()
db.close()


# ? Today we learn :
    # How to connect with database
    # How to create database
    # How to create table
    # How to insert data into table:
        # Method 1: secure 
        # Method 1: lightly secure
    
    
# If you guys like this, comment share and suggest me some other videos also
# stay tunned 
# code with Abubakar


