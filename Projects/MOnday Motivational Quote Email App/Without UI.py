import datetime as dt
import random

now=dt.datetime.now()
weekday=now.weekday()
if weekday==1:

    with open("quote.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote=random.choice(all_quotes)
    print(quote)
    # ! Email
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # Email configuration
    sender_email = "mhafeezmabubakar@gmail.com"
    receiver_email = "mshafeez6566@gmail.com"
    password = "fryhdorkfsknzrdl"

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Monday Motivate Quote"

    # Add body to email
    body = quote
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

