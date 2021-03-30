from winsound import Beep
from time import localtime, strftime, sleep

alarm_time=input("What time does the alarm sound?(Enter 05 13 or 00 15 in 24-hour format):")
text = input("If your alarm has text, enter it:")
pattern = "%H %M"


while True:
    now = strftime(pattern, localtime())
    if now==alarm_time:
        print(text)
        print("Your alarm time has come. It is now "+alarm_time)
        for i in range(3):
            Beep(1000,500)
        break
    sleep(15)
