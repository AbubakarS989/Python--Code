import re


def check_email_secure(gmail):
    """
    This module takes one parameter:-> Gmail
    - Returns a string in case of True ("Secure Email. Thank You")
    - Returns a string in case of False ("Invalid Email: reason. Please Re-Check Your Email. Thank You")
    """
    
    """
    It check the following 
    Check @
    Check . dot
    Check lowercase,uppercase
    Check number
    Check symbols
    """

    # Check if @ is present
    if "@" not in gmail:
        print("Invalid Email: '@' is missing. Please Re-Check Your Email. Thank You")
        return False

    # Check if . is present
    if "." not in gmail:
        print("Invalid Email: Dot '.' is missing. Please Re-Check Your Email. Thank You")
        return False

    # Check for special symbols
    # The code snippet you provided is checking if the email address contains any special symbols from
    # the `special_symbols` string.
    special_symbols = '!@#$%^&*(),.{?":}|<>'
    if any(char in special_symbols for char in gmail):
        print("Invalid Email: Special symbols are not allowed. Please Re-Check Your Email. Thank You")
        return False

    # Get start character of gmail until @
    email_char = gmail.split("@")[0]

    # Check if email contains at least one alphabet character
    if not any(char.isalpha() for char in email_char):
        print("Invalid Email: Email must contain at least one alphabet character (a-zA-Z). Please Re-Check Your Email. Thank You")
        return False

    # Check length of email_char
    if not 6 <= len(email_char) <= 30:
        print("Invalid Email: Gmail ID length should be between 6 and 30 characters. Please Re-Check Your Email. Thank You")
        return False

    print("Email is Secure, Good to go!")
    return True




def check_password(password):
    """
    This module takes one parameter:-> Password
    - Returns a string in case of True ("Password is strong, Good to go!")
    - Returns a string in case of False ("Invalid Password:Please Re-Create Your Password. Thank You")
    """

    """
    It check the following 
    Check length
    Check Uppercase
    Check lowercase
    Check number
    Check symbols
    """
    # Check length
    if len(password) < 8:
        print("Invalid Password: Password is too short, it should be at least 8 characters. Please Re-Create Your Password. Thank You")
        return False

    # Check Uppercase
    if not re.search(r"[A-Z]", password):
        print("Invalid Password: Password should contain at least 1 uppercase letter. Please Re-Create Your Password. Thank You")
        return False

    # Check lowercase
    if not re.search(r"[a-z]", password):
        print("Invalid Password: Password should contain at least 1 lowercase letter. Please Re-Create Your Password. Thank You")
        return False

    # Check number
    if not re.search(r"[1-9]", password):
        print("Invalid Password: Password should contain at least 1 digit. Please Re-Create Your Password. Thank You")
        return False

    # Check symbol
    special_symbols = '!@#$%^&*(),.{?":}|<>'
    if not any(char in special_symbols for char in password):
        print("Invalid Password: Password should contain at least 1 special symbol. Please Re-Create Your Password. Thank You")
        return False

    print("Password is strong, Good to go!")
    return True



if __name__ == "__main__":
    check_email_secure()
    check_password()
