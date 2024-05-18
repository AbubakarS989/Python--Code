def Send_Email(receive_email,content,Subject):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart  

    # Email configuration
    sender_email = "mhafeezmabubakar@gmail.com"
    receiver_email = receive_email
    password = "fryhdorkfsknzrdl"

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