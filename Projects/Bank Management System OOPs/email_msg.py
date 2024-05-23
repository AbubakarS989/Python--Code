import html
def Email_Msg(pin, name, gmail,subject):
    msg = f"""
    <html>
    <body>
        <p>Hi {name},</p>
        <p>We received a request that you are {subject} at  'Bank Management System - Abubakar Hafeez' account ({gmail}).</p>
        <p>Please use the following code to complete your authentication:</p>
        <p style="font-size: 24px; font-weight: bold; color: black;">Your Authentication Code: {pin}</p>
        <p>If you did not request this code, it’s possible that someone else is trying to access your account.
        Do not forward or give this code to anyone. You can safely ignore this email if you did not request a code.</p>
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