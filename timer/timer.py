from winsound import Beep
from time import localtime, strftime, sleep
import keyboard

alarm_time=input("What time does the alarm sound?(Enter it in 24-hour format like 05:13 or 00:15):")
text = input("If your alarm has text, enter it:")
pattern = "%H:%M"


while True:
    now = strftime(pattern, localtime())
    if now==alarm_time:
        print(text)
        print("Your alarm time has come. It is now "+alarm_time)
        while True:
            Beep(1000,500)
            if keyboard.is_pressed("Esc"):
                break
        break
    sleep(15)
