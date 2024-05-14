import time
from plyer import notification

while True:
    notification.notify(
        title="Please drink water",
        message="Remember to stay hydrated. Drink some water!",
        app_icon="Projects\glass icon.ico",
        timeout=3,

    )
    time.sleep(60*2)
