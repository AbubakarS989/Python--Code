
# Python Script to Connect to MySQL, Create Database and Table, and Insert Data

## 1. Import Necessary Libraries

First, you need to import the necessary libraries for the script.

```python
import os
import mysql.connector
from dotenv import load_dotenv
```
## os:
  This module provides a way to use operating system-dependent functionality.
## mysql.connector: 
  This is the MySQL Connector library, which allows Python to interact with a MySQL database.
dotenv: This module loads environment variables from a .env file into your Python environment.

## 2. Load Environment Variables
Use the load_dotenv() function to load your environment variables from a .env file. 
This is important for keeping sensitive data like database credentials secure.

```
load_dotenv()
```

## 3. Connect to the MySQL Database
Next, we establish a connection to the MySQL database using the mysql.connector.connect() method. The host, user, and passwd values are retrieved from the environment variables.
```
try:
    db = mysql.connector.connect(
        host="localhost",
        user=os.environ["USER"],  # The username stored in your .env file
        passwd=os.environ["PASSWORD"],  # The password stored in your .env file
        database="yt_test"  # The database you want to connect to (it will be created if it doesn’t exist)
    )
except EOFError as e:
    print(e)
```

## 4. Create a Cursor Object
After establishing a connection, create a cursor object. This cursor allows you to execute SQL queries
```
my_cursor = db.cursor()
```
## 5. Create a Database (If It Doesn't Exist)
We can now create a database named yt_test using the CREATE DATABASE IF NOT EXISTS SQL statement.
```
my_cursor.execute("CREATE DATABASE IF NOT EXISTS yt_test")
```
## 6. Create a Table
Next, create a table named data inside the yt_test database. The table will contain three columns: id, name, and class.
```
create_table_query = """
CREATE TABLE IF NOT EXISTS data(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    class INT
);
"""
# Execute the query
try:
    my_cursor.execute(create_table_query)
    print("Table is created successfully.")
except EOFError as e:
    print(e)
```
## 7. Insert Data into the Table
You can now insert data into the data table. There are two methods provided for inserting data:

## Method 1: Secure Method (Parameterized Query)
This method uses parameterized queries, which are more secure against SQL injection.
```
for _ in range(0, 3):
    name = input("Enter your name: ")
    class_ = input("Enter your class: ")
    sql = "INSERT INTO data (name, class) VALUES (%s, %s)"
    values = (name, class_,)
    my_cursor.execute(sql, values)
```
## Method 2: Simple Method (Using String Formatting)
This method uses string formatting to insert values into the query. While it's simpler, it's less secure against SQL injection.
```
for _ in range(0, 3):
    name = input("Enter your name: ")
    class_ = input("Enter your class: ")

    sql = f"INSERT INTO data (name, class) VALUES ('{name}', '{class_}')"
    my_cursor.execute(sql)
```

## 8. Commit Changes and Close the Connection
After inserting the data, use the commit() method to save the changes, and then close both the cursor and the database connection.
```
db.commit()
my_cursor.close()
db.close()
```

# Summary
In this script, we have learned:

  How to connect to a MySQL database using Python.<br>
  How to create a database.<br>
  How to create a table.<br>
  How to insert data into the table using two different methods:<br>
      *Method 1* : Secure, using parameterized queries.<br>
      *Method 2* : Simple, using string formatting.<br>
If you found this tutorial helpful, please comment, share, and suggest other topics you'd like to see. Stay tuned for more!

## Code with Abubakar
I’m Abubakar, a passionate python developer and graphic designer dedicated to helping others learn and grow in the field of technology. Whether you’re just starting out or looking to refine your skills, I’m here to share knowledge and guide you on your journey.
# INSTAGRAM: [codexdesign](https://www.instagram.com/codexdeisgn/)
