import os
from dotenv import load_dotenv


load_dotenv() #take environment from .env
# print(sender_email)
# print(receive_email)
# print(password)

def Send_Email(content,Subject):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart  

    sender_email=os.environ["SENDER_EMAIL"]
    receiver_email=os.environ["RECIEVER_EMAIL"]
    password=os.environ["PASS"]
    # Email configuration


    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = Subject

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

    return "Email sent successfully."