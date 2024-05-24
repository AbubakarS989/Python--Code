import html

def Email_Msg_Delete_Account(name, user_id, gmail, balance):
    msg = f"""
    <html>
    <body>
        <p>Hi {name},</p>
        <p>We are sorry to inform you that your account with Abubakar Bank has been successfully deleted.</p>
        
        <p>Account Details:</p>
        <p>User ID: {user_id}<br>
        Remaining Balance: {balance}<br>
        Email: {gmail}</p>
        
        <p>Thank you for using the Bank Management System App!</p>
        <p>Best regards,<br/>
        The Bank Management System - Abubakar Hafeez Team</p>
        <p>Security Tip: Protect your account by never sharing your password or authentication codes with others.</p>
        <p>Need Help?<br/>
        Visit our Help Center or contact us at <a href="mailto:abubakarhafeez66@gmail.com">abubakarhafeez66@gmail.com</a>.</p>
        <p>Bank Management System - Abubakar Hafeez, Inc.<br/>
        SadiqAbad, Pakistan</p>
        <p>Disclaimer: This message was sent to {gmail} in response to your request for an account deletion.
        If you have received this email in error, please disregard it.</p>
    </body>
    </html>
    """
    return msg



#! in case of checking

# from Email_emplate import Send_Email
# email_content = Email_Msg(234, "bakar", "abubakarhafeez66@gmail.com")
# Send_Email("abubakarhafeez66@gmail.com",email_content,"helo guys")