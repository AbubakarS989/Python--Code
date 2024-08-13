
# Python Script to Connect to MySQL, Create Database and Table, and Insert Data

## 1. Import Necessary Libraries

First, you need to import the necessary libraries for the script.

```python
import os
import mysql.connector
from dotenv import load_dotenv

os:  This module provides a way to use operating system-dependent functionality.
mysql.connector*: This is the MySQL Connector library, which allows Python to interact with a MySQL database.
dotenv: This module loads environment variables from a .env file into your Python environment.