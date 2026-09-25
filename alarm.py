from datetime import datetime
import os
import time
import keyboard as kb

question = input("Pick a Hour 00:00, 24:00: ")

print(f"wait for {question}")

while True:
    now = datetime.now().strftime("%H:%M")

    if now == question:
        os.startfile("alarm.mp3")
        break

kb.wait("q")

os.system("taskkill /f /im Microsoft.Media.Player.exe")

time.sleep(1)
