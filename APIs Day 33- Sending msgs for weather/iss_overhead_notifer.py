import requests
import time
from datetime import datetime



# ! SadiqAbad City Pakistan
latitude=28.310350
longitude=70.127403

def is_night():
    parameters={
    "lat":latitude,
    "lng":longitude,
    "formatted":0
    }
    # current time
    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()
    sunrise=data["results"]["sunrise"]
    sunset=data["results"]["sunset"]


    # take hour value from the entire date time
    list_data_R=sunrise.split(":")
    list_data_S=sunset.split(":")
    # print(list_data[1])
    API_hour_sunrise=int(list_data_R[1])
    API_hour_sunset=int(list_data_S[1])
    time_now_hour=datetime.now().hour
    print(time_now_hour)

    if time_now_hour>= API_hour_sunset or time_now_hour<= API_hour_sunrise:
    #    it's  Dark  mean night time
        return True

def is_iss_overhead():

    #! iss location
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()
    iss_longitude=float(data["iss_position"]["latitude"])
    iss_latitude=float(data["iss_position"]["longitude"])
    print(iss_latitude)
    print(iss_longitude)


    # Our position is within +5 or -5 degrees of the ISS
    # 28-5=23
    # 28+5=33
    # above numbers are within the range of ISS
    if latitude-5 <= iss_latitude <=latitude+5 and longitude-5 <=iss_longitude <=longitude+5:
        return True




# If both function return true then we send ourself an email that
# describe ISS is overhead (over of home )


def Email():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # Email configuration
    sender_email = "mhafeezmabubakar@gmail.com"
    password = "fryhdorkfsknzrdl"

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = sender_email
    message["Subject"] = "Look UP"

    # Add body to email
    body = "ISS is overhead just look uP!"
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
    messagebox.showinfo(title="Email Send", message="Email sent successfully.")

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        # ! Email
        Email()


