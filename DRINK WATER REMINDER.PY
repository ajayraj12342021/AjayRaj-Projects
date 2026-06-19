import time
from plyer import notification

while True:
    print("Please sip some water.")

    notification.notify(title="Drink water.",message="Please drink some water.")
    time.sleep(60*60*60)