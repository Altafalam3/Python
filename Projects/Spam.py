import pyautogui as spam
import time

Msg=("spammer is back")

time.sleep(10)

while True:
   spam.typewrite(Msg)
   spam.press('Enter')
