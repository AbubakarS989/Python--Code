import datetime as dt
import pandas
import random
# current month
moth=dt.datetime.now().month
# current day
day=dt.datetime.now().day
# combine them into tuple
today=(moth,day)
# print(today)

# read date from the date csv
# pandas dataFrame
date_data=pandas.read_csv("dates.csv") 
# print(date_data)

# dict to store the birthday data for use

birthday_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in date_data.iterrows()}

# print(birthday_dict)

# check if the current day and month match with the birthday date
# then select the random letter from out of 3

if today in birthday_dict:
    # jis ki aj birthday ho gi, us ka data save ho jae ga
    birthday_person=birthday_dict[today]
    file_path=f"letter Templete/letter{random.randint(1,3)}.txt"
    # print(file_path)
    # read text from the selected file
    with open(file_path) as letter_file:
        content=letter_file.read()
        content=content.replace("[name]",birthday_person["name"])
    print(content)
    # ! Email Format and Code 
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart  

    # Email configuration
    sender_email = "mhafeezmabubakar@gmail.com"
    receiver_email = birthday_person["email"]
    password = "fryhdorkfsknzrdl"

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Birthday Wishes!"

    # Add body to email
    body = content
    message.attach(MIMEText(body, "plain"))

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    # Send email
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)

    # Close the connection
    server.quit()

    print("Email sent successfully.")










