import html
def Email_Msg_Send_MONey(receiver_name,sender_name, gmail, money,balance):
    msg = f"""
    <html>
    <body>
        <p>Hi {receiver_name},</p>
        <p>We are pleased to inform you that RS:<p style="font-size: 20px; font-weight: bold; color: black;">{money}</p> has been successfully received into your 'Abubakar Bank ' account from {sender_name}.
        
        
        <br>Recipient Name: {receiver_name}<br>
        Sender Name: {sender_name}<br>
        Send Amount: {money}<br>
        Your Account Balance: {balance}<br>
        
        <p>Thank you for using the Bank Management System App!</p>
        <p>Best regards,<br/>
        The Bank Management System - Abubakar Hafeez Team</p>
        <p>Security Tip: Protect your account by never sharing your password or authentication codes with others.</p>
        <p>Need Help?<br/>
        Visit our Help Center or contact us at <a href="mailto:abubakarhafeez66@gmail.com">abubakarhafeez66@gmail.com</a>.</p>
        <p>Bank Management System - Abubakar Hafeez, Inc.<br/>
        SadiqAbad, Pakistan</p>
        <p>Disclaimer: This message was sent to {gmail} in response to your request for an authentication code.
        If you have received this email in error, please disregard it.</p>
    </body>
    </html>
    """
    return msg


#! in case of checking

# from Email_emplate import Send_Email
# email_content = Email_Msg(234, "bakar", "abubakarhafeez66@gmail.com")
# Send_Email("abubakarhafeez66@gmail.com",email_content,"helo guys")