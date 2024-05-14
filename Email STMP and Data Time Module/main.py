# import smtplib #---< allow us to work with emails

# my_email="mhafeezmabubakar@gmail.com"
# connection=smtplib.SMTP("smtp.gmail.com") # connection is established
# # TLS -> Transport Layer Security
# # provide security to our connection
# connection.starttls()

# # login 
# connection.login(user=my_email,password="fryhdorkfsknzrdl")
# # send mail
# connection.sendmail(from_addr=my_email,to_addrs="abubakarhafeez66@gmail.com",msg="Hi from python")

# # connection closed
# connection.close()    
# ! Send mail to anyone
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "mhafeezmabubakar@gmail.com"
receiver_email = "abubakarhafeez66@gmail.com"
password = "fryhdorkfsknzrdl"

# Create a multipart message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email from Python"

# Add body to email
body = "This is a test email sent from Python."
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
